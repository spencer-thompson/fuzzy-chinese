import logging
import pathlib
import shutil

import streamlit as st
from bs4 import BeautifulSoup

NEW_HEAD_ID = "custom-head-tag"


def inject_header():
    """
    Inject HTML and CSS to preload custom fonts, and customize further
    """
    with open("head.html") as file:
        new_head_html = file.read()

    with open("style.css") as styles:
        new_styles = styles.read()

    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    logging.info(f"Editing {index_path}")
    soup = BeautifulSoup(index_path.read_text(), features="lxml")
    if not soup.find(id=NEW_HEAD_ID):  # if cannot find tag
        bck_index = index_path.with_suffix(".bck")
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  # recover from backup
        else:
            shutil.copy(index_path, bck_index)  # keep a backup
        html = str(soup)
        new_html = html.replace("<head>", "<head>\n" + new_head_html)
        new_html = new_html.replace("<title>Streamlit</title>", "<title>Fuzzy Chinese</title>")
        new_html = new_html.replace("</head>", f"<style>{new_styles}</style>\n</head>")
        index_path.write_text(new_html)


if __name__ == "__main__":
    inject_header()
