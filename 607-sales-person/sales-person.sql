# Write your MySQL query statement below
# Find all salespersons who did NOT have any orders related to the company "RED"
# First, find the com_id from Company that corresponds to "RED"
# Then, find all the order_ids from Orders that do NOT have com_id "RED"

# OR, find all the order_ids from Orders that DO have com_id "RED"
# Find all associated salespersons from Orders
# Select every salesperson NOT from this group

SELECT DISTINCT name FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT sales_id 
    FROM Orders 
    WHERE com_id = (
        SELECT DISTINCT com_id
        FROM Company
        WHERE name = "RED"
    ));