import streamlit as st 
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage



# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}



#st.session_state -> dict -> 

# Initialize message history if it doesn't exist
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []  # This creates a list to store message dictionaries

# {'role':'user','content':'HI'}
#{'role':'assistant','content':'Hi Hello'}


st.set_page_config(page_title = "Chat History with Streamlit")
st.title("Chat History ")
#Loading the Conversion History
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


user_input = st.chat_input("Enter any Message")

if user_input:
    # Display user message
    st.session_state['message_history'].append(
        {'role':'user',
        'content':user_input
        })
    # Display user message
    with st.chat_message('user'):
        st.text(user_input)


    # 2. Add ASSISTANT response to history
    response = chatbot.invoke({'messages':[HumanMessage(content = user_input)]},config = CONFIG)
    ai_message = response['messages'][-1].content
    st.session_state['message_history'].append(
        {'role':'assistant','content':ai_message
        })
    with st.chat_message('assistant'):
        st.text(ai_message)
        

