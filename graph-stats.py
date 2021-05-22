import csv, sys


#a  frequency  distribution  of  the  node  degrees  of  the  network,  in  a descending order of frequency 
# (from the highest to the lowest frequency). The degree of a node is  the  number  of  edges  that  are  incident  to  the node  
# (i.e.,  #neighbors).  The  output  should  be one line per pair of values as follows: 
# nodeID:nodeDegreefor example:JJ-aSuM4pCFPdkfoZ34q0Q:14pzpbr9mlagHhDRdin8DvPQ:12

def nodeDegreeDist():

    # Nodes and Edges Dict
    networkDict = {}

    #opening txt file from partC
    with open('yelp-network.txt', 'r') as friends:
        yelp_data  = csv.reader(friends, delimiter=',')

        #looping through data
        for col in yelp_data:

            # ignoring the first line which is split in the middle by 2 spaces
            if (col[0] != 'user_id  friends'):

                # Split friends by 2 spaces not 1 as in file
                nodesSplit = col[0].split('  ')

                # if node user_id (key) is not in dict then we add it and assign its degree count (value) to 1 since it has only now been seen
                if nodesSplit[0] not in networkDict.keys():
                    networkDict[nodesSplit[0]] = 1

                #key was found in dict, so we just increase its degree count
                else:
                    networkDict[nodesSplit[0]] += 1

                #if node friends is not in dict then we add it and assign its degree count (value) to 1 since it has only now been seen
                if nodesSplit[1] not in networkDict.keys():
                    networkDict[nodesSplit[1]] = 1

                #key was found in dict, so we just increase its degree count
                else:
                    networkDict[nodesSplit[1]] += 1
                    
    #the number of nodes is = to the number of keys in the dictionary
    number_of_nodes = len(networkDict.keys())

    #edges have not been created yet
    number_of_edges = 0
    
    #looping through dict
    for node in networkDict.keys():

        #num of edges is = to the num of degrees the value part of the dict holds
        number_of_edges += networkDict[node]

    #degTotal holds num of edges so we can use it for calculations in avgNodeDegree method
    degTotal = int(number_of_edges)

    #has to divide by 2 since we are adding edge twice considering if A has B as friend then B has A as friend (bidirectional)
    number_of_edges = int(number_of_edges / 2)

    #creating space in term
    print("\n")

    #printing stats in necessary format
    print("#nodes: " + str(number_of_nodes) + "  edges: " + str(number_of_edges))

    #calling method which will output stats to file
    nodeDegree(networkDict)

    #printing the average node degree by passing the total number of nodes and the total degrees for all of the nodes
    print(avgNodeDegree(number_of_nodes, degTotal))



#method that takes a dictionary, sorts it in decreasing order and writes to file the user_id(node): # of incident edges to the node (user_id)
def nodeDegree(networkDict):

    #opening file to write outout too. Needed to write to file since outputting in terminal took > 10-15 minutes
    #writing to file took much less time approx. 2-4 min maybe less
    output = open("nodeDegreeDist.txt", 'w')

    #sorting dict items in decreasing order
    for key, value in sorted(networkDict.items(), key=lambda item: item[1], reverse=True):

        #writing output to file if needed
        output.write(key + ": " + str(value) + "\n")

        #for printing to console if needed
        #print(key + ": " + str(value) + "\n")

    #closing file
    output.close()


# The average node degree of the graph.
def avgNodeDegree(number_of_node, degTotal):

    #calculating the average node degree which is the number of degrees in total from all of the edges divided by the number of nodes (user_ids)
    avgNodeDegree = round(degTotal / number_of_node, 2)

    #creating some space in term
    print("\n")

    #returning avgNodeDegree in format needed
    return "avgNodeDegree:" + str(avgNodeDegree) + "\n"



def main():

    # checking if the number of args is correct and if the arguments are in the correct positions
    if len(sys.argv) != 2:
        print("\nERROR: Incorrect number of arguments\n")
        print("USAGE: <python3> <""graph-stats.py""> <""yelp-network.txt"">\n")
        sys.exit()
   
    if sys.argv[0] != 'graph-stats.py':
        print("\nERROR: arg[0] must be graph-stats.py")
        sys.exit()

    if sys.argv[1] != 'yelp-network.txt':
        print("\nERROR: argv[1] must be yelp-network.txt")
        sys.exit()

    #csv file limit had to be raised since the file we are dealing with is larger then the allowed csv limit
    csv.field_size_limit(sys.maxsize)

#calling the method for execution
nodeDegreeDist()


#calling main method for execution
main()


# -------------------------------previous attempts at trying to make this code work until we finally got it -------------------------------


# def nodeDegreeDist():
#     # Nodes and Edges
#     G = nx.Graph()
#     number_of_edges = 0

#     with open("yelp-network.txt", 'r') as friends:
#         yelp_data  = csv.reader(friends, delimiter=",")

#         for col in yelp_data:
#             if (col[0] != 'user_id friends'):
#                 # Split frineds 
#                 nodesSplit = col[0].split(' ')
#                 # Check user and friend node before adding to graph
#                 if nodesSplit[0] not in G.nodes():
#                     G.add_node(nodesSplit[0])
#                 if nodesSplit[1] not in G.nodes():
#                     G.add_node(nodesSplit[1])

#                 G.add_edge(nodesSplit[0], nodesSplit[1])
    
#     print("Number of nodes: " + str(G.number_of_nodes()))
#     print("Number of edges: " + str(G.number_of_edges()))