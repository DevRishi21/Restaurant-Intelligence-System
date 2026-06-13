import streamlit as st
import pandas as pd

from database import engine
from restaurant_queries import restaurant_queries
from order_queries import order_queries

st.title(
    "Uber Eats Bangalore Restaurant Intelligence & Decision Support System"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Restaurant FAQs",
        "Orders FAQs"
    ]
)

# =====================================================
# DASHBOARD PAGE
# =====================================================
if page == "Dashboard":

    st.header("Restaurant Dashboard")

    # Load filter values from SQL
    locations = pd.read_sql(
        """
        SELECT DISTINCT location
        FROM restaurants
        WHERE location IS NOT NULL
        ORDER BY location
        """,
        engine
    )

    locations = locations["location"].tolist()

    # Filters
    selected_location = st.selectbox(
        "Location",
        ["All"] + locations
    )

    selected_online_order = st.selectbox(
        "Online Ordering",
        ["All", "Yes", "No"]
    )

    selected_book_table = st.selectbox(
        "Table Booking",
        ["All", "Yes", "No"]
    )

    selected_price_segment = st.selectbox(
        "Price Segment",
        [
            "All",
            "Budget",
            "Mid Range",
            "High",
            "Premium"
        ]
    )

    # Build SQL dynamically
    query = """
    SELECT
        restaurant_id,
        name,
        location,
        rate,
        pricing_segment,
        ratings_category,
        online_order,
        book_table,
        cuisines,
        approx_cost_for_two
    FROM restaurants
    WHERE 1=1
    """

    if selected_location != "All":
        query += f" AND location = '{selected_location}'"

    if selected_online_order != "All":
        query += f" AND online_order = '{selected_online_order}'"

    if selected_book_table != "All":
        query += f" AND book_table = '{selected_book_table}'"

    if selected_price_segment != "All":
        query += f" AND pricing_segment = '{selected_price_segment}'"

    query += " ORDER BY rate DESC NULLS LAST"

    if st.button("Apply Filters"):

        filtered_df = pd.read_sql(
            query,
            engine
        )

        st.subheader("Filtered Restaurant Results")

        st.dataframe(
            filtered_df,
            use_container_width=True
        )

        st.write(
            f"Total Records Found: {len(filtered_df)}"
        )

# analysis_type = st.selectbox(
#     "Select Analysis Type",
#     ["Restaurant Insights", "Order Insights"]
# )

# Restaurant Insights
elif page == "Restaurant FAQs":

    question = st.selectbox(
        "Select Business Question",
        list(restaurant_queries.keys())
    )

    if st.button("Execute Query"):

        query = restaurant_queries[question]

        result = pd.read_sql(
            query,
            engine
        )

        st.dataframe(result)

# Order Insights
elif page == "Orders FAQs":

    question = st.selectbox(
        "Select Business Question",
        list(order_queries.keys())
    )

    if st.button("Execute Query"):

        query = order_queries[question]

        result = pd.read_sql(
            query,
            engine
        )

        st.dataframe(result)