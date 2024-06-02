import streamlit as st

# Page Configuration
st.set_page_config(page_title="Página principal", layout="wide")

# Add CSS styles
st.markdown("""
    <style>
        .main {
            margin: 18px;
            border-radius: 4px;
        }
        .pva-embedded-web-chat {
            background-color: #484644;
            border: 1px solid #FFFFFF;
            border-radius: 50%;
            box-shadow: rgba(0, 0, 0, 0.13) 0px 3.2px 7.2px, rgba(0, 0, 0, 0.11) 0px 0.6px 1.8px;
            display: block;
            height: 44px;
            width: 44px;
        }
        .pva-embedded-web-chat-widget-icon {
            display: block;
            height: 23px;
            margin: 11.5px 10.5px;
            width: 21px;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("Página principal")

# Placeholder for the chatbot widget
st.markdown("""
    <div class="pva-embedded-web-chat">
        <img class="pva-embedded-web-chat-widget-icon" src="path_to_icon_image" alt="Chatbot Icon">
    </div>
""", unsafe_allow_html=True)

# Add more components as needed
st.header("Welcome to the main page")
st.write("This is an example page created with Streamlit.")

# You can add more Streamlit components to replicate the functionalities

if __name__ == "__main__":
    st.write("Streamlit app running...")

# To run this app, use the command: streamlit run app.py
