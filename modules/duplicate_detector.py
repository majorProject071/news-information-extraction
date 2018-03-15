from difflib import SequenceMatcher

date1 = "2017-05-03"
date2 = "2017-05-03"

death1 = 23
death2 = 21

injury1 = 12
injury2 = 13

location1 = "kathmandu"
location2 = "kathmandu"

vehicle_nos1 = ["Na 4 Kha 512", "Ma 1 Pa 12"]
vehicle_nos2 = ["Na 2 Kha 143", "Ba 80 Pa 112"]

vehicles1 = ["bus","car"]
vehicles2 = ["car","bus"]
def date_similarity(d1,d2):
    if SequenceMatcher(None, d1, d2).ratio() == 1:
        return True
    else:
        return False

def location_similarity(loc1,loc2):
    if SequenceMatcher(None, loc1, loc2).ratio() == 1:
        return True
    else:
        return False
def vehicle_similarity(v1,v2):
    difference = list(set(v1) - set(v2))
    if difference != None:
        return False
    else:
        return True

def news_similarity():
    if date_similarity(date1,date2):
        if location_similarity(location1,location2):
            if vehicle_similarity(vehicle_nos1,vehicle_nos2):
                print("News are same")
            elif vehicle_similarity(vehicles1,vehicles2):
                if (death1==death2) and (injury1==injury2):
                    print("News are same")
                elif (death1 == None) and (death2 == None):
                    if(injury1==injury2):
                        print("News are same")
                elif (injury1 == None) and (injury2 == None):
                    if(death1==death2):
                        print("News are same")
                else:
                    print("News are different")
            else:
                print("News are different")
        else:
            print("News are different (location)")
    else:
        print("News are different(date)")
news_similarity()
