USE northwind_dw;

SELECT last_name, SUM(quantity) as total_quantity, SUM(unit_price) as total_unit_price
FROM fact_orders
JOIN dim_customers on fact_orders.customer_id = `dim_customers`.`customer_key`
GROUP BY last_name;