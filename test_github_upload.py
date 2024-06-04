from github import Github
import os

API_token = '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'
username = 'csknyy@hotmail.com'
password = 'At@han2014'

g = Github(login_or_token=username,password=password)
#g = Github(API_token)
repo = g.get_repo("csknyy/monster", lazy=False)
#issues = repo.get_issues(state="open")

rate_limit = g.get_rate_limit()
core_rate_limit = rate_limit.core

if core_rate_limit.remaining == 0:
    st.error(f"Rate limit exceeded. Reset at {core_rate_limit.reset}")
else:
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
