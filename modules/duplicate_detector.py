from difflib import SequenceMatcher

date1 = 2017-05-01
date2 = 2017-05-03

death1 = 23
death2 = 21

injury1 = 12
injury2 = 13

location1 = "kathmandu"
location2 = "pokhara"

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

print(date_similarity(str(date1),str(date2)))
print(location_similarity(location1,location2))
