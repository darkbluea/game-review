import streamlit as st
from typing import Sequence, Tuple

st.set_page_config(page_title="review", layout='centered', initial_sidebar_state="collapsed")

def questionRanked(answers: Sequence[dict]):
  st.write(str(answers))

def main():
  questionRanked([{"name":"a"},
                  {"name":"b"}])
if __name__ == '__main__':
  main()
