import re
import statistics
from statistics import median
from collections import Counter

text = '''\
Ехал Грека через реку. Видит Грека в реке рак.
Сунул Грека руку в реку, рак за руку Греку цап.
'''

def get_words_amount(text):
    words = re.findall(r'\w+', text)
    words = [i.title() for i in words]
    ls = Counter(words).most_common()
    ls.sort(key=lambda x: (-x[1], x[0]))
    for word, i in ls:
        print(word, i)

def get_average_amount(text):
    numbers_per_sentence =  [len(words) for words in (sentence.split() for sentence in text.split("."))]
    mean = sum(numbers_per_sentence)/len(numbers_per_sentence)
    print(mean)

def get_median_amount(text):
    print(median([len(sentence.split()) for sentence in text.split(".")]))


   
get_words_amount(text)
get_average_amount(text)
get_median_amount(text)
