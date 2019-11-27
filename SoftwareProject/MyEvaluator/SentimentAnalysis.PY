import nltk
import pandas as pd 
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

ss = sid.polarity_scores("I think the professor is boring")
s2 = sid.polarity_scores(" the professor is not bad")

print(ss)
print(s2)