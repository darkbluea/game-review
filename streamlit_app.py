import streamlit as st
from typing import Sequence, Tuple

st.set_page_config(page_title="review", layout='centered', initial_sidebar_state="collapsed")

def questionRanked(name: str, answers: Sequence[dict]):
  st.write(name)
  st.write(str(answers))
  

def main():
  st.select_slider("question", options=["a",
                                        "b"])
  questionRanked("question",
    [{"name":"a"},
     {"name":"b"}])
if __name__ == '__main__':
  main()
