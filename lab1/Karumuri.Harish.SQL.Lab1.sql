# Harish Karumuri Answers

#1.	Write a query to get Product name and quantity/unit.  
SELECT product_name, quantity_per_unit FROM northwind.products;

#2. Write a query to get current Product list (Product ID and name).  
SELECT id, product_name, discontinued 
FROM northwind.products
WHERE discontinued = 0;

#3. Write a query to get discontinued Product list (Product ID and name).  
SELECT id, product_name, discontinued 
FROM northwind.products
WHERE discontinued = 1;

#4. Write a query to get most expense and least expensive Product list (name and unit price).  
SELECT DISTINCT product_name, unit_price
FROM products
JOIN order_details ON products.id = order_details.product_id
WHERE order_details.unit_price = (SELECT max(unit_price) FROM order_details) OR order_details.unit_price = (SELECT min(unit_price) FROM order_details);

#5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.  
SELECT products.id, product_name, unit_price
FROM products
JOIN order_details ON products.id = order_details.product_id
WHERE order_details.unit_price < 20;

#6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
SELECT products.id, product_name, unit_price
FROM products
JOIN order_details ON products.id = order_details.product_id
WHERE order_details.unit_price BETWEEN 15 and 25;

#7. Write a query to get Product list (name, unit price) of above average price.  
SELECT DISTINCT product_name, unit_price
FROM products
JOIN order_details ON products.id = order_details.product_id
WHERE order_details.unit_price > (SELECT avg(unit_price) FROM order_details);

#8. Write a query to get Product list (name, unit price) of ten most expensive products.  
SELECT DISTINCT product_name, unit_price
FROM products
JOIN order_details ON products.id = order_details.product_id
ORDER BY unit_price DESC
LIMIT 10;

#9. Write a query to count current and discontinued products. 
SELECT COUNT(product_name)
FROM products;

#10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  

SELECT product_name, inventory_transactions.quantity as Inventory_Quant, order_details.quantity as Order_Quant
FROM products
JOIN order_details on products.id = order_details.product_id
JOIN inventory_transactions on products.id = inventory_transactions.product_id
WHERE inventory_transactions.quantity < order_details.quantity;



