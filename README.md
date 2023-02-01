# About Script 
It is a Python script that calculates payer's individual remaining points after spending a given target amount using the below rules - 

* We want the oldest points to be spent first (oldest based on transaction timestamp, not the order they’re received)
* We want no payer's points to go negative

## Components of the project
The project consists of following files - 

* transactions.csv - a csv file with the information payers, points and timestamp for each entry
* program.py - this is the main code that computes remaining points per payer after spending a target points
* requirements.txt - file with all the packages and dependencies 

## Executing the script 
```
pip3 install -r requirements.txt
python3 program.py <spend_points>

```

- first command installs are the packages and dependencies if any in this project
- second command runs the python script with a spend_points (target amount) argument. 
<spend_points> is a commandline argument and can be passed when running the python script from the terminal. 


## Code walkthrough 

Code is divided into three parts - 
1. the main function - it takes in the commandline argument, creats a nested list of all the transactions from the csv and runs the amount_spend function to output desired result. 
2. reading_transactions function - it takes in the transactions.csv file's path, checks if the file exists. Next it skips the header line in the file and performs validation on the payer's name and points. If the payer's name and points are in the proper format, it stores each transaction in a nested list and return it. 
3. amount_spend function - it takes in the nested transactions list and spend_points as input. It sorts the nested list on the timestamp field in the ascending order then performs following checks as -

* Case1: if spend_points is greater than total points of all the payers, it returns points as 0 for all the payers if each payer initially had a positive total points else returns points as per the calculation of spending the target points.
* Case2: if spend_points is negative, returns all the payers points as it is. 
* Case3: it checks if spend_points is equal to zero, returns all the payers points as it is.
* Case4: Computes points spend from each transaction from the nested transactions list, updates the payer's points and returns the final payer details. 

## Assumptions and Alternates 

I have added the assumptions and alternates in the codebase as a comment before each check and added a print statement to state my code's assumption and hence, the ouput result. 

