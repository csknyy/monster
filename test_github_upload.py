import base64
import requests
import streamlit as st
from github import Github

# GitHub credentials
token = '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'
user = 'csknyy'
repo_name = 'monster'
path_to_file = 'update_this.csv'

# Create GitHub instance
g = Github(token)

try:
    repo = g.get_repo(f'{user}/{repo_name}')

    # Display a text input box and a button in the Streamlit app
    st.title("GitHub File Updater")
    input_text = st.text_area("Enter text to update the file")
    update_button = st.button("Update File")

    # Handle button click event
    if update_button:
        # Get the current file content
        file = repo.get_contents(path_to_file)
        current_content = base64.b64decode(file.content).decode('utf-8')

        # Update the file content
        new_content = current_content + '\n' + input_text
        repo.update_file(path_to_file, 'Updated file', new_content, file.sha)

        st.success("File updated successfully!")

except Exception as e:
    st.error(f"Failed to connect to GitHub: {str(e)}")
