import argparse
from preprocess_doc import embed_doc
from models import load_retrieval_model, load_inference_model
from inference import answer_question, get_relevant_chunks


if __name__ == "__main__":
    # Load the retrieval model
    print("Loading retrieval model... \n")
    retrieval_model = load_retrieval_model()
    # Load the inference model
    print("Loading inference model...\n")
    inference_tokenizer, inference_model = load_inference_model()
    print("Models loaded successfully!\n")

    args = argparse.ArgumentParser()
    args.add_argument("--doc_path", type=str, default="data/ivory_coast.txt")
    args = args.parse_args()

    # Load the document
    print("Embedding the document...\n")
    chunk_embeddings, chunks = embed_doc(args.doc_path, retrieval_model)
    print("Document embedded successfully!\n")

    # After question is asked   
    while True:
        question = input("Ask a question: ")
        print('\n')
        if question.lower() == "exit":
            break
        # Retrieve the most relevant chunks
        retrieved_chunks = get_relevant_chunks(retrieval_model, chunk_embeddings, chunks, question)
        # Answer the question
        answer, context = answer_question(inference_tokenizer, inference_model, retrieved_chunks, question)
        print("Found context:", context.strip().strip('\n'))
        print('\n')
        # well formatted answer
        answer = answer.split('Answer:')
        answer = " ".join(answer[1:])
        print("<|assistant|>:", answer.strip().strip('\n'))
