import streamlit as st
import controller as ctrl




st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

ctrl.setup_agent()


default_questions = [
    "How many messages were sent by each contact?",
    "Show the content of the table messages",
    "How many messages did John Doe received ?"
]

"Example questions :"
all_questions = default_questions

for i, quest in enumerate(all_questions):
    if st.button(quest, key=f"btn_question_exp{i}"):
        st.session_state["my_question"] = quest

question =  st.text_input(
    "Ask a personalized question" , key="my_question"
)



st.toast('bonjour jol')