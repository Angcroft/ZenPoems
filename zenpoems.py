import random
import nltk
from nltk.corpus import cmudict
from collections import Counter

#   Download necessary corpus
nltk.download('cmudict')
nltk.download('words')

#   Load CMU dictionary
d = cmudict.dict()

#   Conting syllables in a word
def count_syll(word):
    if word.lower() in d:
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
    else:
        return 0

#   Counting syllables in a phrase
def count_syll_phrase(phrase):
    words = phrase.split()
    syllable_count = sum(count_syll(word) for word in words)
    return syllable_count

#   Create words lists depending on the number of syllables
word_list = nltk.corpus.words.words()
one_syll = [word for word in word_list if count_syll(word) == 1]
two_syll = [word for word in word_list if count_syll(word) == 2]
three_syll = [word for word in word_list if count_syll(word) == 3]
four_syll = [word for word in word_list if count_syll(word) == 4]
five_syll = [word for word in word_list if count_syll(word) == 5]

#   Here we store every word, ordered by number of syllables
syll_collection = {
    1: one_syll,
    2: two_syll,
    3: three_syll,
    4: four_syll,
    5: five_syll
}

#   Function for generating a new line
def generate_line(target_syll):
    line = []
    current_syll_count = 0
    
    while current_syll_count < target_syll:
        remaining_syll = target_syll - current_syll_count
        possible_words = [word for syll in range(1, remaining_syll + 1) if syll in syll_collection for word in syll_collection[syll]]
        if not possible_words:
            break
        word = random.choice(possible_words)
        line.append(word)
        current_syll_count += count_syll(word)
        
    return ' '.join(line)

#   Function for generating a Haiku
def generate_haiku():
    line1 = generate_line(5)
    line2 = generate_line(7)
    line3 = generate_line(5)
    
    haiku = f"{line1}\n{line2}\n{line3}"
    return haiku

#   Haiku generated
print(generate_haiku())