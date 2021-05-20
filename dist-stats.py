import csv, sys
import matplotlib.pyplot as plt

# restaurantCategoryDist: a frequency distribution of the number of restaurants in each category of restaurants
# (e.g.,  Chinese,  Japanese,  Korean,  Greek,  etc.)in  a  descending  order  of popularity 
# (from the most popular category to the least popular). The output should be one line per pair of values as follows: 
# category: #restaurants for example: Korean: 120 Italian: 110 ... 

def restaurantCategoryDist(city):

    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter=",")

        dataDict = {}
        dataSplit = ""
    
        for row in data:
            
            if row[4] == city and 'Restaurants' in row[12]:
               
                dataSplit = row[12].split(";")
               
                for key in dataSplit:
                   
                    if key == 'Restaurants':
                        continue
                   
                    elif key in dataDict.keys():
                        dataDict[key] += 1
                    
                    else:
                        dataDict[key] = 1
    
    sorteddictList = dict(sorted(dataDict.items(), key=lambda item: item[1], reverse=True))

#getting the first 10 elements of the sorted list
    top10 = {k: sorteddictList[k] for k in list(sorteddictList)[:10]}

#printing in the correct format wanted by prof eg: categoryTag:value
    for key, value in sorteddictList.items():
        print(key, ':', value)

#creating the plot with the correct specifications having top 10 tags and spacing as to not cut anything off
    categories = list(top10.keys())
    catCounts = list(top10.values())
    
    plt.figure(figsize=(15,5))
    plt.ylabel('Frequency')
    plt.xlabel('Restaurant Category')

    plt.title('Top 10 Restaurant Category Tags In The City Of: ' + city)
    plt.bar(range(len(top10)), catCounts, tick_label=categories, align='center', alpha=0.5)
    #plt.tick_params(axis='x', which='major', labelsize=3)
    plt.tight_layout()



   
    return sorteddictList   


# print('\n')
# print(str(restaurantCategoryDist('McMurray')))
# print('\n')

# restaurantReviewDist: a frequency distribution of the number of reviews submitted for each category of restaurants 
# (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order 
# (from the most reviewed category to the least reviewed), along with the average number of stars received per category. 
# The output should be one line per triplet as follows: category: #reviews: avg_stars for example: Korean: 580: 4.5 Italian: 110: 3.8 ...

def restaurantReviewDist(city):
   
   tagCount = 0
   starCount = 0
   avgStars = 0.0

   with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter=",")

        # key : number of reviews
        dataDict = {}

        #key : number of stars
        dataDict2 = {}

        # dataDict3 = {}

        dataSplit = ""
    
        for row in data:
            
            if row[4] == city and 'Restaurants' in row[12]:
               
                dataSplit = row[12].split(";")
               
                for key in dataSplit:
                   
                    if key == 'Restaurants': # if a tag == Restaurant do nothing, since we already assume we are looking at Restaurant tags
                        continue             # we only want to increment those tags that define the TYPE of Restaurant it is
                   
                    if key in dataDict.keys():
                        
                        dataDict[key] += int(row[10])
                    if key in dataDict2.keys():
    
                        dataDict2[key] += float(row[9]) 

                    
                    else:
                        dataDict[key] = int(row[10])
                        dataDict2[key] = float(row[9])
                
               

        sorteddictList = dict(sorted(dataDict.items(), key=lambda item: item[1], reverse=True))
        sorteddictList2 = dict(sorted(dataDict2.items(), key=lambda item: item[1], reverse=True))


        #printing some messages to the command line if the checks are passed, the stats will be displayed
        print("\n The most popular categories of food by country from the city " +city+" and ranked from most popular to least are: ")
        dictCOUNT = restaurantCategoryDist(city)
        print("\n \n")

        # #Checker to make sure no division by 0
        # for key, value in dictCOUNT.items():
        #     if value == 0:
        #         dictCOUNT.update({key:'1'})
        

        print("\n The total number of reviews for each restaurant by category from the city " +city+ ", as well as the average stars for those categories and ranked from most popular to least are: ")

        for key, value in sorteddictList.items():
            print(key ,':', value, ':', round(float(sorteddictList2[key]) / float(dictCOUNT[key]), 1))

        # print(sorteddictList)
        # print("\n \n \n")
        # print(sorteddictList2)



    
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

    # with open("yelp_business.csv", "r") as business:
    #     data = csv.reader(business, delimiter = ',')
    #     for row in data:
    #         if sys.argv[2] not in row[4]:
    #             print("\nPlease enter a valid city, city entered is not in the valid list of cities\n")
    #             sys.exit()

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

