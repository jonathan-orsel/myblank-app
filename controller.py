import streamlit as st
import vanna as vn


readme = "./README.md"

def read_readme_file():
    with open(readme, 'r') as file:
        content = file.read()
    return content


def setup_agent():
    """Return vanna agent."""
    vn.set_api_key(st.secrets.vanna.api_key)
    vn.set_model(st.secrets.vanna.model)

    vn.run_sql = run_sql
    vn.run_sql_is_set = True

    st.toast('Vanna Agent [OK]')



def get_db_conn():
    db_connexion = sqlite3.connect(
       "dump.sql", check_same_thread=False
    )
    return db_connexion
