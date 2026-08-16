import psycopg2
import pandas as pd
import numpy as np


def get_dashboard_data():

    conn = psycopg2.connect(
        host="localhost",
        database="RMS_Data",
        user="postgres",
        password="Monika321",
        port="5432"
    )

    cursor = conn.cursor()

    sql = """
    SELECT
        acct_id,
        meter_badge_no,
        load,
        con_status,
        supply_type
    FROM public.genus_data
    """

    cursor.execute(sql)

    header = [desc[0] for desc in cursor.description]

    batch_size = 500000

    total_all = 0
    total_ge = 0

    category_count = {
        "WC 1-Phase": 0,
        "WC 3-Phase": 0,
        "LTCT": 0,
        "HTCT": 0
    }

    category_count_ge = {
        "WC 1-Phase": 0,
        "WC 3-Phase": 0,
        "LTCT": 0,
        "HTCT": 0
    }

    lookup = pd.read_excel(
        r"C:\Users\Admin\OneDrive - Genus Power Infrastructures Ltd\Desktop\Supply Type vs Tariff Type.xlsx"
    )

    lookup["SUPPLY_TYPE"] = (
        lookup["SUPPLY_TYPE"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    lookup_df = lookup.drop_duplicates(
        subset=["SUPPLY_TYPE"]
    ).copy()

    final_pivot = None

    while True:

        rows = cursor.fetchmany(batch_size)

        if not rows:
            break

        df = pd.DataFrame(rows, columns=header)

        df["supply_type"] = (
            df["supply_type"]
            .astype(str)
            .str.strip()
            .str.upper()
        )
        
        df = df.merge(
            lookup_df[["SUPPLY_TYPE", "tarrif"]],
            left_on="supply_type",
            right_on="SUPPLY_TYPE",
            how="left"
        )
        
        pivot = pd.pivot_table(
            df,
            index="tarrif",
            columns="con_status",
            aggfunc="size",
            fill_value=0
        )

        if final_pivot is None:
            final_pivot = pivot
        else:
            final_pivot = final_pivot.add(
                pivot,
                fill_value=0
            )
            
        total_all += len(df)

        df["load"] = pd.to_numeric(
            df["load"],
            errors="coerce"
        ).fillna(0)

        conditions = [
            df["load"] <= 5,
            (df["load"] > 5) & (df["load"] <= 25),
            (df["load"] > 25) & (df["load"] <= 50),
            df["load"] > 50
        ]

        choices = [
            "WC 1-Phase",
            "WC 3-Phase",
            "LTCT",
            "HTCT"
        ]

        df["TYPE"] = np.select(
            conditions,
            choices,
            default="WC 1-Phase"
        )

        counts = df["TYPE"].value_counts()

        for meter_type, count in counts.items():
            category_count[meter_type] += count

        df_ge = df[
            df["meter_badge_no"]
            .astype(str)
            .str.startswith("GE", na=False)
        ].copy()

        total_ge += len(df_ge)

        ge_counts = df_ge["TYPE"].value_counts()

        for meter_type, count in ge_counts.items():
            category_count_ge[meter_type] += count

        del df
        del df_ge

    final_pivot = (
        final_pivot
        .fillna(0)
        .astype(int)
    )

    cursor.close()
    conn.close()

    return (
        total_all,
        total_ge,
        category_count,
        category_count_ge,
        final_pivot
    )