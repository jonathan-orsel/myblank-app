import streamlit as st
import time
import controller as ctrl


st.set_page_config(
    page_title="MYAPPPPPP",
    page_icon="🇵🇫",
)

def main():
    """Main."""
    with st.spinner('Setting up..'):
        time.sleep(5)

    st.markdown(
        ctrl.read_readme_file()
    )


if __name__ == "__main__":
    main()