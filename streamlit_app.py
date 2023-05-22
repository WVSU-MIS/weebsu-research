import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]
import hashlib

global history

def append_history(history, item):
    history.append(item)
    return history

def get_reply(input_string): 
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a helpful assistant. \
          follow the instructions below: 1. Ensure you adhere closely \
          to the given instructions of the user. 2. Think in a \
          step by step fashion."},
          {"role": "user", "content":  + input_string}
        ]
    )

    # Print the generated response
    answer = response['choices'][0]['message']['content']
    return answer

# Define the Streamlit app
def app():
    history = []
    st.title("Weebsu Research Helper Chatbot")
    st.header("AI assistant for improving research at WVSU.")
    
    st.write("A research helper chatbot is a computer program that can be used to help researchers with their work. Chatbots can be used to perform a variety of tasks, such as:\
    \n\nFinding and retrieving information: Chatbots can be used to search for information on the web, in databases, and in other sources. They can also be used to retrieve specific pieces of information, such as citations, definitions, and research papers. \
     \n\nBrainstorming and generating ideas: Chatbots can be used to help researchers brainstorm and generate ideas. They can ask questions, provide feedback, and help researchers to think outside the box.")
    
    # Create a multiline text field
    course = st.text_area('Input field of discipline or course (do not use acronym):', height=2)
What are research areas in the field of 
    # Display the text when the user submits the form
    if st.button('Submit'):
        history = append_history(history, ('user: What are research areas in the field of ' + course))
        output = get_reply('What are research areas in the field of ' + course)
        history = append_history(history, ('Weebsu: ' + output))
        for item in range(len(history)):
            st.write(history[item])
            
        study_area = st.text_area('Copy one of the recommended research areas or input your own:', height=5)
        if st.button('Find Research Topics'):
            history = append_history(history, ('user: What are research topics in the field of ' + study_area))
            output = get_reply('What are research topics in the field of ' + study_area)
            history = append_history(history, ('Weebsu: ' + output))
            for item in range(len(history)):
                st.write(history[item])
    
    st.write('\n\n\n© 2023 West Visayas State University - Management Information System Office.')
    st.write('\n\n\nDisclaimer: Weebsu may produce inaccurate information about people, places, or facts especially if the question is outside the scope of topics it was trained on.')
    text = "*WVSU at the forefront of AI-research in Western Visayas.*"
    st.markdown(text)

# Run the app
if __name__ == "__main__":
    app()
