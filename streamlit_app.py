import streamlit as st
from typing import Sequence, Tuple

st.set_page_config(page_title="review", layout='centered', initial_sidebar_state="collapsed")


class Section():
  def __init__(self):
    st.write(str(type(self)))

class Graphics(Section):
  def __init__(self):
    super(Graphics, self).__init__()
    st.select_slider("question", options=["a",
                                          "b"])

def main():
  st.write("Graphics")
  st.select_slider("question", options=["a",
                                        "b"])


if __name__ == '__main__':
  main()
