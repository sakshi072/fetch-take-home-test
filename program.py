import csv 
import sys 
import os.path

# function to evaluate all payers points used in the spend amount starting from the oldest transaction as per the timestamp.
def amount_spend(spend_points, transactions):
    
    # sorting transactions nested list on ascending order of timestamp.
    transactions = sorted(transactions, key=lambda x: x[2], reverse=False)

    # dictionary of payers with total points in all the transactions combined. 
    payers_details = {}
    
    # looping on all the transactions to get total points of each payer. 
    for payer_name, points, timestamp in transactions:
        if payer_name not in payers_details:
            payers_details[payer_name] = 0
        payers_details[payer_name] += points
    
    # Check-1: if the combined points of all the payers is less than the spend points, the requirement cannot be met. 
    if sum(payers_details.values()) < spend_points:
        # Alternate for spend_points more than payer's points is to add all the negative points of any payer to spend.
        # make all the points as 0.
        # print("The remaining spend amount =", spend_points - sum(payers_details.values()))
        # payers_details = {payer_name: 0 for payer_name in payers_details}
        
        print("Spending amount is not feasible as all the payers in total have less points than spend amount.")
        
        # if points of all the payers is greater than 0, it will reduce the spend points by some amount.
        # all the payers' points will become zero.
        if all(value >= 0 for value in payers_details.values()):
            print("The remaining spend amount =", spend_points - sum(payers_details.values()))
            payers_details = {payer_name: 0 for payer_name in payers_details}
        
        # if some payers have negative points, skipping them to avoid increasing the spend points
        # only spending points of payers with positiove points.
        else:
            for payer_name, points in payers_details.items():
                if points > 0:
                    spend_points -= points
                    payers_details[payer_name] -= points
            print("The remaining spend amount = ", spend_points)

        return payers_details
    
    # Check-2: if spend points is negative, all the payers points remain intact and this transaction is not feasible. 
    if spend_points < 0:
        # Alternate for negative spend_points is to add the entire spend_points amount to the latest entry.
        # payers_details[transactions[-1][0]] += spend_points
        # return payers_details

        print("The spend amount is negative so none of the payers will lose any points")
        return payers_details
    
    # Check-3: if any payer has a negative total points.
    # Currently, negative payer points are added to the spend points according to the transaction that is processed. 

    # Spending points from each payer according to the sorted transactions list of payers.
    for payer_name, points, timestamp in transactions:
        # if spend points is zero, return all the payers details as is 
        if spend_points == 0:
            break
        elif points >= spend_points:
            payers_details[payer_name] -= spend_points
            break
        else:
            spend_points -= points
            payers_details[payer_name] -= points

    return payers_details

# Reading and parding the csv file and validating the file and its contents.
def reading_transactions(path_file):
    # Checking if the transactions csv file exists on the system.
    if not os.path.exists(path_file):
        print("transaction csv does not exists")
        return []
    
    transaction_list = []
    # Opening the csv file in the read mode.
    with open(path_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Validating if the csv file is not empty.
        if not csv:
            print("empty transaction csv")
            return []

        # Skipping the header line in the csv file. 
        next(csv_reader)

        for line in csv_reader:
            # check for any empty line in between or towards the end of csv.
            if not line:
                continue
            
            payer, points, timestamp = line

            # Validating if payer name string is not empty.
            if not payer:
                print("invalid payer name")
                continue
            # Validating if points are integers and not any garbage value.
            if not int(points):
                print("invalid points of a payer")
                continue

            # Transaction_list is the nested list of all the transactions.
            transaction_list.append((payer, int(points), timestamp))
        
    return transaction_list

# Main function to execute the python script 
if __name__ == '__main__':

    # Taking command-line arguemnt for the spend amount to implement the entire functionality. 
    spend_points = int(sys.argv[1])
    transactions = reading_transactions('transactions.csv')

    # Checking if the transactions csv file has atleast one set of transaction.
    if transactions:
        payers_details = amount_spend(spend_points, transactions)
        print(payers_details)
    else:
        print("Error: No transaction to process")

