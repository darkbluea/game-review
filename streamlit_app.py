import streamlit as st
from typing import Sequence, Tuple

st.set_page_config(page_title="review", layout='centered', initial_sidebar_state="collapsed")

def questionRanked(Sequence[Tuple[str]]: answers):
  st.write(str(answers))

def main():
  questionRanked(["a", "b"])
if __name__ == '__main__':
  main()
