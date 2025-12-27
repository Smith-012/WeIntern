import re
from collections import Counter
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))

def analyze_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s.]", "", text)    #text cleaning

    words = [w for w in text.split() if w not in STOPWORDS]
    sentences = [s for s in text.split(".") if s.strip()]

    word_count = len(words)
    avg_sentence_length = round(
        word_count / max(1, len(sentences)), 2
    )

    top_words = Counter(words).most_common(5)

    return word_count, avg_sentence_length, top_words
