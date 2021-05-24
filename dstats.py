import csv, sys

# I  am aware that opening the file at the beginning of each method is not the optimal solution, but I was having a hard time
# figuring out how to create a helper method to open the file once and then call that method once instead of the with statement.

#numOfBus: the number of businesses in the city
def numOfBus(city):
    counter = 0
    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        #looping through data and counting the number of businesses in the city specified 
        for row in data:
            if row[4] == city:
                counter = counter + 1

    #returning the number of businesses in the city      
    return counter
  

#avgStars: the average number of stars of a business in the city
def avgStars(city):
    numStars = 0.0
    avrStars = 0.0
    counter = 0

    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        #looping through data and if city given in term is same as city in row[4] from yelp data then
        for row in data:
            if row[4] == city:

                # increase counter add total stars for the businesses in that city and calculating the avg stars for the business
                counter = counter + 1
                numStars = numStars + float(row[9])
                avrStars = numStars / counter

    #returning avg stars for every business in the city
    return avrStars


#numOfRestaurants: the number of restaurants in the city
def numOfRestaurants(city):
    counter = 0
    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')

        # looping through data and counting the number of businesses in the city
        for row in data:

            # if city from term is = city in row[4] of yelp data, and Restuarants is in row[12] specifiying that the business is a Restaurant 
            # then we will increase the Restaurant counter
            if row[4] == city and 'Restaurants' in row[12]: 
                counter = counter + 1    
    
    # return the number of Restaurants in the city      
    return counter


#avgStarsRestaurants: the average number of stars of restaurants in the city
def avgStarsRestaurants(city):
    counter = 0
    numStars = 0.0
    avrStars = 0.0

    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        for row in data:

            #if city from term is = city in row[4] of yelp data, and Restuarants is in row[12] specifiying that the business is a Restaurant 
            # then we will increase the Restaurant counter
            if row[4] == city and 'Restaurants' in row[12]: 
                counter = counter + 1    

                # we will also add the number of stars for each Restaurant casting to a float to prepare for division
                numStars = numStars + float(row[9])

                #calculating average stars for each Restaurant 
                avrStars = numStars / counter

    # returning the average number of stars for each business that is a restuarant        
    return avrStars


#avgNumOfReviews: the average number of reviews for all businesses in the city
def avgNumOfReviews(city):
    counter = 0
    numReviews = 0.0
    avgReviews = 0.0
    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
        for row in data:
            if row[4] == city:
                counter = counter + 1
                numReviews = numReviews + float(row[10])
                avgReviews = numReviews / counter

    return avgReviews


#avgNumOfReviewsBus: the average number of reviews for restaurants in the city
def avgNumOfReviewsBus(city):
    counter = 0
    numReviews = 0.0
    avgReviews = 0.0
    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
        for row in data:
            if row[4] == city and 'Restaurants' in row[12]:
                counter = counter + 1
                numReviews = numReviews + float(row[10])
                avgReviews = numReviews / counter

    return avgReviews
   
    

def main():
    
# checking if the number of args is correct and if the arguments are in the correct positions
    if len(sys.argv) != 3:
        print("\nERROR: Incorrect number of arguments\n")
        print("USAGE: <python3> <""dstats.py""> <""yelp_business.csv""> <city name>\n")
        sys.exit()
   
    if sys.argv[0] not in 'dstats.py':
        print("\nERROR: arg[0] must be python3")
        sys.exit()

    if sys.argv[1] != 'yelp_business.csv':
        print("\nERROR: argv[1] must be dstats.py")
        sys.exit()

    # city is = to term arg in 2nd position
    city = sys.argv[2]
                

# printing some messages to the command line if the checks are passed, the stats will be displayed
    print("\nThe number of businesses in the city " + city + " is: ")
    print(numOfBus(city)) 
    
    print("\nThe average number of stars of all the businesses in the city " + city + " is: ")  
    print(round(avgStars(city),2))
    
    print("\nThe number of restaurants in the city " + city + " is: " ) 
    print(numOfRestaurants(city))
    
    print("\nThe average number of stars for all of the restaurants in the city " + city + " is: " ) 
    print(round(avgStarsRestaurants(city),2))
    
    print("\nThe average number of reviews for all of the businesses in the city " + city + " is: " ) 
    print(round(avgNumOfReviews(city),2))
    
    print("\nThe average number of reviews for all of the restaurants in the city " + city + " is: " )
    print(round(avgNumOfReviewsBus(city),2))
    
    print("\n")

main()
