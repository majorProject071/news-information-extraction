from __future__ import print_function

import nltk
import re

from modules.tagger import Tagger
class DataExtractor:
    """ A class to extract the required data like location, month, deaths,etc.
        from the news story.
    """
    def __init__(self,pos_tagged_words):
        self.pos_tagged_words = pos_tagged_words

    def location(self):
        """ Gets the location from the news story.

            Inputs include the parts of speech tagged words.
            Output is the phrase containing the location of mishap.
        """
        location_regex = "Location: {<IN><NNP|NN>+}"

        location_regex = r"""
                      Location:
                        {<IN><NNP|NN>+}          # Chunk everything
                        }<IN|NN>{      # Chink sequences of VBD and IN
                  """
        location_parser = nltk.RegexpParser(location_regex)
        # location = location_parser.parse(self.pos_tagged_words)
        # return location

        for i in self.pos_tagged_words:
            location = location_parser.parse(i)
            for i in location.subtrees(filter=lambda x:x.label() == 'Location'):
                print(i.leaves())

    def day(self,complete_news):
        """ Gets the day of mishap.
        """
        day_regex = re.compile('\w+day')
        day = day_regex.findall(complete_news)[0]
        print("The day when the accident occured is: \n"+day)



    def vehicle(self):
        """ Gets the vehicle number from the news story.

            Inputs inclue the POS tagged words from the news.
            Output is the phrase containing the vehicle number.
        """

        vehicle_regex = "Vehicle: {<.*><CD><.*><CD>}"
        vehicle_parser = nltk.RegexpParser(vehicle_regex)

        for i in self.pos_tagged_words:
            vehicle = vehicle_parser.parse(i)
            for i in vehicle.subtrees(filter=lambda x:x.label() == 'Vehicle'):
                for p in i.leaves():
                    print(p[0],end=' ')
                print("\n")

    def deaths(self,sentences):
        """ Gets the number of deaths from the news story.

            Inputs include the POS tagged words from the news story.
            Output includ the number of deaths mentioned in the news.
        """

        death_words = ["died","death","killed","life"]
        # death_regex = "Deaths: {<NNP>?<CD><NNS|NNP>?<VBD|VBN>?<VBD|VBN>}"
        death_regex = "Deaths: {<CD>}"
        has_deaths = [sent for sent in sentences if("died" or "death") in
                        nltk.word_tokenize(sent)]
        print(has_deaths)
        print(has_deaths[0].split("and"))
        # death_regex = r"""
        #     Deaths:
        #     """
        death_parser = nltk.RegexpParser(death_regex)

        for i in self.pos_tagged_words:
            deaths = death_parser.parse(i)
            for i in deaths.subtrees(filter = lambda x:x.label() == 'Deaths'):
                print(i.leaves())

    def injury(self,sentences):
        has_injuries = [sent for sent in sentences if("injured" or "injury"
                        or "injuries" or "injur") in nltk.word_tokenize(sent)]
        print(has_injuries)

        has_injuries_words = nltk.word_tokenize(has_injuries[0])

        injury_pos_tagged = nltk.pos_tag(has_injuries_words)
        print(injury_pos_tagged)

        injury_regex = r"""
                      INjury:
                        {<.*>+}          # Chunk everything
                        }<CC|IN|NNS|NN|DT|WRB>+{      # Chink sequences of VBD and IN
                  """
        injury_parser = nltk.RegexpParser(injury_regex)
        injury_occurence = injury_parser.parse(injury_pos_tagged)
        print(injury_occurence)
