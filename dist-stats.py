import matplotlib.pyplot as plt 
import csv, sys

# restaurantCategoryDist: a frequency distribution of the number of restaurants in each category of restaurants
# (e.g.,  Chinese,  Japanese,  Korean,  Greek,  etc.)in  a  descending  order  of popularity 
# (from the most popular category to the least popular). The output should be one line per pair of values as follows: 
# category: #restaurants for example: Korean: 120 Italian: 110 ... 

def restaurantCategoryDist(city):


    #opening yelp data 
    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter=",")

        #declaring dict to store tags
        dataDict = {}
        dataSplit = ""
    
        #looping through the yelp data
        for row in data:
            
            #checking if city from term is same as city in the 4th column of yelp data
            # also checking if the tag in column 12 has restuarant in it
            if row[4] == city and 'Restaurants' in row[12]:
               
               #splitting tags by ;
                dataSplit = row[12].split(";")
               
                #looping through the split tags, not counting restuarant since it would be the most counted tag
                for key in dataSplit:
                   
                    if key == 'Restaurants':
                        continue
                   
                    #incrementing the counter for each tag if its seen in the dict
                    elif key in dataDict.keys():
                        dataDict[key] += 1
                    
                    #if tag not in dict then we add it and give it an inital count of 1
                    else:
                        dataDict[key] = 1

    #sorting list in decreasing order
    sorteddictList = dict(sorted(dataDict.items(), key=lambda item: item[1], reverse=True))

    #getting the first 10 elements of the sorted list
    top10 = {k: sorteddictList[k] for k in list(sorteddictList)[:10]}

    #printing in the correct format wanted by prof eg: categoryTag:value
    for key, value in sorteddictList.items():
        print(key, ':', value)

    #creating the plot with the correct specifications having top 10 tags and spacing as to not cut anything off
    categories = list(top10.keys())
    catCounts = list(top10.values())
    
    #creating the graph (15,5) for extra spacing
    plt.figure(figsize=(15,5))
    plt.ylabel('Frequency')
    plt.xlabel('Restaurant Category')

    plt.title('Top 10 Restaurant Category Tags In The City Of: ' + city)
    plt.bar(range(len(top10)), catCounts, tick_label=categories, align='center', alpha=0.5)
    #plt.tick_params(axis='x', which='major', labelsize=3)
    plt.tight_layout()


    # returning the sorted list which contains tags in decreasing order
    # we return the list so that we can use this method for calculations in restuarantReviewDist(city)
    return sorteddictList   




# restaurantReviewDist: a frequency distribution of the number of reviews submitted for each category of restaurants 
# (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order 
# (from the most reviewed category to the least reviewed), along with the average number of stars received per category. 
# The output should be one line per triplet as follows: category: #reviews: avg_stars for example: Korean: 580: 4.5 Italian: 110: 3.8 ...

def restaurantReviewDist(city):
   

   with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter=",")

        # key : number of reviews
        dataDict = {}

        #key : number of stars
        dataDict2 = {}

        # dataDict3 = {}

        dataSplit = ""
    
        for row in data:
            
             #checking if city from term is same as city in the 4th column of yelp data
            # also checking if the tag in column 12 has restuarant in it
            if row[4] == city and 'Restaurants' in row[12]:
               
               #splitting data in categories column
                dataSplit = row[12].split(";")
               
               #looping through split data
                for key in dataSplit:
                   
                    if key == 'Restaurants': # if a tag == Restaurant do nothing, since we already assume we are looking at Restaurant tags
                        continue             # we only want to increment those tags that define the TYPE of Restaurant it is
                   
                   #checking whether tag is in dict
                    if key in dataDict.keys():
                        
                        #if tag is in dict we add the number of reviews for that tag to its current value
                        dataDict[key] += int(row[10])

                    # same kets as dataDict but value is total num of stars rather then reviews    
                    if key in dataDict2.keys():
                        
                        #if tag is in dict then we add the num of stars for that tag to its current value count
                        dataDict2[key] += float(row[9]) 

                    #if the tag is not in the dict then we add it and give it its inital values which is found in their respective columns
                    else:
                        dataDict[key] = int(row[10])
                        dataDict2[key] = float(row[9])
                
               
        #sorting both dics in decreasing order
        sorteddictList = dict(sorted(dataDict.items(), key=lambda item: item[1], reverse=True))
        sorteddictList2 = dict(sorted(dataDict2.items(), key=lambda item: item[1], reverse=True))


        #printing some messages to the command line if the checks are passed, the stats will be displayed
        print("\n The most popular categories of food by country from the city " +city+" and ranked from most popular to least are: ")
        dictCOUNT = restaurantCategoryDist(city)
        print("\n \n")

        

        print("\n The total number of reviews for each restaurant by category from the city " +city+ ", as well as the average stars for those categories and ranked from most popular to least are: ")

        #looping only through one dict is necessary since both dicts contain the same keys
        #and in the same order, so both dicts can be accessed using the single loop 
        for key, value in sorteddictList.items():

            #printing the key:value: total star count / tag count and rounding to 1 decimal place
            print(key ,':', value, ':', round(float(sorteddictList2[key]) / float(dictCOUNT[key]), 1))


        # returning nothing as nothing is needed to be returned, could change that later if needed
        return ""




def main():
    # checking if the number of args is correct and if the arguments are in the correct positions
    if len(sys.argv) != 3:
        print("\nERROR: Incorrect number of arguments\n")
        print("USAGE: <python3> <""dist-stats.py""> <""yelp_business.csv""> <city name>\n")
        sys.exit()
   
    if sys.argv[0] != 'dist-stats.py':
        print("\nERROR: arg[0] must be dist-stats.py")
        sys.exit()

    if sys.argv[1] != 'yelp_business.csv':
        print("\nERROR: argv[1] must be yelp_business.csv")
        sys.exit()

    # city is = to term arg in 2nd position
    city = sys.argv[2]
                
    #Needed to remove the method call from here since I needed to get the dict by returning it from restuarantCategoryDist(city)
    #and this caused the output to duplicate since I assigned the return value from restuarantCategoryDist(city)
    #to a variable in restaurantReviewDist(city)
    
    # printing some messages to the command line if the checks are passed, the stats will be displayed
    # print("\n The most popular categories of food by country from the city " +city+" and ranked from most popular to least are: ")
    # restaurantCategoryDist(city)


    # print("\n The total number of reviews for each restaurant by category from the city " +city+ ", as well as the average stars for those categories and ranked from most popular to least are: ")
    restaurantReviewDist(city)
    print("\n")


    


#calling main method for execution
main()

#calling matlibplot show() at the bottom of the code in order for execution of code to continue.
#if show() was called in the restuarantCategoryDist(city) execution would continue up until show() and nothing after would be executed until the plot is closed
plt.show()

