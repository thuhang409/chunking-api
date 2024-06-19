import os
import base64
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS
from chunking.chunker import CharacterChunking, RecursiveCharacterChunking, DocumentSpecificChunkingMarkdown
import fitz
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, resources={r"/chunk": {"origins": "http://localhost:3000"}})
app.config['UPLOAD_FOLDER'] = ""
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

@app.route('/chunk', methods=['POST'])
def chunk_endpoint():
    '''
    print(request.files.form)
    print(request.files)
    if 'uploadthing' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['uploadthing']
    selected_option = request.form['selectedOption']
    chunk_size = int(request.form['chunk_size'])
    chunk_overlap = int(request.form['chunk_overlap'])
    
    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    if filename.lower().endswith('.docx'):
        text = read_docx(file_path)
    elif filename.lower().endswith('.pdf'):
        text = read_pdf(file_path)
    print(text)  
    
    '''
    data = request.get_json()
    print(data)
    file_data = data.get('file', '')
    print(file_data)
    chunk_size = data.get('chunk_size', 1000)
    chunk_overlap = data.get('chunk_overlap', 200)
    selected_option = data.get('selected_option', 'chunks')

    if not file_data:
        return jsonify({'error': 'No file data provided'}), 400

    # Decode the base64 string and save it as a temporary file
    file_content = base64.b64decode(file_data.split(",")[1])
    file_ext = '.pdf' if 'pdf' in file_data.split(",")[0] else '.docx'
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as temp_file:
        temp_file.write(file_content)
        temp_file_path = temp_file.name

    if file_ext == '.pdf':
        text = read_pdf(temp_file_path)
    elif file_ext == '.docx':
        text = read_docx(temp_file_path)
    else:
        return jsonify({'error': 'Unsupported file type'}), 400

    os.remove(temp_fileW_path)
    
    if selected_option == "CharacterChunking":
        return CharacterChunking(text, chunk_size, chunk_overlap)
    elif selected_option == "RecursionCharacterChunking":
        return RecursiveCharacterChunking(text, chunk_size, chunk_overlap)
    elif selected_option == "DocumentSpecificChunking":
        return DocumentSpecificChunking(text, chunk_size)
    else:
        return jsonify({"chunks":[]})


if __name__=="__main__":
    app.run(debug=True)