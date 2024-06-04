import streamlit as st
from github import Github
from access_token import token

token = "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"
account = Github(token)

organization = account.get_organization("csknyy")

repo = organization.get_repo("monster")

file_path = "update_this.txt"

text_input = st.textbox()

update_button = st.button()

if update_button == True:
    repo.update_file(path=file_path)
