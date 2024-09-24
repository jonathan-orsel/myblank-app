import streamlit as st
import controller as ctrl
from controller import (
    generate_questions_cached,
    generate_sql_cached,
    run_sql_cached,
    generate_plotly_code_cached,
    generate_plot_cached,
    generate_followup_cached,
    should_generate_chart_cached,
    is_sql_valid_cached,
    generate_summary_cached
)

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

#ctrl.setup_vanna()


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


my_question = st.session_state.get("my_question", default=None)

if my_question is None:
    my_question = st.chat_input(
        "Ask me a question about your data",
    )


if my_question:
    user_message = st.chat_message("user")
    user_message.write(f"{my_question}")

    sql = generate_sql_cached(question=my_question)
    if sql:
         st.code(sql, language="sql", line_numbers=True)
      