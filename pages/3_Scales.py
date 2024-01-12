import pandas as pd
import streamlit as st
import time
from PIL import Image
from random import randint


# data frame
def create_df_scales():
    note = {'Note': ['DO', 'REb', 'RE', 'MIb', 'MI', 'FA', 'FA#', 'SOL', 'LAb', 'LA', 'SIb', 'SI']}
    stato = {'Stato': ['Maggiore', 'Minore Naturale','Minore Armonica', 'Minore Melodica']}
    note_df = pd.DataFrame(note)
    stato_df = pd.DataFrame(stato)
    note_df['key'] = 1
    stato_df['key'] = 1
    df = pd.merge(note_df, stato_df, on ='key')
    df.drop('key', axis=1, inplace=True)
    df['Scala'] = df['Note'] + ' ' + df['Stato']
    return df


df_scales = create_df_scales()


# pagina
st.title('Chords Generator App')
st.markdown("____")
text = 'Selecting the checkbox automatically generates a scale, the positions and notes of which can be seen later with the specific button.'
st.write(text)
st.markdown("____")
st.write('Select the checkbox for generate a random scale')
st.markdown(" ")


# initializing with a random number
if "rnsc" not in st.session_state:
    st.session_state["rnsc"] = randint(0, len(df_scales['Scala'])-1)

# callback function to change the random number stored in state
def change_number():
    st.session_state["rnsc"] = randint(0, len(df_scales['Scala'])-1)
    return    

index_sc =  st.session_state.rnsc
Scala_random_sc = df_scales['Scala'].iloc[index_sc]                              


# process
if st.checkbox("Generate", on_change=change_number):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)
    st.write(Scala_random_sc)
    st.markdown(" ")

    if st.button("Solution"):
        image_url_scale = "{}/{}.jpg".format('Scale', Scala_random_sc)
        image_scale = Image.open(image_url_scale)
        st.image(image_scale, width=700) 
