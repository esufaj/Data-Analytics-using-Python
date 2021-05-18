import csv, sys, copy
import matplotlib.pyplot as plt
import numpy as np

# restaurantCategoryDist: a frequency distribution of the number of restaurants in each category of restaurants
# (e.g.,  Chinese,  Japanese,  Korean,  Greek,  etc.)in  a  descending  order  of popularity 
# (from the most popular category to the least popular). The output should be one line per pair of values as follows: 
# category: #restaurants for example: Korean: 120 Italian: 110 ... 

def restaurantCategoryDist(city):
    mexCount, italCount, japCount, KorCount, greekCount, chineseCount, amerCount, frenchCount, otherCount, thaiCount, indianCount, caribbeanCount = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        for row in data:
            if row[4] == city and 'Restaurants' in row[12]: 
                
                if 'Mexican' in row[12]:
                    mexCount = mexCount + 1
                elif 'Italian' in row[12]:
                    italCount = italCount + 1
                elif 'Japanese' in row[12]:
                    japCount = japCount + 1
                elif 'Korean' in row[12]:
                    KorCount = KorCount + 1
                elif 'Greek' in row[12]:
                    greekCount = greekCount + 1
                elif 'Chinese' in row[12]:
                    chineseCount = chineseCount + 1
                elif 'American' in row[12]:
                    amerCount = amerCount + 1
                elif 'French' in row[12]:
                    frenchCount = frenchCount + 1 
                elif 'Thai' in row[12]:
                    thaiCount = thaiCount + 1
                elif 'Indian' in row[12]:
                    indianCount = indianCount + 1
                elif 'Caribbean' in row[12]:
                    caribbeanCount = caribbeanCount + 1
                else:
                    otherCount = otherCount + 1
        
        dictList = {'Mexican' : mexCount, 'Italian':italCount, 'Japanese':japCount, 'Korean':KorCount, 'Greek':greekCount, 'Chinese':chineseCount,
                'American':amerCount, 'Other':otherCount, 'Thai':thaiCount, 'Indian':indianCount, 'Caribbean':caribbeanCount}

        sorteddictList = dict(sorted(dictList.items(), key=lambda item: item[1], reverse=True))
        top10 = dict(sorteddictList.items(), key=lambda item: item[1])
        top10.popitem()

        

        for key, value in sorteddictList.items():
            print(key, ':', value)




    categories = list(sorteddictList.keys())
    catCounts = list(sorteddictList.values())
    

    plt.ylabel('Frequency')
    plt.xlabel('Restaurant Category')

    plt.title('Top 10 World Cuisines Categories In The City Of: ' + city)
    plt.bar(range(len(top10)), catCounts, tick_label=categories, align='center', alpha=0.5)
    #plt.tick_params(axis='x', which='major', labelsize=3)
    plt.tight_layout()

    return ""        


# print('\n')
# print(str(restaurantCategoryDist('Mississauga')))
# print('\n')

# restaurantReviewDist: a frequency distribution of the number of reviews submitted for each category of restaurants 
# (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order 
# (from the most reviewed category to the least reviewed), along with the average number of stars received per category. 
# The output should be one line per triplet as follows: category: #reviews: avg_stars for example: Korean: 580: 4.5 Italian: 110: 3.8 ...

