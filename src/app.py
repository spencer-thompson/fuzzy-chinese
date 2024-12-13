"""
Honors Contract for CS 3270
---

This is the Web User Interface for the Chinese Fuzzy Finder.
"""

import streamlit as st
from pypinyin.contrib.tone_convert import to_tone
from st_keyup import st_keyup

from db import init_db, query

st.set_page_config("Honors Contract", layout="centered")


# with open("style.css", "r") as file:
#     css = file.read()
#
# st.html(f"<style>{css}</style>")

if "db" not in st.session_state:
    init_db()  # initialize database, if not already
    st.session_state.db = True


st.markdown(
    """
    <div style="text-align: center;">
        
    # `Chinese Fuzzy Finder`

    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2)

with left:
    pin = st_keyup(
        "Pinyin",
        value="",
        placeholder="Pinyin",
        debounce=100,
        key="0",
        label_visibility="hidden",
    )

with right:
    dfn = st_keyup(
        "Definition",
        value="",
        placeholder="Definition",
        debounce=100,
        key="1",
        label_visibility="hidden",
    )

style = st.segmented_control(
    "style",
    ["Traditional", "Simplified"],
    default=["Traditional", "Simplified"],
    selection_mode="multi",
    label_visibility="collapsed",
)

st.write("---")

# This is where the magic happens
result = query(f"""
    pinyin LIKE '%{pin.replace(" ", "%") if pin else "%"}%'
    AND definition LIKE '%{dfn.replace(" ", "%") if dfn else "%"}%'
    LIMIT 10
    """)
# wildcard characters, in the front and back, allow fuzzy search

result.sort(key=lambda x: len(x[0]), reverse=True)

for r in result:
    with st.empty():
        if len(style) == 1:
            chars = f"`{r[0]}`" if style[0].startswith("T") else f"`{r[1]}`"
        else:
            chars = f"`{r[0]}` | `{r[1]}`"

        st.markdown(
            f"""
        <div style="text-align: center;">
        
        # {chars}

        ### `{" ".join([to_tone(p) for p in r[2].split()])}`
        
        *{r[3]}*
        
        </div>
        
        ---
        """,
            unsafe_allow_html=True,
        )
