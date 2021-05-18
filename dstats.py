import csv, sys

# I  am aware that opening the file at the beginning of each method is not the optimal solution, but I was having a hard time
# figuring out how to create a helper method to open the file once and then call that method instead of the with statement.

#numOfBus: the number of businesses in the city
def numOfBus(city):
    counter = 0
    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        for row in data:
            if row[4] == city:
                counter = counter + 1
    print(counter)
    return counter

#numOfBus("McMurray")    

#avgStars: the average number of stars of a business in the city
def avgStars(city):
    numStars = 0.0
    avrStars = 0.0
    counter = 0

    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        for row in data:
            if row[4] == city:
                counter = counter + 1
                numStars = numStars + float(row[9])
                avrStars = numStars / counter

    # print(numStars)        
    print(avrStars)
    # print(counter)
    return avrStars

#avgStars("McMurray")

#numOfRestaurants: the number of restaurants in the city
def numOfRestaurants(city):
    counter = 0
    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        for row in data:
            if row[4] == city and 'Restaurants' in row[12]: 
                counter = counter + 1    
                    
    print(counter)
    return counter

#numOfRestaurants("McMurray")

#avgStarsRestaurants: the average number of stars of restaurants in the city
def avgStarsRestaurants(city):
    counter = 0
    numStars = 0.0
    avrStars = 0.0

    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        for row in data:
            if row[4] == city and 'Restaurants' in row[12]: 
                counter = counter + 1    
                numStars = numStars + float(row[9])
                avrStars = numStars / counter
    # print(numStars)        
    print(avrStars)
    # print(counter)               
    return avrStars

#avgStarsRestaurants('McMurray')

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

    # print(counter)        
    # print(numReviews)
    print(avgReviews)
    return avgReviews

#avgNumOfReviews("McMurray")

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

    # print(counter)        
    # print(numReviews)
    print(avgReviews)
    return avgReviews

#avgNumOfReviewsBus('McMurray')    
    

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

    # with open("yelp_business.csv", "r") as business:
    #     data = csv.reader(business, delimiter = ',')
    #     for row in data:
    #         if sys.argv[2] not in row[4]:
    #             print("\nPlease enter a valid city, city entered is not in the valid list of cities\n")
    #             sys.exit()

    city = sys.argv[2]
                

# printing some messages to the command line if the checks are passed, the stats will be displayed
    print("\nThe number of businesses in the city " + city + " is: ")
    numOfBus(city) 
    print("\nThe average number of stars of all the businesses in the city " + city + " is: ")  
    avgStars(city)
    print("\nThe number of restaurants in the city " + city + " is: " ) 
    numOfRestaurants(city)
    print("\nThe average number of stars for all of the restaurants in the city " + city + " is: " ) 
    avgStarsRestaurants(city)
    print("\nThe average number of reviews for all of the businesses in the city " + city + " is: " ) 
    avgNumOfReviews(city)
    print("\nThe average number of reviews for all of the restaurants in the city " + city + " is: " )
    avgNumOfReviewsBus(city)
    print("\n")

main()
