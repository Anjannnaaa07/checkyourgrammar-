import streamlit as st 
from gingerit.gingerit import GingerIt

def text_correction (text):
    input_text = text
    parser = GingerIt()
    result = parser.parse(input_text)
    return result

st.header('Check grammar and spellings in your text!')
text_area = st.text_area('Enter your text')
if text_area is not None:
    if st.button("Submit"):
        st.write ("Input text is:")
        st.success(text_area)
        corrected_text = text_correction (text_area)
        st.write (corrected_text)
    
    


    
    