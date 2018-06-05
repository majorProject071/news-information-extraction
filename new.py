import spacy
import en_core_web_sm
import nltk
import sys

from spacy.matcher import Matcher,PhraseMatcher
from spacy.attrs import POS,LOWER,IS_PUNCT

from modules.vehicles_gazetter import VehicleInformation
# from spacy import displacy
# nlp = spacy.load('en_core_web_sm')
nlp = en_core_web_sm.load()

deathverb = ['die', 'kill', 'crush', 'pass']
injuryverb = ['injure', 'sustain', 'critical', 'hurt', 'wound', 'harm', 'trauma']
# ----------------------------------------

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


news_story = """fifty eight persons died and 24 others were injured when a two-wheeler Lu 2 Kha 291 plunged into Trishuli River in between Fisling and Chumlingtar of Chitwan district on Wednesday.
There were 28 persons on board the ill-fated.
Police suspect that the incident might have occurred after the bus hit a truck coming from the wrong lane.  Police have impounded the truck and arrested its driver for investigation.
"""


# news_story = """A woman died after being hit by a bus in Sinamangal of Kathmandu on Monday.
#
# The victim has been identified as Goshan Mikrani Begham (49) of Sarlahi.
#
#
#
# Critically injured in the incident, she was rushed to the Bansbari-based Neuro Hospital where she breathed her last during the course of treatment, police said.
#
# The incident took place at around 7 am yesterday.
#
# Police said that they have impounded the vehicle Ba 2 Kha 7085 and arrested its driver for investigation."""

# a1 =nltk.sent_tokenize(news_story)
# print(a1)
# sys.exit()
# doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers")

# document = unicode(news_story.decode('utf8'))
# doc = nlp(document)

# import spacy
# from spacy.lang.en.examples import sentences

# nlp = spacy.load('en_core_web_sm')
# doc = nlp(sentences[0])
vehicle_information = VehicleInformation(news_story)
vehicle_information.make_gazetter()
all_vehicles = vehicle_information.find_vehicles()
print(all_vehicles)
# ------Gets the vehicle name-----
# document = unicode(news_story.decode('utf8'))
# doc = nlp(document)
#
#
# from spacy.matcher import Matcher
# matcher = Matcher(nlp.vocab)
# matcher.add_pattern("Vehicles", [{LOWER: "two"},{IS_PUNCT:True},{LOWER: "wheeler"}])
# # matcher.add_pattern("Vehicles", [{LOWER: "truck"}])
#
# # doc = nlp(u'Hello, world!')
# matches = matcher(doc)
#
# for ent_id, label, start, end in matches:
#     print(doc[start:end], label, ent_id )
