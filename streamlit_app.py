import streamlit as st

st.set_page_config(page_title="review", layout='centered', initial_sidebar_state="collapsed")

def questionRanked(answers):
  st.write(str(answers))

def main():
  questionRanked(["a", "b"])
if __name__ == '__main__':
  main()
