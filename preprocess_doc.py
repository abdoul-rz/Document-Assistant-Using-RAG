import os
import re
import pdfplumber
from docx import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def pdf_to_text(file_path):
    """Convert a PDF file to text.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The text content of the PDF file.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def docx_to_text(file_path):
    """Convert a DOCX file to text.

    Args:
        file_path (str): The path to the DOCX file.

    Returns:
        str: The text content of the DOCX file.
    """
    text = ""
    doc = Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def parse_document(file_path):
    """Parse a document and return its content.

    Args:
        file_path (str): The path to the document.

    Returns:
        str: The content of the document.
    """
    file_ext = os.path.splitext(file_path)[1]
    if file_ext == ".txt":
        with open(file_path, "r", encoding='utf-8') as file:
            return file.read()
    elif file_ext == ".pdf":
        return pdf_to_text(file_path)
    elif file_ext == ".docx":
        return docx_to_text(file_path)
    else:
        raise ValueError("Unsupported file type. Supported types are .txt, .pdf, and .docx.")
    
def preprocess_doc(file_path):
    """Preprocess a document and return its content.

    Args:
        doc_path (str): The path to the document.

    Returns:
        str: The preprocessed content of the document.
    """
    doc_content = parse_document(file_path)
    # Remove special characters
    doc_content = re.sub(r"[^a-zA-Z0-9À-ÿ\s]", "", doc_content)
    # Convert to lowercase
    doc_content = doc_content.lower()
    return doc_content

def split_doc(file_path, chunk_size=1000, chunk_overlap=100):
    """Split a document using a recursive character text splitter.

    Args:
        file_path (str): The path to the document.
        chunk_size (int): The maximum number of characters in each chunk.

    Returns:
        list: A list of text chunks.
    """
    doc_content = preprocess_doc(file_path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_size,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = splitter.split_text(doc_content)
    # save the chunks
    # base_name = os.path.basename(file_path)
    # chunks_path = 'data/' + re.sub(r'\.(txt|pdf|docx)$', '_chunks.txt', base_name)
    # with open(chunks_path, 'w') as f:
    #     for chunk in chunks:
    #         f.write(chunk + '\n')
    return chunks

def embed_doc(file_path, embedding_model):
    """
    Embed the text chunks of a document using a pre-trained SentenceTransformer model.

    Args:
        file_path (str): The path to the document.
    
    Returns:
        torch.Tensor: The embeddings of the text chunks.
        list: The text chunks.
    """
    chunks = split_doc(file_path)
    chunks_embeddings = embedding_model.encode(chunks)
    # save the embeddings
    # base_name = os.path.basename(file_path)
    # chunks_embeddings_path = 'data/' + re.sub(r'\.(txt|pdf|docx)$', '_chunks_embeddings.pt', base_name)
    # torch.save(chunks_embeddings, chunks_embeddings_path)
    return chunks_embeddings, chunks

