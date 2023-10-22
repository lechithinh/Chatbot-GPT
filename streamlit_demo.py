import openai
import streamlit as st
from streamlit_chat import message

openai.api_key = ""

def generate_response(prompt):
    completion = openai.Completion.create(
        model="ada:ft-personal-2023-05-04-06-41-25",
        prompt=prompt,
        max_tokens=1024, 
        temperature=0, 
        top_p=1, 
        n=1, 
        stop=[" END"])

    message=completion.choices[0].text
    return message


st.title("Streamlit Chat - Demo")

#storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input=st.text_input("You:",key='input')

if user_input:
    output=generate_response(user_input)

    #store the output
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
