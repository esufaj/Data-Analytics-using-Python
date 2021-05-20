import csv, sys
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt



# given a collection of users in a file filename.csv creates a file yelp-network.txt that represents the social network of Yelp friends. 
# The social network will be represented as a graph G(V,E), where Vis a set of vertices/nodes representing  the  Yelp users  
# and E is  a  set  of  links/edges  representing  friendships  between  Yelp  users.

#The  graph/network  should  be  represented  in  a  file using  the edge  list  format. 
# An  edge  list  is  a  list  that represents all the edges in a graph. 
# Each edge is represented as a pair of nodes occupying a new line in the  file.  
# For  example,  a  small fully  connected triangle-like  graph  between  nodes a1, a2, a3 would  be represented in the 
# yelp-network.txt file as:     a1 a2
#                               a2 a3
#                               a3 a1



def createNetwork():
    
    # G = nx.graph()

    with open("yelp_user.csv", "r") as users:
        data = csv.reader(users, delimiter=",")
        

        runNetwork = open('yelp-networkTest.txt', 'a')
    
        for row in data:
            if row[4] != 'None':
                
                friendSplit = row[4].split(",")
                
                for user in friendSplit:

                    runNetwork.write(row[0] + " " +  user + " \n")


    with open("yelp-networkTest.txt" , "r") as network:
        network = csv.reader(network , delimiter = ",")

        
        for row[0] in network:
           for row[1] in network:
               if row[0] == row[1]:
                   
                   del network
        
        new_file = open("yelp-network.txt", "w+")

        for line in network:
            runNetwork.write(row[0] + " " +  user + " \n")                    

          

            

            


                
        runNetwork.close()
        return             
                














def main():
    # checking if the number of args is correct and if the arguments are in the correct positions
    if len(sys.argv) != 2:
        print("\nERROR: Incorrect number of arguments\n")
        print("USAGE: <python3> <""yelp-network.py""> <""yelp-user.csv"">\n")
        sys.exit()
   
    if sys.argv[0] != 'yelp-network.py':
        print("\nERROR: arg[0] must be yelp-network.py")
        sys.exit()

    if sys.argv[1] != 'yelp_user.csv':
        print("\nERROR: argv[1] must be yelp_user.csv")
        sys.exit()

    csv.field_size_limit(sys.maxsize)

    createNetwork()

   


    


#calling main method for execution
main()