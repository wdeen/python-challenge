# -------------------------------------------------------------------------------------------------------------------------------------------------------
# PyBank Main Script - Financial Analysis of Budget Dataset
# -------------------------------------------------------------------------------------------------------------------------------------------------------


import os       #Import OS Module for path manipulation of csv dataset file
import csv      #Import CSV Module to read csv dataset file

#join path components to establish file directory of csv dataset file
budgetdata_csv = os.path.join('..','PyBank','Resources', 'budget_data.csv')


#Function to return net total amount (int) of 'Profit/Losses' of entire dataset (requires csv dataset stored in nested list)
def get_total_amount(tuple_dataset):
    #Set new int variable to store total amount
    total = 0

    #For every row (list) until the final row (list) in the dataset (nested list)...
    #Add 'Profit/Losses' value from current row (list) to 'total' 
    for i in range(len(tuple_dataset)):
        total += int(tuple_dataset[i][1])

    return total

#Function to return a new nested list containing changes in 'Profit/Losses' of entire dataset (requires csv dataset stored in nested list)
def get_value_change_list(tuple_dataset):
    #Set new empty list to store lists where each contains month and corresponding changed value
    change_list = []

    #Set loop counter to '0'
    i = 0

    #While loop counter is less than or equal to length of nested list minus 2...
    #Subtraction of length required to end loop after second-last row (list); prevent from referencing row beyond the range
    while i <= (len(tuple_dataset) - 2):
        #In every loop, set new temporary list to store month and changed value
        temp_list = []
        
        #While on current row (list), store the month from the next to temporary list
        #Store the calculated difference of values between next row (list) and current to temporary list
        temp_list.append(str(tuple_dataset[i+1][0]))
        temp_list.append(int(tuple_dataset[i+1][1]) - int(tuple_dataset[i][1]))

        #Add temp list to main list
        change_list.append(temp_list)

        #iterate counter then repeat loop
        i+=1

    return change_list

#Function to return average (int) of all changed values (requires nested list of changed values)
def get_average_change(change_list):
    #Set int variable to store total of alll changed values
    change_total = 0

    #For every row (list) until the last in the dataset(nested list)...
    #Add changed value from current row (list) to total
    for i in range(len(change_list)):
        change_total += change_list[i][1]

    #Int variable to store calculated average (total of changed values / count of changed values from nested list)
    change_average = change_total / len(change_list)

    return change_average


#Function to return new list containing the greatest increase in profit i.e. highest change value (requires nested list of changed values)
def get_highest_change(change_list):
    #Counter to identify which row (list) in the dataset (nested list) has highest changed value
    #Set to '0' to start from the first in the nested list
    j = 0

    #For every row (list) until the last in the dataset(nested list)...
    #If value from current row is greater than the value from row 'j'...
    #Set counter to index of current row in nested list. 
    for i in range (len(change_list)):
        if (change_list[i][1] > change_list[j][1]):
            j = i

    #New list to store row (list) containing the highest changed value and corresponding month
    change_highest = change_list[j]

    return change_highest

#Function to return new list containing the greatest decrease in profit i.e. lowest change value (requires nested list of changed values)
def get_lowest_change(change_list):
    #Counter to identify which row (list) in the dataset (nested list) has lowest changed value
    #Set to '0' to start from the first in the nested list
    j = 0

    #For every row (list) until the last in the dataset(nested list)...
    #If value from current row is less than the value from row 'j'...
    #Set counter to index of current row in nested list. 
    for i in range (len(change_list)):
        if (change_list[i][1] < change_list[j][1]):
            j = i

    #New list to store row (list) containing the lowest changed value and corresponding month
    change_lowest = change_list[j]

    return change_lowest


#Function to print Financial Analysis of budget dataset (requires csv dataset stored in nested list)
def print_financial_analysis (tuple_dataset):
    #length of nested list; every list in nested list can be visualised as a row
    total_months = int(len(tuple_dataset))

    #Store result of function which returns total net amount of 'Profit/Losses' in entire budget dataset
    total_amount = get_total_amount(tuple_dataset)
    
    #Store result of function which returns nested list of changed 'Profit/Losses' in entire budget dataset; each list has the changed value and corresponding month
    list_change = get_value_change_list(tuple_dataset)

    #Using the nested list of changed values, store result of function which returns average of all changed values
    average_change = get_average_change(list_change)

    #Using the nested list of changed values, store result of function which returns greatest profit increase value
    highest_change = get_highest_change(list_change)

    #Using the nested list of changed values, store result of function which returns greatest profit decrease value
    lowest_change = get_lowest_change(list_change)
    

    #Print to Terminal: Financial Analysis with the calculated results from above
    print("-------------------------------------------------------", end='\n')
    print("Financial Analysis", end='\n')
    print("-------------------------------------------------------", end='\n')
    print("Total Months: ", total_months, end='\n')
    print("Total Amount: $", total_amount, end='\n')
    print("Average Change: $", round(average_change,2), end='\n') #Round average changed value to 2 decimal places
    print("Greatest Increase in Profits: ", highest_change[0], " ( $", highest_change[1], ")", end='\n')
    print("Greatest Decrease in Profits: ", lowest_change[0], " ( $", lowest_change[1], ")", end='\n')
    print("-------------------------------------------------------", end='\n')
    print("Module 3 Challenge (Python) - Wassim Deen", end='\n')
    print("-------------------------------------------------------", end='\n')


    #Use Open() module to create a new text file and store in the analysis sub-folder within 'PyBank' main folder
    #Write the analyis results to the text file
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

    #After analysis results are written, close the file
    txtfile.close()

    #Inform user the text file is created and stored
    print("\n******Saved to Text File (analysis/financial_analysis.txt)******")


# Where the code starts after importing Modules...
# Open the csv file in "read" mode ('r') and store the contents in variable "csv_file"
with open(budgetdata_csv, 'r') as csv_file:

    #Variable to read the data from the csv file
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Store first row from the csv file into variable and jump to the next row
    #Header not required for calculating financial analysis results
    csv_header = next(csv_reader)

    #From the 2nd row, store every row from the csv dataset as a tuple
    #List of tuples where each tuple contains the month and its corresponding 'Profit/Losses' value e.g. [Month1, Value1]
    #To be used only to reference from for calculating financial analysis results; not required to add more members after this point
    dataset_tuple = list(tuple(row) for row in csv_reader)

    #Using the List of Tuples, run the function to generate financial analysis results
    print_financial_analysis(dataset_tuple)