def restaurantReviewDist(city):
    mexCount, italCount, japCount, KorCount, greekCount, chineseCount, amerCount, frenchCount, otherCount, thaiCount, indianCount, caribbeanCount = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    mexStar, italStar, japStar, korStar, greekStar, chineseStar, amerStar, frenchStar, otherStar, thaiStar, indianStar, caribbeanStar = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    mexrestCount, italrestCount, japrestCount, korrestCount, greekrestCount, chineserestCount, amerrestCount, frenchrestCount, otherrestCount, thairestCount, indianrestCount, caribbeanrestCount = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    avgstrMex, avgstrItal, avgstrJap, avgstrKor, avgstrGreek, avgstrChinese, avgstrAmer, avgstrFrench, avgstrOther, avgstrThai, avgstrIndian, avgstrCaribbean = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

    with open("yelp_business.csv", "r") as business:
        data = csv.reader(business, delimiter = ',')
    
        for row in data:
            if row[4] == city and 'Restaurants' in row[12]: 
                
                if 'Mexican' in row[12]:
                    mexCount = mexCount + int(row[10])
                    mexStar = mexStar + float(row[9])
                    mexrestCount +=1
                    if mexrestCount == 0:
                        avgstrMex = 0.0
                    else:
                         avgstrMex = mexStar / mexrestCount

                elif 'Italian' in row[12]:
                    italCount = italCount + int(row[10])
                    italStar = italStar + float(row[9])
                    italrestCount +=1
                    if italrestCount == 0:
                        avgstrItal = 0.0
                    else:
                         avgstrItal = italStar / italrestCount

                elif 'Japanese' in row[12]:
                    japCount = japCount + int(row[10])
                    japStar = japStar + float(row[9])
                    japrestCount +=1
                    if japrestCount == 0:
                        avgstrJap = 0.0
                    else:
                        avgstrJap = japStar / japrestCount

                elif 'Korean' in row[12]:
                    KorCount = KorCount + int(row[10])
                    korStar = korStar + float(row[9])
                    korrestCount +=1
                    if korrestCount == 0:
                        avgstrKor = 0.0
                    else:
                        avgstrKor = korStar / korrestCount

                elif 'Greek' in row[12]:
                    greekCount = greekCount + int(row[10])
                    greekStar = greekStar + float(row[9])
                    greekrestCount +=1
                    if greekrestCount == 0:
                        avgstrGreek = 0.0
                    else:
                        avgstrGreek = greekStar / greekrestCount

                elif 'Chinese' in row[12]:
                    chineseCount = chineseCount + int(row[10])
                    chineseStar = chineseStar + float(row[9])
                    chineserestCount +=1
                    if chineserestCount == 0:
                        avgstrChinese = 0.0
                    else:
                        avgstrChinese = chineseStar / chineserestCount

                elif 'American' in row[12]:
                    amerCount = amerCount + int(row[10])
                    amerStar = amerStar + float(row[9])
                    amerrestCount +=1
                    if amerrestCount == 0:
                        avgstrAmer = 0.0
                    else:
                        avgstrAmer = amerStar / amerrestCount

                elif 'French' in row[12]:
                    frenchCount = frenchCount + int(row[10])
                    frenchStar = frenchStar + float(row[9])
                    frenchrestCount +=1
                    if frenchrestCount == 0:
                        avgstrFrench = 0.0
                    else:
                        avgstrFrench = frenchStar / frenchrestCount

                elif 'Thai' in row[12]:
                    thaiCount = thaiCount + int(row[10])
                    thaiStar = thaiStar + float(row[9])
                    thairestCount +=1
                    if thairestCount == 0:
                        avgstrThai = 0.0
                    else:
                        avgstrThai = thaiStar / thairestCount

                elif 'Indian' in row[12]:
                    indianCount = indianCount + int(row[10])
                    indianStar = indianStar + float(row[9])
                    indianrestCount +=1
                    if indianrestCount == 0:
                        avgstrIndian = 0.0
                    else:
                        avgstrIndian = indianStar / indianrestCount

                elif 'Caribbean' in row[12]:
                    caribbeanCount = caribbeanCount + int(row[10])
                    caribbeanStar = caribbeanStar + float(row[9])
                    caribbeanrestCount +=1
                    if caribbeanrestCount == 0:
                        avgstrCaribbean = 0.0
                    else:
                        avgstrCaribbean = caribbeanStar / caribbeanrestCount

                else:
                    otherCount = otherCount + int(row[10])
                    otherStar = otherStar + float(row[9])
                    otherrestCount +=1
                    if otherrestCount == 0:
                        avgstrOther = 0.0
                    else:
                        avgstrOther = otherStar / otherrestCount
        
        dictList = {'Mexican' : [mexCount,avgstrMex], 'Italian':[italCount,avgstrItal], 'Japanese':[japCount,avgstrJap], 
                    'Korean':[KorCount,avgstrKor], 'Greek':[greekCount,avgstrGreek], 'Chinese':[chineseCount,avgstrChinese],
                'American':[amerCount,avgstrAmer], 'French':[frenchCount,avgstrFrench], 'Other':[otherCount,avgstrOther],
                'Thai':[thaiCount, avgstrThai], 'Indian':[indianCount,avgstrIndian], 'Caribbean':[caribbeanCount,avgstrCaribbean]}

        sorteddictList = dict(sorted(dictList.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorteddictList.items():
        print(key, ':', value[0], ':', round(value[1],1))



    
    return ""




def main():
    # checking if the number of args is correct and if the arguments are in the correct positions
    if len(sys.argv) != 3:
        print("\nERROR: Incorrect number of arguments\n")
        print("USAGE: <python3> <""dist-stats.py""> <""yelp_business.csv""> <city name>\n")
        sys.exit()
   
    if sys.argv[0] != 'dist-stats.py':
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
    print("\n The most popular categories of food by country from the city " +city+" and ranked from most popular to least are: ")
    print(restaurantCategoryDist(city))

    print("\n The total number of reviews for each restaurant by category from the city " +city+ ", as well as the average stars for those categories and ranked from most popular to least are: ")
    print(restaurantReviewDist(city))
    print("\n")


#calling main method for execution
main()

#calling matlibplot show() at the bottom of the code in order for execution of code to continue.
#if show() was called in the restuarantCategoryDist(city) execution would continue up until show() and nothing after would be executed until the plot is closed
plt.show()

