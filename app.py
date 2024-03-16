import panel as pn
import random
from get_definitions import get_definitions
import json

pn.extension()

WOORDENLIJST_NAME = 'ARI_JSON'

if WOORDENLIJST_NAME == 'opentaal_basiswoorden':
     # Example list of Dutch words from https://github.com/OpenTaal/opentaal-wordlist/blob/master/elements/basiswoorden-gekeurd.txt
    with open('basiswoorden-gekeurd.txt') as fp:
        dutch_words = fp.readlines()
        dutch_words = {woord : '' for woord in dutch_words}

if WOORDENLIJST_NAME == 'ARI_JSON':
     # Woordenlijst from https://github.com/AriSaadon/NederlandseWoordenboek/tree/main
    with open('Woordenlijst.json', encoding='utf-8') as fp:
        dutch_words = json.load(fp)

# Function to randomly select Dutch words
def generate_random_words(event=None):

    if toggle_definitions.value:
        word_display_format = "# {word:<{woordlength}}\n <span style='color: grey; font-size: small;'>\t\t{definition_text}</span>\n"
    else:
        word_display_format = "# {word}\n"

    words = random.sample(list(dutch_words.keys()), min(slider.value, len(dutch_words)))
    words_with_definitions = []
    woordlength = len(max(words, key=len))
    for word in words:
        if WOORDENLIJST_NAME == 'opentaal_basiswoorden':
            definitions = get_definitions(word)
        elif WOORDENLIJST_NAME == 'ARI_JSON':
            definitions = dutch_words[word]
        definition_text = definitions[0] if definitions else "No definition found"
        words_with_definitions.append(word_display_format.format(word=word, woordlength = woordlength, definition_text=definition_text))


    random_words_pane.object = ' '.join(words_with_definitions)
# Slider to select the number of words
slider = pn.widgets.IntSlider(name='Number of words', start=1, end=10, value=5)
toggle_definitions = pn.widgets.Checkbox(name='Toggle Definitions', value = True)

# Button to generate new words
generate_button = pn.widgets.Button(name='Generate New Words', button_type='primary')
generate_button.on_click(generate_random_words)

# Pane to display the random words
random_words_pane = pn.pane.Markdown('# ')

# Initial generation of random words
generate_random_words()
# Layout
layout = pn.Row(pn.layout.HSpacer(), pn.Column( pn.layout.VSpacer(), slider, generate_button, random_words_pane, toggle_definitions, pn.layout.VSpacer()), pn.layout.HSpacer(), align='center')

# css = """
# .bk-root {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     height: 100vh;
# }
# """
# pn.extension(raw_css=[css])

layout.servable()