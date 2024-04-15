import pandas as pd
import streamlit as st
from PIL import Image
from random import randint
import time


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
    stato = {'Stato': ['Settima Maggiore', 'Settima Dominante', 'Settima Minore', 'Settima Semidiminuito', 'Settima Diminuito', 'Minore Settima Maggiore', 'Settima Maggiore Aumentato']}
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

# data frame
def create_df_intervals():
    note = {'Note': ['DO','RE','MI','FA','SOL','LA','SI']}
    alterazioni = {'Alterazioni': ['#','b','']}
    note_df = pd.DataFrame(note)
    alterazioni_df = pd.DataFrame(alterazioni)
    note_df['key'] = 1
    alterazioni_df['key'] = 1
    df_sub = pd.merge(note_df, alterazioni_df, on ='key')
    df_sub['Notes'] = df_sub['Note'] + '' + df_sub['Alterazioni']
    df_sub.drop('Note', axis=1, inplace=True)
    df_sub.drop('Alterazioni', axis=1, inplace=True)
    df_sub['key'] = 1
    df = pd.merge(df_sub, df_sub, on ='key')
    df['Intervals'] = df['Notes_x'] + ' - ' + df['Notes_y']
    df.drop('Notes_x', axis=1, inplace=True)
    df.drop('Notes_y', axis=1, inplace=True)
    df.drop('key', axis=1, inplace=True)
    return df

df_3 = create_df_3notes()
df_4 = create_df_4notes()
df_sc = create_df_scales()
df_int = create_df_intervals()

# pagina
st.title('Chords Generator App')
st.markdown("____")
text = 'This app allows you to do exercises on the position and composition of chords on the piano, including all the turns. Using the selection boxes below you can see all the chords contained in the application, with the corresponding picture of the location. On the pages to the right, however, you can do exercises by selecting a chord randomly'
st.write(text)
st.markdown("____")

# boxes
option_3 = st.selectbox('3 notes chords list:',(df_3['Accordo'].unique()), placeholder='Select one chord to visualize the position',index=None)
if option_3 != None:
    image_url_3 = "{}/{}.jpg".format(option_3.split(' ')[1], option_3)
    image_3 = Image.open(image_url_3)
    st.image(image_3, width=700) 

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

option_4 = st.selectbox('4 notes chords list:',(df_4['Accordo'].unique()), placeholder='Select one chord to visualize the position',index=None)
if option_4 != None:
    if len(option_4.split(' ')) == 5:
        img_str = "{}/{}.jpg".format(option_4.split(' ')[1] + ' ' + option_4.split(' ')[2] + ' ' + option_4.split(' ')[3], option_4)
    else: 
        img_str = "{}/{}.jpg".format(option_4.split(' ')[1] + ' ' + option_4.split(' ')[2], option_4)
    image_url_4 = img_str
    image_4 = Image.open(image_url_4)
    st.image(image_4, width=700) 

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")   

option_sc = st.selectbox('Scales list:',(df_sc['Scala'].unique()), placeholder='Select one scale to visualize the position',index=None)
if option_sc != None:
    image_url_sc = "{}/{}.jpg".format('Scale', option_sc)
    image_sc = Image.open(image_url_sc)
    st.image(image_sc, width=700)

#Intervals
st.markdown(" ")    
st.markdown("____")
text = 'Select the checkbox for generate a random interval'
st.write(text)

# initializing with a random number
if "rn_int" not in st.session_state:
    st.session_state["rn_int"] = randint(0, len(df_int['Intervals'])-1)

# callback function to change the random number stored in state
def change_number():
    st.session_state["rn_int"] = randint(0, len(df_int['Intervals'])-1)
    return
index_int =  st.session_state.rn_int
Intervals_random_3 = df_int['Intervals'].iloc[index_int]

# process
if st.checkbox("Generate", on_change=change_number):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i+1)
    st.write(Intervals_random_3)
    st.markdown(" ")


