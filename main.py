#%% LIBRARY
from openai import OpenAI
import streamlit as st

#%% SIDER BAR INFOR
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key",
                                   key="API key",
                                   type="password")
    

#%% MAIN SECTION
st.title("Ms. Hoai's Teaching Assistant")
st.caption("Powered by Artificial Intelligent")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
        ]
    
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your key")
        st.stop()
        
    client = OpenAI(api_key=openai_api_key)
    
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
        )
    
    st.chat_message("user").write(prompt)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = st.session_state.messages  # input full chat history
        )
    
    msg = response.choices[0].message.content
    
    st.session_state.messages.append(
        {"role": "assistant", "content": msg}
        )
    
    st.chat_message("assistant").write(msg)
    