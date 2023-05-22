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
          {"role": "user", "content": input_string}
        ]
    )

    # Print the generated response
    answer = response['choices'][0]['message']['content']
    return answer

# Define the Streamlit app
def app():
    history = []
    st.title("Weebsu Research Helper Chatbot")
    st.header("Leveraging AI for enhancing research at WVSU")
    
    st.write("A research helper chatbot is a computer program that can be used to help researchers with their work. Chatbots can be used to search for information on the web, in databases, and in other sources. They can also be used to retrieve specific pieces of information, such as citations, definitions, and research papers. Chatbots can be used to help researchers brainstorm and generate ideas. They can ask questions, provide feedback, and help researchers to think outside the box.")
    level = 'undergraduate'
    options = ["undergraduate", "masters", "doctorate"]
    selected_option = st.selectbox("Select your academic level:", options)
    level = selected_option
    # Create an input field
    course = st.text_input('Input field of discipline or course, example: Computer Science (do not use acronyms):')
    # Display the text when the user submits the form
    if st.button('Discover research areas'):
        prompt = 'What are research areas in the field of ' + course
        prompt += (' appropriate for ' + level + ' degree')
        output = get_reply(prompt)
        history = append_history(history, ('Weebsu: ' + output))
        for item in range(len(history)):
            st.write(history[item])
            
    study_area = st.text_input('Copy one of the recommended research areas or input your own:')
    checkbox_state = st.checkbox('Enhance research with data science')
    if st.button('Explore Research Topics'):
        prompt = 'What are current research studies in the field of ' + study_area
        # Check the checkbox state
        if checkbox_state:
            prompt += (' enhance the research study with data science ')
        
        prompt += (' appropriate for ' + level + ' degree')
        output = get_reply(prompt)
        history = append_history(history, ('Weebsu: ' + output))
        for item in range(len(history)):
            st.write(history[item])

    topic = st.text_input('Copy one of the recommended research topics or input your own:')
    if st.button('Get Research Recommendations'):
        prompt = 'Recommend a research title for ' + study_area
        prompt += (' a research study appropriate for ' + level + ' degree')
        # Check the checkbox state
        if checkbox_state:
            prompt += (' enhance the research study with data science ')
        prompt += (' give a brief abstract')
        prompt += ' What type of research is appropriate? '
        prompt += 'Generate some questions to help the research conduct this study. '
        prompt += 'What variables are investigated? '
        prompt += 'Desribe the methology. '
        prompt += 'Give some related literature. '

        output = get_reply(prompt)
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
