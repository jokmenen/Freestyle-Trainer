import nltk
from nltk.corpus import wordnet as wn

# Ensure you have the necessary NLTK data
# nltk.download('wordnet')
nltk.download('omw-1.4')  # Open Multilingual Wordnet, check if Dutch is supported

# Assuming you want to work with a language supported by NLTK's WordNet
def get_definitions(word, lang='nld'):  # ISO 639-3 code for Dutch
    # Look up synsets in the specified language
    synsets = wn.synsets(word, lang=lang)
    definitions = []
    for synset in synsets:
        # Append definitions for each synset of the word
        definitions.append(synset.definition())
    return definitions

if __name__ == '__main__':
    # Example usage
    word = 'huisdier'  # Dutch for "dog"
    definitions = get_definitions(word)
    for definition in definitions:
        	print(definition)