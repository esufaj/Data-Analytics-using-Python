import csv, sys
import time

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

#for measuring execution time
#start_time = time.time()

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

    #for measuring execution time
    # print("--- %s seconds ---" % (time.time() - start_time))

#calling main method for execution
main()