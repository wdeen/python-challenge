# -------------------------------------------------------------------------------------------------------------------------------------------------------
# PyPoll Main Script - Results of Election Dataset
# -------------------------------------------------------------------------------------------------------------------------------------------------------


import os       #Import OS Module for path manipulation of csv dataset file
import csv      #Import CSV Module to read csv dataset file

#join path components to establish file directory of csv dataset file
electiondata_csv = os.path.join('..','PyPoll','Resources', 'election_data.csv')

#Function to return new nested list where each list contains the candidate and their own total votes (requires csv dataset stored in nested list)
def get_candidate_list(tuple_dataset):
    #Set empty list to store lists of every candidate with their total votes
    candidate_list = []

    #Set loop counter to '0'
    i = 0

    #While loop counter is less than or equal to length of nested list minus 1...
    #Subtraction of length required to end loop after last row (list); prevent from referencing row beyond the range
    while i <= (len(tuple_dataset) - 1):
        #In a new loop, take candidate name from current row as reference
        candidate = tuple_dataset[i][2]

        #If candidate name from 'candidate' exists in the final 'candidate_list'...
        #Then for every row (list) in that list, find the list containing the candidate name...
        #If on that list, add 1 'vote' to that list
        if any(candidate in j for j in candidate_list):
            for v in range(len(candidate_list)):
                if(candidate_list[v][0] == candidate):
                    candidate_list[v][1] += 1

        #If candidate name from 'candidate' does NOT exist in final 'candidate_list'...
        #Create new temporary list containing that candidate name and 1 vote (e.g. [Wassim Deen, 1]) and add that list to nested list ('candidate_list')
        else:
            temp_list = []
            
            temp_list.append(candidate)
            temp_list.append(1)

            candidate_list.append(temp_list)

        #iterate counter then repeat loop            
        i+=1

    
    return candidate_list


#Function to return amended candidate list where each list of candidate also contains their percentage of votes (requires initial candidate list and total no. votes)
def get_candidate_percentage(candidate_list, votes_total):
    #For every list in the nested list...
    #Divide their votes over the total number of votes, then add that result to that list
    for i in range(len(candidate_list)):
        candidate_percent = candidate_list[i][1] / votes_total

        candidate_list[i].append(candidate_percent)


    return candidate_list

#Function to return the candidate winner's name (requires candidate list)
def get_candidate_winner(candidate_list):
    #Counter to identify which list in the nested list has the highest number of votes
    #Set to '0' to start from the first in the nested list
    j = 0

    #For every list until the last in the nested list...
    #If number of votes from current list is greater than the value from list 'j'...
    #Set counter to index of current list in nested list. 
    for i in range (len(candidate_list)):
        if (candidate_list[i][1] > candidate_list[j][1]):
            j = i

    #New string variable to store the name of the candidate winner
    candidate_winner = candidate_list[j][0]

    return candidate_winner


#Function to print Election Results of election dataset (requires csv dataset stored in nested list)
def print_election_results(tuple_dataset):
    
    #length of nested list; every list in nested list can be visualised as a row, and each row = 1 vote
    total_votes = int(len(tuple_dataset))

    #Store result of function which returns a nested list where each list contains candidate name as their corresponding number of votes collected
    list_candidate = get_candidate_list(tuple_dataset)

    #Store result of function which returns an amended nested list where each list of candidate now also contains their percentage of votes
    list_candidate = get_candidate_percentage(list_candidate, total_votes)

    #Store result of function which returns the name of the candidate winner (candidate w/ highest number of votes)
    winner_candidate = get_candidate_winner(list_candidate)

    #Print to Terminal: Election Results using the results generated and collected from above
    print(f"-------------------------------------------------------")
    print(f"Election Results")
    print(f"-------------------------------------------------------\n")
    print(f"Total Votes: {total_votes} \n")
    print(f"-------------------------------------------------------\n")

    #For every list in the candidate list, print the candidate's name, percentage of votes (% Format to 3 d.p.) and collected number of votes
    for i in range(len(list_candidate)):
        print(f"{list_candidate[i][0]}: {list_candidate[i][2]:.3%} ({list_candidate[i][1]} Votes) \n")

    #Print to Terminal: Print Remaining Results
    print(f"-------------------------------------------------------\n")
    print(f"Winner: {winner_candidate}\n")
    print(f"-------------------------------------------------------")
    print(f"Module 3 Challenge (Python) - Wassim Deen")
    print(f"-------------------------------------------------------")


    #Use Open() module to create a new text file and store in the analysis sub-folder within 'PyPoll' main folder
    #Write the analyis results to the text file
    with open('analysis/election_results.txt', 'w') as txtfile:
        txtfile.write("------------------------------------------------------- \n" +
                      "Election Results \n" +
                      "------------------------------------------------------- \n" + "\n" +
                      "Total Votes: " + str(total_votes) + "\n" + "\n" + 
                      "------------------------------------------------------- \n" + "\n")
        
        #For every list in the candidate list, write the candidate's name, percentage of votes (% Format to 3 d.p.) and collected number of votes to the text file
        for i in range(len(list_candidate)):
            txtfile.write(str(list_candidate[i][0]) + ": " + str(round((list_candidate[i][2] * 100), 3)) + "%" + " (" + str(list_candidate[i][1]) + " Votes) \n" + "\n")

        #Write Remaining Results to text file 
        txtfile.write("------------------------------------------------------- \n" + "\n" +
                      "Winner: " + str(winner_candidate) + "\n" + "\n"
                      "------------------------------------------------------- \n" +
                      "Module 3 Challenge (Python) - Wassim Deen \n" +
                      "-------------------------------------------------------")
    
    #After analysis results are written, close the file
    txtfile.close()

    #Inform user the text file is created and stored   
    print("\n******Saved to Text File (analysis/election_results.txt)******")


# Where the code starts after importing Modules...
# Open the csv file in "read" mode ('r') and store the contents in variable "csv_file"
with open(electiondata_csv, 'r') as csv_file:

    #Variable to read the data from the csv file
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Store first row from the csv file into variable and jump to the next row
    #Header not required for calculating election results
    csv_header = next(csv_reader)

    #From the 2nd row, store every row from the csv dataset as a tuple
    #List of tuples where each tuple contains Ballot ID/County/Candidate Name e.g. [BallotID1, County1, CandidateName1]
    #To be used only to reference from for calculating election results; not required to add more members after this point
    dataset_tuple = list(tuple(row) for row in csv_reader)

    #Using the List of Tuples, run the function to generate election results
    print_election_results(dataset_tuple)