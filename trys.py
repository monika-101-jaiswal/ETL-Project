import streamlit as st
from E_and_T import get_dashboard_data


st.set_page_config(
    page_title="Energy Analytics Dashboard",
    page_icon="⚡",
    layout="wide"
)


st.title("⚡ Energy Analytics Dashboard")


(
    total_all,
    total_ge,
    category_count,
    category_count_ge,
    final_pivot
) = get_dashboard_data()


# ==========================================
# PUBLIC DISPLAY NAME MAPPING
# ==========================================

display_names = {
    "WC 1-Phase": "Type A",
    "WC 3-Phase": "Type B",
    "LTCT": "Type C",
    "HTCT": "Type D"
}


# ==========================================
# KPI
# ==========================================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Total Records",
        value=f"{total_all:,}"
    )

with col2:
    st.metric(
        label="Category A Records",
        value=f"{total_ge:,}"
    )


st.markdown("---")


# ==========================================
# ALL RECORDS
# ==========================================

st.subheader("📊 Record Type Distribution")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        display_names["WC 1-Phase"],
        f"{category_count['WC 1-Phase']:,}"
    )

with col2:
    st.metric(
        display_names["WC 3-Phase"],
        f"{category_count['WC 3-Phase']:,}"
    )

with col3:
    st.metric(
        display_names["LTCT"],
        f"{category_count['LTCT']:,}"
    )

with col4:
    st.metric(
        display_names["HTCT"],
        f"{category_count['HTCT']:,}"
    )


st.markdown("---")


# ==========================================
# CATEGORY A
# ==========================================

st.subheader("⚡ Category A Record Distribution")

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        display_names["WC 1-Phase"],
        f"{category_count_ge['WC 1-Phase']:,}"
    )

with col2:
    st.metric(
        display_names["WC 3-Phase"],
        f"{category_count_ge['WC 3-Phase']:,}"
    )

with col3:
    st.metric(
        display_names["LTCT"],
        f"{category_count_ge['LTCT']:,}"
    )

with col4:
    st.metric(
        display_names["HTCT"],
        f"{category_count_ge['HTCT']:,}"
    )


st.markdown("---")


# ==========================================
# PIVOT TABLE
# ==========================================

st.subheader("📋 Category vs Status")


# Copy so original dataframe is not changed
public_pivot = final_pivot.copy()


# Rename index
public_pivot.index = public_pivot.index.map(
    lambda x: display_names.get(x, x)
)

# Generic index name
public_pivot.index.name = "Category"

# Generic column names
public_pivot.columns = [
    f"Status {i+1}"
    for i in range(len(public_pivot.columns))
]

public_pivot.index = [
    f"Category {i+1}"
    for i in range(len(public_pivot.index))
]

st.dataframe(
    public_pivot.style.format("{:,.0f}"),
    use_container_width=True,
    height=500
)


# ==========================================
# DOWNLOAD
# ==========================================

csv = public_pivot.to_csv().encode("utf-8")


st.download_button(
    label="📥 Download Analytics CSV",
    data=csv,
    file_name="Analytics_Summary.csv",
    mime="text/csv"
)