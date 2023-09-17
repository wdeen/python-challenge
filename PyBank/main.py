# -------------------------------------------------------------------------------------------------------------------------------------------------------
# PyBank Main Script - Financial Analysis of Budget Dataset
# -------------------------------------------------------------------------------------------------------------------------------------------------------


import os
import csv

budgetdata_csv = os.path.join('..','PyBank','Resources', 'budget_data.csv')


def get_total_amount(tuple_dataset):
    total = 0

    for i in range(len(tuple_dataset)):
        total += int(tuple_dataset[i][1])

    return total


def get_value_change_list(tuple_dataset):
    change_list = []

    i = 0

    while i <= (len(tuple_dataset) - 2):
        temp_list = []
        
        temp_list.append(str(tuple_dataset[i+1][0]))
        temp_list.append(int(tuple_dataset[i+1][1]) - int(tuple_dataset[i][1]))

        change_list.append(temp_list)

        i+=1

    return change_list


def get_average_change(change_list):
    change_total = 0

    for i in range(len(change_list)):
        change_total += change_list[i][1]

    change_average = change_total / len(change_list)

    return change_average


def get_highest_change(change_list):
    j = 0

    for i in range (len(change_list)):
        if (change_list[i][1] > change_list[j][1]):
            j = i

    change_highest = change_list[j]

    return change_highest


def get_lowest_change(change_list):
    j = 0

    for i in range (len(change_list)):
        if (change_list[i][1] < change_list[j][1]):
            j = i

    change_lowest = change_list[j]

    return change_lowest


def print_financial_analysis (tuple_dataset):
    
    total_months = int(len(tuple_dataset))

    total_amount = get_total_amount(tuple_dataset)
    
    list_change = get_value_change_list(tuple_dataset)

    average_change = get_average_change(list_change)

    highest_change = get_highest_change(list_change)

    lowest_change = get_lowest_change(list_change)
    

    print("-------------------------------------------------------", end='\n')
    print("Financial Analysis", end='\n')
    print("-------------------------------------------------------", end='\n')
    print("Total Months: ", total_months, end='\n')
    print("Total Amount: $", total_amount, end='\n')
    print("Average Change: $", round(average_change,2), end='\n')
    print("Greatest Increase in Profits: ", highest_change[0], " ( $", highest_change[1], ")", end='\n')
    print("Greatest Decrease in Profits: ", lowest_change[0], " ( $", lowest_change[1], ")", end='\n')
    print("-------------------------------------------------------", end='\n')
    print("Module 3 Challenge (Python) - Wassim Deen", end='\n')
    print("-------------------------------------------------------", end='\n')


    with open('analysis/financial_analysis.txt', 'w') as txtfile:
        txtfile.write("------------------------------------------------------- \n" +
                      "Financial Analysis \n" +
                      "------------------------------------------------------- \n" +
                      "Total Months: " + str(total_months) + "\n" +
                      "Total Amount: $" + str(total_amount) + "\n" +
                      "Average Change: $" + str(round(average_change,2)) + "\n" +
                      "Greatest Increase in Profits: " + highest_change[0] + " ( $" + str(highest_change[1]) + " )" + "\n" +
                      "Greatest Decrease in Profits: " + lowest_change[0] + " ( $" + str(lowest_change[1]) + " )" + "\n" +
                      "------------------------------------------------------- \n" +
                      "Module 3 Challenge (Python) - Wassim Deen \n" +
                      "------------------------------------------------------- \n"
        )

    print("******Saved to Text File (analysis/financial_analysis.txt)******")

# Open the csv file in "read" mode ('r') and store the contents in the variable "csv_file"
with open(budgetdata_csv, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    dataset_tuple = list(tuple(row) for row in csv_reader)

    print_financial_analysis(dataset_tuple)