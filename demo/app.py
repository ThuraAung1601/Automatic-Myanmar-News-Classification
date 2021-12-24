import streamlit as st
import pickle
import numpy as np
import pyidaungsu as pds
from sklearn.feature_extraction.text import TfidfVectorizer

stopwordslist = []
slist = []

with open("./stop_words.txt", encoding = 'utf8') as stopwordsfile:
    stopwords = stopwordsfile.readlines()
    slist.extend(stopwords)

    for w in range(len(slist)):
        temp = slist[w]
        stopwordslist.append(temp.rstrip())

def stop_word(sentence):
  new_sentence = []
  for word in sentence.split():
    if word not in stopwordslist:
      new_sentence.append(word)
  return(' '.join(new_sentence))


def tokenize(line):
    sentence = pds.tokenize(line,form="word")
    sentence = ' '.join([str(elem) for elem in sentence])
    sentence = stop_word(sentence)
    return sentence

filename = './nb_model.sav'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

vectorizer = pickle.load(open("vectorizer.pickle", "rb"))

st.title('Automatic News Classification System for Myanmar Language')
st.subheader("Input the News content below")
sentence = st.text_area("Enter your news Content Here", height=200)
sentence = tokenize(sentence)
predict_btt = st.button("Predict")
if predict_btt:
  data = vectorizer.transform([sentence]).toarray()
  prediction = loaded_model.predict(data)
  if prediction == ['Politics']:
    st.text("This is Politics News")
  elif prediction == ['Sports']:
    st.text("This is Sports News")
  elif prediction == ['Entertainment']:
    st.text("This is Entertainment News")
  elif prediction == ['Business']:
    st.text("This is Business News")
  

