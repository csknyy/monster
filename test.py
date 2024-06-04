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

# Display the content in Streamlit
st.title("Text File Content")
st.text_area("Current File Content", value=file_content, height=300, disabled=True)

# Add a text area for adding new content
new_content = st.text_area("Add New Lines")

# Add a button to save the new content
if st.button("Save Changes"):
    # Combine the old content with the new content
    updated_content = file_content + "\n" + new_content

    # Note: This is a placeholder for the actual save logic, which would require server-side support to update the file.
    # Here, we are just displaying the combined content as an example.
    st.text_area("Updated File Content", value=updated_content, height=300, disabled=True)
    st.success("New lines added successfully!")

# Define the URL of the Flask server endpoint
update_url = "https://coskunyay.com/test.txt"  # Change to your server URL

# Add a text area for adding new content
new_content = st.text_area("Add New Lines")

# Add a button to save the new content
if st.button("Save Changes"):
    # Send the updated content to the Flask server
    response = requests.post(update_url, data={"content": new_content})

    # Check if the update request was successful
    if response.status_code == 200:
        st.success("File updated successfully!")
    else:
        st.error("Failed to update the file.")
