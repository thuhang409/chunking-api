import os
import base64
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS
from chunking.chunker import CharacterChunking, RecursiveCharacterChunking, 
import fitz
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/chunk": {"origins": "http://localhost:3000"}})

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

@app.route('/chunk', methods=['POST'])
def chunk_endpoint():
    data = request.get_json()
    file_data = data.get('uploadthing','')
    selected_option = data.get('selectedOption', 0)
    
    if not file_data:
        return jsonify({'error': 'No file data provided'}), 400
    
    # Decode the base64 string and save it as a temporary file
    file_content = base64.b64decode(file_data.split(",")[1])
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_file:
        temp_file.write(file_content)
        temp_file_path = temp_file.name
    
    text = extract_text_from_pdf(temp_file_path)
    os.remove(temp_file_path)  # Remove the file after extracting text
    if selected_option == "CharacterChunking":
        return CharacterChunking(text)

    

if __name__=="__main__":
    app.run(debug=True)