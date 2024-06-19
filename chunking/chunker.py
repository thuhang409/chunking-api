from flask import request, jsonify
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter, MarkdownTextSplitter
from langchain_text_splitters import PythonCodeTextSplitter
# from unstructured.partition.pdf import partition_pdf
# from unstructured.staging.base import elements_to_json

def CharacterChunking(text,chunk_size, chunk_overlap):
    """Character Splitting

    Args:
        text (string): the text need to be chunked

    Returns:
        JSON: _description_
    """
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size,
                                          chunk_overlap=chunk_overlap,
                                          separator="", 
                                          strip_whitespace=False)
    texts = text_splitter.create_documents([text])
    string_texts = [texts[i].page_content for i in range(len(texts))]
    return jsonify({'chunks': string_texts})

def RecursiveCharacterChunking(text, chunk_size, chunk_overlap):
    """_summary_

    Args:
        text (_type_): _description_
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                   chunk_overlap=chunk_overlap)
    texts = text_splitter.create_documents([text])
    string_texts = [texts[i].page_content for i in range(len(texts))]
    return jsonify({'chunks': string_texts})


def DocumentSpecificChunkingMarkdown(text, chunk_size):
    # Markdown chunking
    splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
    texts = splitter.create_documents([text])
    string_texts = [texts[i].page_content for i in range(len(texts))]
    return jsonify({'chunks': string_texts})

def DocumentSpecificChunkingPython(text, chunk_size):
    # Python chunking
    splitter = PythonCodeTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = splitter.create_documents([text])
    string_texts = [texts[i].page_content for i in range(len(texts))]
    return jsonify({'chunks': string_texts})

# def DocumentSpecificChunkingPDF(filename):
#     elements = partition_pdf(
#         filename=filename,
        
#         # Unstructured Helpers
#         strategy="hi_res",
#         infer_table_structure=True,
#         model_name="yolox"
#     )
#     return 


def SemanticChunking(text):
    return jsonify({'chunks': "Not implementations"})

def AgentChunking(text):
    return jsonify({'chunks': "Not implementations"})
    