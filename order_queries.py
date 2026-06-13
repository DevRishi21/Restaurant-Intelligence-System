order_queries = {
    "Which restaurants generate the highest order revenue?":
    """
        SELECT
        restaurant_name,
        ROUND(SUM(order_value), 2) AS total_revenue,
        COUNT(*) AS total_orders
        FROM orders
        GROUP BY restaurant_name
        ORDER BY total_revenue DESC
        LIMIT 10;
    """,
    "Which months receive the highest number of orders?":
    """
        SELECT
        TO_CHAR(order_date, 'MONTH') AS month,
        COUNT(*) AS total_orders
        FROM orders
        GROUP BY month
        ORDER BY total_orders DESC;
    """,
    "Do discounts increase customer spending?":
    """
        SELECT
        discount_used,
        ROUND(AVG(order_value), 2) AS avg_order_value,
        COUNT(*) AS total_orders
        FROM orders
        GROUP BY discount_used;
    """,
    "Which payment methods are most preferred?":
    """
        SELECT
        payment_method,
        COUNT(*) AS total_orders,
        ROUND(AVG(order_value), 2) AS avg_order_value
        FROM orders
        GROUP BY payment_method
        ORDER BY total_orders DESC;
     """,
     "Which restaurants have the highest average order value?":
    """
        SELECT
        restaurant_name,
        ROUND(AVG(order_value), 2) AS avg_order_value,
        COUNT(*) AS total_orders
        FROM orders
        GROUP BY restaurant_name
        ORDER BY avg_order_value DESC
        LIMIT 10;
    """
}