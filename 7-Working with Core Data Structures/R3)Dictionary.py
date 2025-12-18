import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "God is Great! I won a lottery."

sentences=sent_tokenize(text)
print("sentences:", sentences)
tokens=word_tokenize(text)
print("word tokens:", tokens)

#Stop Words Removing
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
print("stop words removal:", filtered_tokens)

#Lower Casing
lower_tokens=[w.lower() for w in filtered_tokens]
print("lower cased tokens:", lower_tokens)

#Stemming
ps=PorterStemmer()
stemmed=[ps.stem(w) for w in lower_tokens]
print("stemmed tokens:", stemmed)

#Lemmatization
lemmatizer = WordNetLemmatizer()

lemmas1=[lemmatizer.lemmatize(w) for w in lower_tokens]
print("lemmatized (default pos=n):", lemmas1)

word='better'
print(f"lemmatized 'better' as adjective:", lemmatizer.lemmatize(word, pos='a'))



