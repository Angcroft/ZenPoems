import random

#   Five syllable phrases
five_phrases = [
    "The moon is shining",
    "Over the blue sea",
    "In the mountains high",
    "Wind on the pines trees",
    "Clear Sky above us"
]

#   Seven syllable phrases
seven_phrases = [
    "Among the clouds and the sun",
    "Leaves are falling slowly down",
    "The river sings softly",
    "Flowers bloom in the garden",
    "A whisper in the air"
]

def generate_haiku():
    line1 = random.choice(five_phrases)
    line2 = random.choice(seven_phrases)
    line3 = random.choice(five_phrases)

    haiku = f"{line1}\n{line2}\n{line3}"
    return haiku

#   Generate haiku
print(generate_haiku())