# Document-Assistant-Using-RAG

This repository contains the code for a simple document assistant using RAG (Retrieval Augmented Generation) model. Given a text format document, the model can answer questions related to the document by retrieving the relevant information from the document using text embeddings and a cosine similarity metric.

### Prerequisites
Ensure you have the following installed:
- Docker
- Git

## Files
- `main.py`: The main script to run the document assistant.
- `inference.py`: Contains the code for the inference.
- `models.py`: Contains the code for the Retriever and Generator models.
- `preprocess.py`: Contains the code for preprocessing the text format document.

## Usage
1. Clone the repository
```bash
git clone https://github.com/abdoul-rz/Document-Assistant-Using-RAG.git
cd Document-Assistant-Using-RAG
```

2. Build the Docker Image
```bash
docker build -t document-assistant-rag-cli:latest .
```

3. Run the Application
To start the CLI program interactively:
```bash
docker run --rm -it document-assistant-rag-cli:latest python main.py --doc_path data/<document_name>.txt
```

---

## Example Usage

After starting the application with the default parameters, the interactive CLI will prompt you to ask questions based on the embedded document:

```plaintext
Loading retrieval model... 

Loading inference model...

Models loaded successfully!

Ask a question: In which city was there a terrorist attack in Côte d'Ivoire?

Founded context: ...

Answer: Grand-Bassam

Ask a question: exit
```

## Note

- Place the files you intend to use in the `data` directory.