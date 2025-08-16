-- ================================
-- Task 6: Sales Trend Analysis Using Aggregations
-- ================================

-- Step 1: Create the table
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    product_id INT
);

-- Step 2: Insert sample data
INSERT INTO orders (order_id, order_date, amount, product_id) VALUES
(1, '2024-01-15', 500.00, 101),
(2, '2024-01-20', 300.00, 102),
(3, '2024-02-05', 800.00, 103),
(4, '2024-02-18', 200.00, 104),
(5, '2024-02-25', 700.00, 101),
(6, '2024-03-02', 450.00, 105),
(7, '2024-03-15', 600.00, 106),
(8, '2024-03-22', 350.00, 107),
(9, '2024-04-01', 900.00, 108),
(10, '2024-04-10', 400.00, 109),
(11, '2024-04-18', 300.00, 110),
(12, '2024-05-05', 750.00, 111),
(13, '2024-05-15', 200.00, 112),
(14, '2024-05-22', 650.00, 113);

-- ================================
-- Step 3: Monthly Revenue and Order Volume
-- ================================
-- This query shows total revenue and number of unique orders per month

SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT order_id) AS order_volume
FROM orders
GROUP BY year, month
ORDER BY year, month;

-- ================================
-- Step 4: Top 3 Months by Sales
-- ================================
-- This query gives the top 3 months with the highest revenue

SELECT 
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY year, month
ORDER BY total_revenue DESC
LIMIT 3;
