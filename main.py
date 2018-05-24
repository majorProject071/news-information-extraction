from __future__ import print_function

import os
import sys

import nltk
#semanti role labelibg, dependency parsing
# from modules import extractor
from modules.extractor import DataExtractor
from modules.tokenizer import Tokenize
from modules.tagger import Tagger
from modules.getdeathinjury import *

# news_story = """A woman died after a motorbike hit a scooter she was riding on at Banasthali in Kathmandu on Saturday.
#
# The victim has been identified as Rameshwori Maharjan of Kharibot.
#
#
#
# The motorbike  hit the scooter  at around 8:45 pm yesterday.
#
#
# Police said that they have impounded the motorbike and arrested the rider."""


# news_story = """fifty eight persons died and 24 others were injured when a passenger bus Lu 2 Kha 291 plunged into Trishuli River in between Fisling and Chumlingtar of Chitwan district on Wednesday.
# There were 28 persons on board the ill-fated.
# Police suspect that the incident might have occurred after the bus hit a truck coming from the wrong lane.  Police have impounded the truck and arrested its driver for investigation.
# """

news_story = """A woman died after being hit by a bus in Sinamangal of Kathmandu on Monday.

The victim has been identified as Goshan Mikrani Begham (49) of Sarlahi.



Critically injured in the incident, she was rushed to the Bansbari-based Neuro Hospital where she breathed her last during the course of treatment, police said.

The incident took place at around 7 am yesterday.

Police said that they have impounded the vehicle Ba 2 Kha 7085 and arrested its driver for investigation."""

# news_story = """
# A person died in a road accident at Balaju in Kathmandu on Monday night.
# """

# news_story = news_story.lower()
news = Tokenize(news_story)

#The model to find the death number takes the splited sentences to find the
# numer of death
splited_sentences = nltk.sent_tokenize(news_story)
# print(splited_sen)
# sys.exit()
# Get death count and injury count

# death = death_no(splited_sen)
# if death == "None":
#     actualdeath = death
#     deathNo = 0
# else:
#     actualdeath = remove_date(death)
#     deathNo = convertNum(death)
# print("Death No: ")
# print(death, actualdeath, deathNo)
#
# print("\n No of dead people: " + str(deathNo))
#Finding the death number ends here


# injury = injury_no(splited_sen)
# if injury == "None":
#     actualinjury = "None"
#     injuryNo = 0
# else:
#     actualinjury = remove_date(injury)
#     injuryNo = convertNum(injury)
# print("Injury No:")
# print(injury, actualinjury, injuryNo)
# print("\n No of injured people: " + str(injuryNo))

tokenized_words = news.split_words()
tagger = Tagger(tokenized_words)

pos_tagged_sentences = tagger.tag()


data_extractor = DataExtractor(pos_tagged_sentences,news_story)

sentences = news.split_story()#splits into sentences
# data_extractor.deaths(nltk.sent_tokenize(news_story))
data_extractor.day(news_story)

print("From the modular component")
print("--------------------------------")
print(data_extractor.location())
print(data_extractor.death_number())
print(data_extractor.injury_number())

# injuries = data_extractor.injury(nltk.sent_tokenize(news_story))

print("\nThe vehicles involved are:")
data_extractor.vehicle()
# print("new")fdfd
