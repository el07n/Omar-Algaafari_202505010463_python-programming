# Analytical Thinking and Boolean Logic
# Movie Theater Entry Checker
##**Activity 1: Identify the Components**
### What are the Inputs?
**Answer:**
- Age
- With Adult
- His ticket

## What are the Process?
**Answer:**
- Check if age >= 13 OR with adult
- Check if has ticket
- Decide entry allowed or not

### What is the output ?
**Answer:**
- Entry Allowed
- Entry Not Allowed

## **Activity 2: Design the Algorithm
### The Flow
Drag the created diagram image while holding the "Shift" key

![alt text](<WhatsApp Image 2026-06-10 at 12.12.37 PM dai.jpeg>)

### The Truth Table
**Answer:**

| Age >= 13 | With Adult | Has Ticket | Entry Allowed |
|---|---|---|---|
| True | True | True |  True |
| True | False | True | True |
| False | True | True | True |
| False | False | True | False |
| True  | True  | False | False |
| False | True  | False | False |
| False | False | False | False |

### Algorithm (The Step-by-Step Solution)
*Answer:*
 
1. Start
2. Input age
3. Input with adult
4. Input ticket status
5. Evaluate conditions
6. Display result
7. End
### Pseudocode
```
START
INPUT age
INPUT withAdult
INPUT hasTicket

IF ((age >= 13 OR withAdult) AND hasTicket) THEN
    DISPLAY "Entry Allowed"
ELSE
    DISPLAY "Entry Not Allowed"
END 
```