# **Data Analytics Using Python**

### **In this project I write python programs/scripts for performing basic analytics on a large dataset. The dataset is a subset of Yelp1's businesses, reviews, and user  data. It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp's data. The dataset  contains seven CSV files including information about businesses across 11 metropolitan areas in four countries and can be accessed here(registration to Kaggle is required):Yelp dataset:https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6orYelp. The first program (dstats.py)performs descriptive analytics of the dataset.  The second(dist-stats.py)computes useful frequency distributions. The third (yelp-network.py) constructs a social network of Yelp friends. The fourth(graph-stats.py)performs basic network analytics.**


#### **A. Descriptive Statistics**
  I write a python program (dstats.py) that when given a city as input, the output will be:

  1) The number of businesses in that city
  2) The average stars each of those businesses have
  3) The number of resturants in that city
  4) The average stars those restuarants have
  5) The average number of reviews that each business has
  
  This will be written to a file for review/use later.

-----------------------------------------------------------------------------------------------------------------------------------------------
#### **B. Distribution Statistics**
  I write a python program (dist-stats.py) that when given a city as input, the output will be:
  
  1) A frequency distribution of the number of restaurants  in each category of restaurants(e.g.,  Chinese,  Japanese,  Korean,  Greek,  etc.)in a descending order  of popularity (from the most popular category to the least popular).
  2) A frequency distribution  of the  number  of reviews submitted  for each category of restaurants (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order (from  the  most  reviewed  category  to  the  least  reviewed),  along  with  the  average  number  of stars received per category.  
  3) A bar chart which will compare the top-10 highest frequency distributions from part 1 where the x-axis represents the restaurant category and the y-axis represents its frequency (#restaurants).

  This will be written to a file for review/use later.

-----------------------------------------------------------------------------------------------------------------------------------------------
#### **C. Creating the Yelp Social Network**
  I write a python program (yelp-network.py) that when given a collection of users from a file as input, the output will be:
  
  1) A social network of Yelp friends which will be represented as a graph G(V,E) where V is a set of vertices/nodes representing Yelp users and E is a set of links/edges representing the friendships/relationships between Yelp users. 
  
  The network will be represented in a file using the edge list format

-----------------------------------------------------------------------------------------------------------------------------------------------
#### **D. Computing Network Statistics** 
  I write a python program (graph-stats.py) that when given a file containing an edge list which represents a network such as the one created in part C, will output:
  
  1) The number of nodes (users) and edges (relationships) of the network.
  2) A frequency distribution of the node degrees of the network, in a descending order of frequency (from the highest to the lowest frequency). The degree of a node is the number of edges that are incident to the node (i.e.,  #neighbors).
  3) The average node degree of the graph.
  
  The output will be represented in a file using the edge list format

-----------------------------------------------------------------------------------------------------------------------------------------------
#### **HOW TO RUN:**

From the command line run:

PART A: python3 dstats.py yelp_business.csv (city of your choice here)

PART B: python3 dist-stats.py yelp_business.csv (city of your choice here)

PART C: python3 graph-stats.py yelp-network.txt

PART D: python3 yelp-network.py yelp-user.csv
