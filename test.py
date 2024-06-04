from flask import Flask, request, jsonify

app = Flask(__name__)

# Path to your text file
file_path = 'test.txt'

@app.route('/read', methods=['GET'])
def read_file():
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({"content": content}), 200
    except Exception as e:
        return str(e), 500

@app.route('/write', methods=['POST'])
def write_file():
    try:
        new_content = request.form['content']
        with open(file_path, 'w') as file:
            file.write(new_content)
        return "File updated successfully", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)



import streamlit as st
import requests

# URL of your Flask server endpoints
read_url = "http://127.0.0.1:5000/read"
write_url = "http://127.0.0.1:5000/write"

# Fetch the file contents from the Flask server
response = requests.get(read_url)

# Check if the request was successful
if response.status_code == 200:
    file_content = response.json()["content"]
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

    # Send the updated content to the Flask server
    save_response = requests.post(write_url, data={"content": updated_content})

    # Check if the save request was successful
    if save_response.status_code == 200:
        st.success("File saved successfully!")
    else:
        st.error("Failed to save the file.")
