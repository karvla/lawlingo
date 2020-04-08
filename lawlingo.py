import textract
#from sklearn.feature_extraction.text import CountVectorizer
import re 
#import spacy
#from spacy.lang.sv import Swedish
#from spacy.lang.en import English
import os
import sys

#nlp = Swedish()
#nlp = English()
#
#text = textract.process('./Dom2016-13.pdf', encoding='utf-16').decode('utf-16')

def sentences(text):
    return re.findall("[A-Z].*?[\.!?]", text, re.MULTILINE | re.DOTALL )


def words(text):
    text = text.lower()
    text = re.sub('\n', " ", text)
    text = re.sub('[/./?,!/:/(/)_]', "", text)
    words = text.split()
    return words


path = sys.argv[1]
for doc in os.listdir('./decisions_hd/'):
    text = textract.process(path + doc, encoding='utf-16').decode('utf-16')
    for word in words(text):
        print(word)



