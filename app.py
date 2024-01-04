# Import necessary libraries
import os
import streamlit as st
import google.generativeai as genai 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Google Gemini Chatbot",
    page_icon="🤖"
)

# Check if the Google API key is provided in the sidebar
with st.sidebar:
    if 'GOOGLE_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        api_key = st.secrets['GOOGLE_API_KEY']
    else:
        api_key = st.text_input('Enter Google API Key:', type='password')
        if not (api_key.startswith('AI')):
            st.warning('Please enter your API Key!', icon='⚠️')
        else:
            st.success('Success!', icon='✅')
    os.environ['GOOGLE_API_KEY'] = api_key
    "[Get a Google Gemini API key](https://ai.google.dev/)"
    "[View the source code](https://github.com/wms31/streamlit-gemini-chatbot)"
    "[Check out the blog post!](https://letsaiml.com/create-your-own-ai-chat-using-gemini-for-free/)"

# Set the title and caption for the Streamlit app
st.title("🤖 Google Gemini Chatbot")
st.caption("🚀 A streamlit app powered by Google Gemini")

# Function to convert roles for Streamlit chat display
def convert_role_for_streamlit(role):
    return "assistant" if role == "model" else role

# Initialize Gemini chat history if not present in session state
if "chat" not in st.session_state:
    model = genai.GenerativeModel('gemini-pro')
    st.session_state.chat = model.start_chat(history=[])

# Display chat history and accept user input
for message in st.session_state.chat.history:
    with st.chat_message(convert_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user input and interact with Gemini
user_input = st.chat_input("Ask me anything!")
if user_input:
    st.chat_message("user").markdown(user_input)
    response = st.session_state.chat.send_message(user_input)

    with st.chat_message("assistant"):
        st.markdown(response.text)
