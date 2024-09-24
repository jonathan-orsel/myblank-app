import streamlit as st
#import vanna as vn
from vanna.remote import VannaDefault
import pandas as pd
import sqlite3

readme = "./README.md"

montrx_ddl = """CREATE TABLE IF NOT EXISTS montrx_2024 (
	idt VARCHAR(255) NOT NULL,
	dateheure_ges001 TIMESTAMP NOT NULL,
	souscodeevt_ges005 VARCHAR(3) NULL DEFAULT NULL,
	mcc_chp018 VARCHAR(4) NULL DEFAULT NULL,
	mcc_gpa VARCHAR(4) NULL DEFAULT NULL,
	token_chp002 VARCHAR(19) NOT NULL,
	pan_masque VARCHAR(19) NULL DEFAULT NULL,
	contrat_chp042 VARCHAR(15) NULL DEFAULT NULL,
	bnqacq_chp032 VARCHAR(11) NULL DEFAULT NULL,
	montant_chp004 BIGINT NOT NULL,
	devisechp004_chp049 VARCHAR(3) NULL DEFAULT NULL,
	montantdevise_chp006 BIGINT NULL DEFAULT NULL,
	devisechp006_chp051 VARCHAR(3) NULL DEFAULT NULL,
	numautor_chp038 VARCHAR(6) NULL DEFAULT NULL,
	repiso_chp039 VARCHAR(2) NULL DEFAULT NULL,
	statutda VARCHAR(100) NOT NULL,
	libelle_repiso VARCHAR(100) NULL DEFAULT NULL,
	enseigne VARCHAR(40) NULL DEFAULT NULL,
	modelecture_chp022 VARCHAR(3) NULL DEFAULT NULL,
	ert_chp059_200 VARCHAR(2) NOT NULL,
	capaciteterminal_chp047_03 VARCHAR(12) NULL DEFAULT NULL,
	traitementcryptogramme_chp059_301 VARCHAR(4) NULL DEFAULT NULL,
	numtpe_chp041 VARCHAR(8) NULL DEFAULT NULL,
	paysacq_chp019 VARCHAR(3) NULL DEFAULT NULL,
	codetraittement_chp003 VARCHAR(6) NULL DEFAULT NULL,
	version3ds_chp057_0022 VARCHAR(8) NULL DEFAULT NULL,
	paysacceptation_chp059_0205 VARCHAR(3) NULL DEFAULT NULL,
	securisationcommerceelectronique_chp059_0407 VARCHAR(2) NULL DEFAULT NULL,
	resultatarchitecturepaiementsecurise_chp059_0412 VARCHAR(8) NULL DEFAULT NULL,
	identifiantapplicatif_ges003 VARCHAR(20) NULL DEFAULT NULL,
	typecarte VARCHAR(10) NULL DEFAULT NULL,
	codeproduit VARCHAR(6) NULL DEFAULT NULL,
	bnqemt VARCHAR(5) NULL DEFAULT NULL,
	paysemt VARCHAR(5) NULL DEFAULT NULL,
	ispayzen INTEGER NULL DEFAULT NULL,
	ismanuel INTEGER NULL DEFAULT NULL,
	is3ds INTEGER NULL DEFAULT NULL,
	isssl INTEGER NULL DEFAULT NULL,
	isbred INTEGER NULL DEFAULT NULL,
	isapplibt INTEGER NULL DEFAULT NULL,
	istpa INTEGER NULL DEFAULT NULL,
	ispsc INTEGER NULL DEFAULT NULL,
	datetlc TIMESTAMP NULL DEFAULT NULL,
	datecompens TIMESTAMP NULL DEFAULT NULL,
	PRIMARY KEY (idt, dateheure_ges001),
	INDEX montrx_2024_ert_chp059_200_idx (ert_chp059_200),
	INDEX montrx_2024_dateheure_ges001_idx (dateheure_ges001),
	INDEX montrx_2024_datecompens_idx (datecompens)
);"""


def read_readme_file():
    with open(readme, 'r') as file:
        content = file.read()
    return content


@st.cache_resource(ttl=3600)
def setup_vanna():
    vn = VannaDefault(
        model=st.secrets.vanna.model,
        api_key=st.secrets.vanna.api_key
    )
    vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
    return vn

@st.cache_data(show_spinner="Generating sample questions ...")
def generate_questions_cached():
    vn = setup_vanna()
    return vn.generate_questions()


@st.cache_data(show_spinner="Generating SQL query ...")
def generate_sql_cached(question: str):
    vn = setup_vanna()
    return vn.generate_sql(question=question, allow_llm_to_see_data=True)

@st.cache_data(show_spinner="Checking for valid SQL ...")
def is_sql_valid_cached(sql: str):
    vn = setup_vanna()
    return vn.is_sql_valid(sql=sql)

@st.cache_data(show_spinner="Running SQL query ...")
def run_sql_cached(sql: str):
    vn = setup_vanna()
    return vn.run_sql(sql=sql)

@st.cache_data(show_spinner="Checking if we should generate a chart ...")
def should_generate_chart_cached(question, sql, df):
    vn = setup_vanna()
    return vn.should_generate_chart(df=df)

@st.cache_data(show_spinner="Generating Plotly code ...")
def generate_plotly_code_cached(question, sql, df):
    vn = setup_vanna()
    code = vn.generate_plotly_code(question=question, sql=sql, df=df)
    return code


@st.cache_data(show_spinner="Running Plotly code ...")
def generate_plot_cached(code, df):
    vn = setup_vanna()
    return vn.get_plotly_figure(plotly_code=code, df=df)


@st.cache_data(show_spinner="Generating followup questions ...")
def generate_followup_cached(question, sql, df):
    vn = setup_vanna()
    return vn.generate_followup_questions(question=question, sql=sql, df=df)

@st.cache_data(show_spinner="Generating summary ...")
def generate_summary_cached(question, df):
    vn = setup_vanna()
    return vn.generate_summary(question=question, df=df)