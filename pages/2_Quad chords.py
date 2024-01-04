import pandas as pd
import streamlit as st
import time
from PIL import Image
from random import randint

# data frame
def create_df():
    note = {'Note': ['DO', 'REb', 'RE', 'MIb', 'MI', 'FA', 'SOLb', 'SOL', 'LAb', 'LA', 'SIb', 'SI']}
    posizione = {'Posizione': ['Fondamentale', 'Primo Rivolto', 'Secondo Rivolto', 'Terzo Rivolto']}
    stato = {'Stato': ['Settima Maggiore', 'Settima Dominante', 'Settima Minore']}
    note_df = pd.DataFrame(note)
    posizione_df = pd.DataFrame(posizione)
    stato_df = pd.DataFrame(stato)
    note_df['key'] = 1
    posizione_df['key'] = 1
    stato_df['key'] = 1
    df = pd.merge(note_df, posizione_df, on ='key')
    df = pd.merge(df, stato_df, on ='key')
    df.drop('key', axis=1, inplace=True)
    df['Accordo'] = df['Note'] + ' ' + df['Stato'] + ' ' + df['Posizione']
    return df


df_quad = create_df()

# pagina
st.title('Chords Generator App')
st.markdown("____")
text = 'Selecting the checkbox automatically generates a chord, the solution of which can be seen later with the specific button. In the perimeter of random chords there are 144 possibilities, representing the 12 notes, in 4 turns for 3 state (Seventh Major, Seventh Dominant, Seventh Minor).'
st.write(text)
st.markdown("____")
st.write('Select the checkbox for generate a random chord')
st.markdown(" ")

# initializing with a random number
if "rn4" not in st.session_state:
    st.session_state["rn4"] = randint(0, len(df_quad['Accordo']))

# callback function to change the random number stored in state
def change_number():
    st.session_state["rn4"] = randint(0, len(df_quad['Accordo']))
    return

index_4 =  st.session_state.rn4
Accordo_random_4 = df_quad['Accordo'].iloc[index_4]
Stato_Accordo_random_4 = df_quad['Stato'].iloc[index_4]

# process
if st.checkbox("Generate", on_change=change_number):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)
    st.write(Accordo_random_4)
    st.markdown(" ")

    if st.button("Solution"):
        image_url = "{}/{}.jpg".format(Stato_Accordo_random_4, Accordo_random_4)
        image = Image.open(image_url)
        st.image(image, width=700) 
