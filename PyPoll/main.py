# -------------------------------------------------------------------------------------------------------------------------------------------------------
# PyPoll Main Script - Results of Election Dataset
# -------------------------------------------------------------------------------------------------------------------------------------------------------


import os
import csv

electiondata_csv = os.path.join('..','PyPoll','Resources', 'election_data.csv')

def get_candidate_list(tuple_dataset):
    print("Get Candidate List")


def get_candidate_winner(list_candidate):
    print("Get Candidate Winner")


def print_election_results(tuple_dataset):
    
    total_votes = int(len(tuple_dataset))

    candidate_list = get_candidate_list(tuple_dataset)

    candidate_winner = get_candidate_winner(candidate_list)

    print(total_votes)


# Open the csv file in "read" mode ('r') and store the contents in the variable "csv_file"
with open(electiondata_csv, 'r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    dataset_tuple = list(tuple(row) for row in csv_reader)

    print_election_results(dataset_tuple)