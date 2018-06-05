import spacy
import en_core_web_sm

from spacy.matcher import Matcher
from spacy.attrs import POS,LOWER,IS_PUNCT

nlp = en_core_web_sm.load()

vehicles_found = set()
vehicles = ['bus','car','truck','tipper','bike','zeep','scooter','scooty',
        'motorbike']

matcher = Matcher(nlp.vocab)
def make_gazetter():
    for vehicle in vehicles:
        matcher.add_pattern("Vehicles", [{LOWER:vehicle}])

def find_vehicles(news_story):
    document = unicode(news_story.decode('utf8'))
    doc = nlp(document)
    # matcher = Matcher(nlp.vocab)

    matches = matcher(doc)
    for ent_id, label, start, end in matches:
        vehicles_found.add(unicode(doc[start:end].text).encode('utf8'))
    return(vehicles_found)
