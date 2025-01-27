# Super_Market_Billing_System--Python
A Python-based supermarket billing system that allows customers to add items to a cart, view a menu with prices, and generate a detailed receipt. 
# Project Overview
The Supermarket Billing System is a Python-based application designed to streamline the billing process in a supermarket. It processes multiple items, calculates total prices, applies discounts based on predefined conditions, and generates an itemized receipt for the customer. This interactive system is built to ensure accurate and efficient billing.
# Features
<br>
-Multiple Item Processing: Allows users to input multiple items with quantities in a single transaction.
<br>
-Discount Application: Automatically applies discounts based on the total amount:
<br>
5% for totals up to ₹500
<br>  
7% for totals up to ₹1000
<br>
15% for totals up to ₹5000
<br>
20% for totals above ₹5000
<br>
-Itemized Receipt: Provides a detailed receipt showing each item, price, quantity, subtotal, discount, and final total.
<br>
-Customer Details: Captures and displays customer name and phone number for each transaction.
<br>
-Continuous Input: Processes multiple transactions for consecutive customers in a single run.

# How It Works
<br>
1. Customer Information:
<br>
The system prompts for the customer's name and phone number.
<br>
2. Item Selection:
<br>
A list of available products and prices is displayed.
Customers enter the item name and quantity. The system calculates the subtotal and adds the item to the cart.
<br>
3. Discount Calculation:
<br>
The system applies discounts based on the total bill amount:
<br>
-5% discount for totals up to ₹500
<br>
-7% discount for totals up to ₹1000
<br>
-15% discount for totals up to ₹5000
<br>
-20% discount for totals above ₹5000
<br>
4. Receipt Generation:
<br>
An itemized receipt is generated, displaying:
-Store information, date, and time
<br>
-Customer name and phone number
<br>
-Itemized details (name, price, quantity)
<br>
-Total bill, discount applied, and the final bill after the discount
<br>
5. Multiple Transactions:
<br>
The program can handle consecutive customers in a single run, asking after each receipt whether there is another customer in the queue.

# Technologies Used
Python 3.x for the core logic and implementation.
<br>
Datetime Module for generating the current date and time on receipts.
