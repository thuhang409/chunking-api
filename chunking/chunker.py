from flask import request, jsonify
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter, MarkdownTextSplitter

def CharacterChunking(text):
    """Character Splitting

    Args:
        text (string): the text need to be chunked

    Returns:
        JSON: _description_
    """
    text_splitter = CharacterTextSplitter(chunk_size = 10, 
                                          chunk_overlap=0, 
                                          separator="\n", 
                                          strip_whitespace=False)
    texts = text_splitter.create_documents([text])
    string_texts = [texts[i].page_content for i in range(len(texts))]
    return jsonify({'chunks': string_texts})

def RecursiveCharacterChunking(text):
    """_summary_

    Args:
        text (_type_): _description_
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 35,
                                                   chunk_overlap=0)
    texts = text_splitter.create_documents([text])
    string_texts = [texts[i].page_content for i in range(len(texts))]
    return jsonify({'chunks': string_texts})


def DocumentSpecificChunking(text):
    splitter = MarkdownTextSplitter()
    texts = text_splitter.create_documents([text])
    string_texts = [texts[i].page_content for i in range(len(texts))]

    return jsonify({'chunks': "Not implementations"})

def SemanticChunking(text):
    return jsonify({'chunks': "Not implementations"})

def AgentChunking(text):
    return jsonify({'chunks': "Not implementations"})
    