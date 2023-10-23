import os
import csv

count=0
list1=[]
list2=[]
election_data=[] 
Charles_vote = 0
Diana_vote=0
Raymon_vote = 0 
csv_path = 'C:/Users/krish/OneDrive/Desktop/Class_Activities/Challenge/Challenge_3/Starter_Code/PyPoll/Resources/election_data.csv'

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    election_data=list(csvreader)
    
    for row in election_data:
        list1.append(int(row[0]))
        list2.append(row[2])
        
    for row in list2:
        if  row == 'Charles Casper Stockham' :
            Charles_vote = Charles_vote +1 
        
        elif row == 'Diana DeGette':
            Diana_vote = Diana_vote + 1
        
        else : 
            Raymon_vote=Raymon_vote + 1
        
    count=len(list1)
    largest_vote = max(Charles_vote,Diana_vote,Raymon_vote)
    Avg_vote_Charles= (Charles_vote/count)*100
    Avg_vote_Diana = (Diana_vote/count)*100
    Avg_vote_Raymon= (Raymon_vote/count)*100
    
    
    if largest_vote== Charles_vote :
        winner = "Charles Casper Stockham"
    elif largest_vote== Diana_vote :
        winner= "Diana DeGette"
    else:
        winner="Raymon Anthony Doane"
    
    print("Election Results")
    print("----------------")
    print("Total Votes : ", count)
    print("------------------")
    print(f"Charles Casper Stockham: ({Avg_vote_Charles:.2f}%) {Charles_vote}")
    print(f"Diana DeGette: ({Avg_vote_Diana:.2f}%) {Diana_vote}")
    print(f"Raymon Anthony Doane: ({Avg_vote_Raymon:.2f}%) {Raymon_vote}")
    print("-----------------")
    print("Winner : ", winner  )
    print("-------------------")