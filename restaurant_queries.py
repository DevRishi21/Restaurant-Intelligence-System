restaurant_queries = {
    "Which Bangalore locations have the highest average restaurant ratings?":
    """
        SELECT location, AVG(rate) as avg_ratings, ratings_category
        FROM restaurants
        WHERE rate is NOT NULL
        GROUP BY location, ratings_category
        ORDER BY avg_ratings DESC
    """,
    "Which locations are over-saturated with restaurants?":
    """
        SELECT location, COUNT(location) as total_restaurants
        FROM restaurants
        GROUP BY location
        ORDER BY total_restaurants DESC
        LIMIT 5
    """,
    "Does online ordering improve restaurant ratings?":
    """
        SELECT online_order, ROUND(AVG(rate), 2) AS avg_rating, COUNT(*) AS restaurant_count
        FROM restaurants
        WHERE rate IS NOT NULL
        GROUP BY online_order;
    """,
    "Does table booking correlate with higher customer ratings?":
    """
        SELECT book_table as table_booking, ROUND(AVG(rate), 2) AS avg_rating, COUNT(*) AS restaurant_count
        FROM restaurants
        WHERE rate IS NOT NULL
        GROUP BY table_booking;
    """,
    "What price range delivers the best customer satisfaction?":
    """
        SELECT AVG(approx_cost_for_two) as avg_cost_for_two, rate as ratings, pricing_segment
        FROM restaurants
        WHERE rate is NOT NULL
        GROUP BY ratings, pricing_segment
        ORDER BY ratings DESC
    """,
    "How do low, mid, and premium-priced restaurants perform in terms of ratings?":
    """
        SELECT
        pricing_segment,
        ROUND(AVG(rate), 2) AS avg_rating,
        COUNT(*) AS restaurant_count
        FROM restaurants
        WHERE rate IS NOT NULL
        GROUP BY pricing_segment
        ORDER BY avg_rating DESC;
    """,
    "Which cuisines are most common in Bangalore?":
    """
        SELECT
        cuisines,
        COUNT(*) AS restaurant_count
        FROM restaurants
        GROUP BY cuisines
        ORDER BY restaurant_count DESC
        LIMIT 10;
    """,
    "Which cuisines receive the highest average ratings?":
    """
        SELECT
        cuisines,
        ROUND(AVG(rate), 2) AS avg_rating,
        COUNT(*) AS restaurant_count
        FROM restaurants
        WHERE rate IS NOT NULL
        GROUP BY cuisines
        HAVING COUNT(*) >= 20
        ORDER BY avg_rating DESC
        LIMIT 10;
    """,
    "Which cuisines perform well despite having fewer restaurants?":
    """
        SELECT
        cuisines,
        COUNT(*) AS restaurant_count,
        ROUND(AVG(rate), 2) AS avg_rating
        FROM restaurants
        WHERE rate IS NOT NULL
        GROUP BY cuisines
        HAVING COUNT(*) BETWEEN 20 AND 100
        ORDER BY avg_rating DESC;
    """,
    "What is the relationship between restaurant cost and rating?":
    """
        SELECT
        pricing_segment,
        ROUND(AVG(rate), 2) AS avg_rating,
        ROUND(AVG(votes), 0) AS avg_votes,
        COUNT(*) AS restaurant_count
        FROM restaurants
        WHERE rate IS NOT NULL
        GROUP BY pricing_segment
        ORDER BY AVG(approx_cost_for_two);
    """
}