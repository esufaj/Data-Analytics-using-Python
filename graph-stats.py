import csv, sys
import time

#a  frequency  distribution  of  the  node  degrees  of  the  network,  in  a descending order of frequency 
# (from the highest to the lowest frequency). The degree of a node is  the  number  of  edges  that  are  incident  to  the node  
# (i.e.,  #neighbors).  The  output  should  be one line per pair of values as follows: 
# nodeID:nodeDegfor example:JJ-aSuM4pCFPdkfoZ34q0Q:14pzpbr9mlagHhDRdin8DvPQ:12

#for measuring execution time
# start_time = time.time()

def nodeDegDist():

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
    numNodes = len(networkDict.keys())

    #edges have not been created yet
    numEdges = 0
    
    #looping through dict
    for node in networkDict.keys():

        #num of edges is = to the num of degrees the value part of the dict holds
        numEdges += networkDict[node]

    #degTotal holds num of edges so we can use it for calculations in avgNodeDeg method
    degTotal = int(numEdges)

    #has to divide by 2 since we are adding edge twice considering if A has B as friend then B has A as friend (bidirectional)
    numEdges = int(numEdges / 2)

    #creating space in term
    print("\n")

    #printing stats in necessary format
    print("#nodes: " + str(numNodes) + "  edges: " + str(numEdges))

    #calling method which will output stats to file
    nodeDeg(networkDict)

    #printing the average node degree by passing the total number of nodes and the total degrees for all of the nodes
    print(avgNodeDeg(numNodes, degTotal))



#method that takes a dictionary, sorts it in decreasing order and writes to file the user_id(node): # of incident edges to the node (user_id)
def nodeDeg(networkDict):

    #opening file to write outout too. Needed to write to file since outputting in terminal took > 10-15 minutes
    #writing to file took much less time approx. 2-4 min maybe less
    output = open("nodeDegDist.txt", 'w')

    #sorting dict items in decreasing order
    for key, value in sorted(networkDict.items(), key=lambda item: item[1], reverse=True):

        #writing output to file if needed
        output.write(key + ": " + str(value) + "\n")

        #for printing to console if needed
        # print(key + ": " + str(value) + "\n")

    #closing file
    output.close()


# The average node degree of the graph.
def avgNodeDeg(number_of_node, degTotal):

    #calculating the average node degree which is the number of degrees in total from all of the edges divided by the number of nodes (user_ids)
    avgNodeDeg = round(degTotal / number_of_node, 2)

    #creating some space in term
    print("\n")

    #returning avgNodeDeg in format needed
    return "avgNodeDeg:" + str(avgNodeDeg) + "\n"



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
nodeDegDist()


#for measuring execution time
# print("--- %s seconds ---" % (time.time() - start_time))


#calling main method for execution
main()