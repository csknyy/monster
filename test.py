import streamlit as st
import requests

# Define the URL of the text file
url = "https://coskunyay.com/test.txt"

# Fetch the file contents from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the text content of the file
    file_content = response.text
else:
    file_content = "Failed to fetch the file."

# Display the content in Streamlit and provide an editable text area
st.title("Edit Text File Content")
edited_content = st.text_area("File Content", value=file_content, height=300)

# Add a button to save the edited content
if st.button("Save Changes"):
    # Send the edited content back to the server
    save_response = requests.post(url, data=edited_content)
    
    # Check if the save request was successful
    if save_response.status_code == 200:
        st.success("File saved successfully!")
    else:
        st.error("Failed to save the file.")
