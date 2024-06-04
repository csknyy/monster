import os
import streamlit as st
from github import Github

# Load GitHub access token from environment variable
token = os.getenv("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")
if not token:
    st.error("GitHub token not found. Please set the 'GITHUB_TOKEN' environment variable.")
    st.stop()

account = Github(token)

organization_name = "csknyy"
repo_name = "monster"
file_path = "update_this.txt"

try:
    organization = account.get_organization(organization_name)
    repo = organization.get_repo(repo_name)

    # Display a text input box and a button in the Streamlit app
    text_input = st.text_input("Enter text to update the file")
    update_button = st.button("Update File")

    # Handle button click event
    if update_button:
        # Perform the file update operation
        new_content = text_input.strip()  # Remove leading/trailing whitespace
        if new_content:
            # Get the current file content
            current_content = repo.get_contents(file_path).decoded_content.decode()

            # Update the file content
            repo.update_file(file_path, "Updated file", new_content, current_content.sha)

            st.success("File updated successfully!")
        else:
            st.warning("Please enter text to update the file")
except Exception as e:
    st.error(f"Failed to connect to GitHub: {str(e)}")
