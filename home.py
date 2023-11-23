import pandas as pd
import streamlit as st
from PIL import Image


# data frame
def create_df_3notes():
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

# data frame
def create_df_4notes():
    note = {'Note': ['DO', 'REb', 'RE', 'MIb', 'MI', 'FA', 'SOLb', 'SOL', 'LAb', 'LA', 'SIb', 'SI']}
    posizione = {'Posizione': ['Fondamentale', 'Primo Rivolto', 'Secondo Rivolto', 'Terzo Rivolto']}
    stato = {'Stato': ['Settima Maggiore']}
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

df_3 = create_df_3notes()
df_4 = create_df_4notes()

# pagina
st.title('Chords Generator App')
st.markdown("____")
text = 'This app allows you to do exercises on the position and composition of chords on the piano, including all the turns. Using the selection boxes below you can see all the chords contained in the application, with the corresponding picture of the location. On the pages to the right, however, you can do exercises by selecting a chord randomly'
st.write(text)
st.markdown("____")

# boxes
option_3 = st.selectbox('3 notes chords list:',(df_3['Accordo'].unique()), placeholder='Select one chord to visualize the position',index=None)
if option_3 != None:
    image_url = "{}/{}.jpg".format(option_3.split(' ')[1], option_3)
    image = Image.open(image_url)
    st.image(image, width=700) 

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

option_4 = st.selectbox('4 notes chords list:',(df_4['Accordo'].unique()), placeholder='Select one chord to visualize the position',index=None)
if option_4 != None:
    image_url = "{}/{}.jpg".format(option_4.split(' ')[1] + ' ' + option_4.split(' ')[2], option_4)
    image = Image.open(image_url)
    st.image(image, width=700) 

