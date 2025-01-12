# Document-Assistant-Using-RAG

This repository contains the code for a simple document assistant using RAG (Retrieval Augmented Generation) model. Given a text format document, the model can answer questions related to the document by retrieving the relevant information from the document using text embeddings and a cosine similarity metric.

## Files
- `main.py`: The main script to run the document assistant.
- `inference.py`: Contains the code for the inference.
- `models.py`: Contains the code for the Retriever and Generator models.
- `preprocess.py`: Contains the code for preprocessing the text format document.

## Requirements
See `requirements.txt` for the list of required libraries.

## Usage
1. Clone the repository
```bash
git clone
```

2. Install the requirements
```bash
pip install -r requirements.txt
```

3. Run the script
```bash
python main.py --doc_path <doc_path>
```

## Example
```bash
python main.py --doc_path data/india_capital.txt
Enter the question:
What is the capital of India?
Answer: New Delhi
```