# Week 8 Tutorial 8 - Food Delivery System

## Scenario

This project is a small backend receipt generator for a Food Delivery System.  
The system collects customer information, calculates the subtotal, service charge, delivery charge, and prints the final receipt.

## Files Used

### 1. main.py
This is the main application file.  
It imports functions from customer.py and receipt.py, then runs the program.

### 2. customer.py
This file contains the get_customer() function.  
It asks the user to enter the customer name, food ordered, quantity, price, and delivery option.

### 3. receipt.py
This file contains the print_receipt() function.  
It calculates the subtotal, service charge, delivery charge, and grand total.

## Formula Used

Subtotal = Quantity × Price

Service Charge = Subtotal × 5%

Grand Total = Subtotal + Service Charge + Delivery Charge

## Sample Input

Customer Name: izzad  
Food Ordered: Cake  
Quantity: 2  
Price per Item: 3.00  
Delivery: Y  

## Sample Output

Subtotal = RM 6.00  
Service Charge = RM 0.30  
Delivery Charge = RM 5.00  
Total = RM 11.30  

## How to Run

Open terminal inside the week_8 folder and run:

```bash
python main.py