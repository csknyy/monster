#####
#I9AZTHT82B4K6NURHWEIB635UHX4WS9S
#####

from flask import Flask, request, jsonify

app = Flask(__name__)

# Path to your text file
file_path = 'test.txt'

# Function to read the file
def read_file():
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Function to write to the file
def write_file(new_content):
    with open(file_path, 'a') as file:
        file.write('\n' + new_content)

@app.route('/read', methods=['GET'])
def get_content():
    content = read_file()
    return jsonify({"content": content})

@app.route('/write', methods=['POST'])
def add_content():
    new_content = request.json.get('new_content')
    if new_content:
        write_file(new_content)
        return jsonify({"message": "New lines added successfully"}), 200
    else:
        return jsonify({"error": "No content provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)


import streamlit as st
import requests

# Define the URL of the Flask server endpoints
read_url = "https://coskunyay.com/read"
write_url = "https://coskunyay.com/write"

# Fetch the file contents from the Flask server
response = requests.get(read_url)

# Check if the request was successful
if response.status_code == 200:
    file_content = response.json()["content"]
else:
    file_content = "Failed to fetch the file."

# Display the current content in Streamlit
st.title("Text File Content")
st.text_area("Current File Content", value=file_content, height=300, disabled=True)

# Add a text area for adding new content
new_content = st.text_area("Add New Lines")

# Add a button to save the new content
if st.button("Save Changes"):
    # Send the new content to the Flask server
    response = requests.post(write_url, json={"new_content": new_content})

    # Check if the update request was successful
    if response.status_code == 200:
        st.success("New lines added successfully!")
    else:
        st.error("Failed to add new lines.")
