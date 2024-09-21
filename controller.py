import streamlit as st
#import vanna as vn
from vanna.remote import VannaDefault
import pandas as pd
import sqlite3

readme = "./README.md"

def read_readme_file():
    with open(readme, 'r') as file:
        content = file.read()
    return content


@st.cache_data(show_spinner="Running sql query..")
def run_sql(sql: str) -> pd.DataFrame:
    """Take in SQL query as string and return DataFrame."""

    conn = get_db_conn()

    df = pd.read_sql_query(
        sql,
        conn
    )
    return df

""" Please switch to the following method for initializing Vanna: 
from vanna.remote import VannaDefault
api_key = # Your API key from https://vanna.ai/account/profile 
vanna_model_name = # Your model name from https://vanna.ai/account/profile 
vn = VannaDefault(model=vanna_model_name, api_key=api_key)
"""

def setup_agent():
    """Return vanna agent."""
    vn = VannaDefault(
        model=st.secrets.vanna.model,
        api_key=st.secrets.vanna.api_key
        )
    

    vn.run_sql = run_sql
    vn.run_sql_is_set = True

    st.toast('Vanna Agent [OK]')



def get_db_conn():
    db_connexion = sqlite3.connect("dump.sql", check_same_thread=False )
    return db_connexion
