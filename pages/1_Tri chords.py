import pandas as pd
import streamlit as st
import time
from PIL import Image
from random import randint

# data frame
def create_df():
    note = {'Note': ['DO', 'REb', 'RE', 'MIb', 'MI', 'FA', 'FA#', 'SOL', 'LAb', 'LA', 'SIb', 'SI']}
    posizione = {'Posizione': ['Fondamentale', 'Primo Rivolto', 'Secondo Rivolto']}
    stato = {'Stato': ['Maggiore', 'Minore', 'Aumentato', 'Diminuito']}
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

df_tri = create_df()

# pagina
st.title('Chords Generator App')
st.markdown("____")
text = 'Selecting the checkbox automatically generates a chord, the solution of which can be seen later with the specific button. In the perimeter of random chords there are 144 possibilities, representing the 12 notes, in 3 turns for 4 states (Major, Minor, Augmented, Diminished).'
st.write(text)
st.markdown("____")
st.write('Select the checkbox for generate a random chord')
st.markdown(" ")

# initializing with a random number
if "rn3" not in st.session_state:
    st.session_state["rn3"] = randint(0, len(df_tri['Accordo'])-1)

# callback function to change the random number stored in state
def change_number():
    st.session_state["rn3"] = randint(0, len(df_tri['Accordo'])-1)
    return
index_3 =  st.session_state.rn3
Accordo_random_3 = df_tri['Accordo'].iloc[index_3]
Stato_Accordo_random_3 = df_tri['Stato'].iloc[index_3]

# process
if st.checkbox("Generate", on_change=change_number):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)
    st.write(Accordo_random_3)
    st.markdown(" ")

    if st.button("Solution"):
        image_url = "{}/{}.jpg".format(Stato_Accordo_random_3, Accordo_random_3)
        image = Image.open(image_url)
        st.image(image, width=700) 
