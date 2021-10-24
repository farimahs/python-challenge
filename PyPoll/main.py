import os
import csv
from collections import Counter

# Set path for file and open/read csv file
csv_path = os.path.join ('Resources', 'election_data.csv')

ID =[]
candid =[]
unique_candid_list =[]
Votes =[]

with open (csv_path) as csv_file:
    csv_reader = csv.reader (csv_file, delimiter =',')

    for row in csv_reader:
        ID.append(row[0])
        candid.append(row[2])

# Removing column headers from the lists
    ID.pop(0)
    candid.pop(0)
    
# Getting the unique candidate names
    for name in candid:
        if name not in unique_candid_list:
            unique_candid_list.append(name)

# Counting votes for each candidate using Counter
    counter_dict = Counter(candid)
    percent_dict = {}
    total_votes = int(len(ID))
    for name in unique_candid_list:
        percent = (int(counter_dict[name])/total_votes)*100
        percent_round = str(round(percent, 3))
        percent_dict[name] = percent_round

# Winner of the election
    winner = max(counter_dict, key=counter_dict.get)

        
    print("Election Results" + "\n")
    print("-" *25 + "\n")
    print (f" Total Votes: {len(ID)} \n")
    print("-" *25 + "\n") 

    for name in unique_candid_list:
        print(f"{name}: {percent_dict[name]}% ({counter_dict[name]}) \n")
    print("-" *25 + "\n")
    print(f"Winner: {winner}")
    print("-" *25 + "\n")


# Exporting the results into a text file
    election_results = open ('election_results.txt', 'w')

    election_results.write("Election Results" + "\n")
    election_results.write("-" *25 + "\n")
    election_results.write(f" Total Votes: {len(ID)} \n")
    election_results.write("-" *25 + "\n")
    for name in unique_candid_list:
        election_results.write(f"{name}: {percent_dict[name]}% ({counter_dict[name]}) \n")
    election_results.write("-" *25 + "\n")
    election_results.write(f"Winner: {winner} \n")
    election_results.write("-" *25 + "\n")

    election_results.close()