import streamlit as st
from typing import Sequence, Tuple

st.set_page_config(page_title="review", layout='centered', initial_sidebar_state="collapsed")


def main():
  st.select_slider("question", options=["a",
                                        "b"])


if __name__ == '__main__':
  main()
