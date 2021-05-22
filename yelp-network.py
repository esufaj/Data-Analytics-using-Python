import csv, sys


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
   #dict to hold user_id and friends
    users = {}

    #opening file which we will write to
    output = open('yelp-network.txt', 'w')

    #reading from yelp file
    with open('yelp_user.csv', 'r') as net:
        netList = csv.reader(net, delimiter=',')

        #looping through yelp data
        for col in netList:
           
            #ignoring rows with an empty friends list
            if col[4] != 'None':
               
                #splitting yelp data
                friendsSplit = col[4].split(', ')
                
                #checking if user_id (key) is in the dict, if its not, we will add it and a place holder value
                if col[0] not in users.keys():
                     users[col[0]] = 'placeHolder'
                
                #looping through the friends list and checking whether the friend is in dict or not
                #if friend is not in dict list then we have not seen it yet and is not a repeat so we will print its key and the friend seen
                for friend in friendsSplit:

                    if friend not in users.keys():
                        output.write(col[0] + "  " + friend + "\n")
                    
                    #friend was seen in dict list and hence we do not want to print as to not create dupes so we do nothing
                    else:
                        continue

    #closing the output file            
    output.close()



    return " "  


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

    #csv file limit had to be raised since the file we are dealing with is larger then the allowed csv limit
    csv.field_size_limit(sys.maxsize)

    #calling the method for execution
    createNetwork()

#calling main method for execution
main()



# -------------------------------previous attempts at trying to make this code work until we finally got it -------------------------------





# def createNetwork():

#     output = open('yelp-networkTest.txt', 'w')

#     with open('yelp_user.csv', 'r', encoding='utf8') as eli:
#         file = csv.reader(eli, delimiter=',')

#         users = []
#         for col in file:
#             if col[4] != 'None':

#                 friends = col[4].split(', ')

#                 for friend in friends:

#                     if friend not in users:
#                         users.append(col[0])
#                         output.write(col[0] + "  " + friend + "\n")
#                     else:
#                         continue

#     output.close()

#     return ""


#def createNetwork():
    


#     with open("yelp_user.csv", 'r') as net:
#         data = csv.reader(net, delimiter=",")

#         seen = []
#        # friends = []
#         file = open("yelp-networkTest.txt", "w")
        
#         for row in data:
            
#             if row[4] != 'None':
#                 friendSplit = row[4].split(", ")

#                 # if row[0] not in seen:
#                     # seen.append(row[0])

#                     #friendSplit = row[4].split(",")
#                 for friend in friendSplit:

#                     if friend not in seen:
#                         file.write(row[0] + " " + friend + "\n")
                
#             seen.append(row[0])

#         file.close()

    # friends_list = []
    
    # with open("yelp_user.csv", 'r', encoding='utf8') as business:
    #     yelp_data = csv.reader(business, delimiter=",")


    #     for row in yelp_data:
    #         if row[4] != 'None':
    #             # Split friends
    #             spliting_friends = row[4].split(",")

    # #             if row[0] not in G.nodes():
    # #                 G.add_node(row[0])

    #             for friend in spliting_friends:
    #                 friends_list.append((row[0], friend))

    # print("Fuck Marc")
    # data = {tuple(item) for item in map(sorted, friends_list)}
    # social_network = open('yelp-network.txt_5', 'w')
    # for node in data:
    #     social_network.write(node[0] + ' ' + node[1] + "\n") 
    # social_network.close()
    
    # G = nx.Graph()

    # with open("yelp_user.csv", "r") as users:
    #     data = csv.reader(users, delimiter=",")
    #     network = open("yelp-networkTEST7.txt", "a")   

    #     for row in data:
           
    #         if row[4] != 'None':
    #             friendSplit = row[4].split(", ")


    #             # if row[0] not in G.nodes():
    #                 # G.add_node(row[0])

                    
    #             for friend in friendSplit:

    #                 if friend not in G.nodes():
    #                      #G.add_node(friend)
    #                     G.add_edge(row[0],friend)
    #                 else:
    #                     continue


    #             G.add_node(row[0])
            

    # for edge in G.edges():
    #     network.write(edge[0] + " " + edge[1] + "\n")

    # network.close()

    # graph = nx.Graph()

    # with open("yelp_user.csv", 'r', encoding='utf8') as business:
    #     yelp_data = csv.reader(business, delimiter=",")
    
        
    #     social_network = open('yelp-networkTEST.txt', 'w')


    #     for row in yelp_data:
            
    #         if row[4] != 'None':
    #             spliting_friends = row[4].split(", ") #for friend in spliting_friends:
                
    #             for friend in spliting_friends:
    #                 if not graph.has_edge(friend, row[0]):
    #                     graph.add_edge(row[0], friend)
    #                 else:
    #                     continue

        # runNetwork = open('yelp-network.txt', 'a')
    
        # for row in data:
        #     if row[4] != 'None':
                
        #         friendSplit = row[4].split(",")
                
        #         for user in friendSplit:

        #             runNetwork.write(row[0] + " " +  user + " \n")


    # with open("yelp-networkTest.txt" , "r") as network:
    #     network = csv.reader(network , delimiter = ",")

        
    #     for row[0] in network:
    #        for row[1] in network:
    #            if row[0]:
                   
    #                del network


        # df = pd.read_csv("yelp-network.txt", sep=",")

        # df.head(n=3)

        # print(df)
    
        # df.drop_duplicates(keep=False, inplace=True)
        # # df = df[df.columns[1] != None]
        # df.to_csv('yelpppp.txt')
        
        # runNetwork.write(df[0] + " " +  df[1] + " \n")        

# def createNetwork():

#     output = open('yelp-networkTestHoly.txt', 'w')

#     with open('yelp_user.csv', 'r', encoding='utf8') as eli:
#         file = csv.reader(eli, delimiter=',')

#         users = []
#         for col in file:
#             if col[4] != 'None':

#                 friends = col[4].split(', ')

#                 if col[0] not in users:
#                      users.append(col[0])

#                 for friend in friends:

#                     if friend not in users:
#                         output.write(col[0] + "  " + friend + "\n")
#                     else:
#                         continue
                
#     output.close()

#     return ""