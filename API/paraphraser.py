import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from random import randint

# Ensure necessary NLTK data is downloaded
nltk.download()
nltk.download('punkt')  # Sentence and word tokenization
nltk.download('averaged_perceptron_tagger')  # POS tagging
nltk.download('wordnet')  # Synonyms for paraphrasing
nltk.download('omw-1.4')

def paraphrase(text: str) -> str:
    output = []

    # Tokenize the text
    words = word_tokenize(text)
    tagged = nltk.pos_tag(words)

    for i, (word, tag) in enumerate(tagged):
        replacements = []
        
        # Ignore proper nouns (NNP) and determiners (DT)
        if tag in ['NNP', 'DT']:
            output.append(word)
            continue

        # Extract part of speech for WordNet
        pos_map = {'J': wordnet.ADJ, 'V': wordnet.VERB, 'N': wordnet.NOUN, 'R': wordnet.ADV}
        word_type = pos_map.get(tag[0].upper(), None)  # Get corresponding WordNet POS

        if word_type:
            for syn in wordnet.synsets(word, pos=word_type):
                syn_word = syn.lemmas()[0].name()  # Get the first synonym
                if syn_word.lower() != word.lower():  # Avoid replacing with itself
                    replacements.append(syn_word)

        # Use a random replacement if available, otherwise keep the original word
        output.append(replacements[randint(0, len(replacements) - 1)] if replacements else word)

    return " ".join(output)

