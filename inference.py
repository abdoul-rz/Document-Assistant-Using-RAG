import torch
from sentence_transformers import util


def get_relevant_chunks(retrieval_model, chunk_embeddings, chunks, question, k=2):
    """Retrieve the most relevant chunks from a document given a question.

    Args:
        retrieval_model (SentenceTransformer): The retrieval model.
        chunks_embedding (torch.Tensor): The embeddings of the document chunks.
        chunks (List[str]): The document chunks.
        question (str): The question to ask.
        k (int): The number of chunks to retrieve.

    Returns:
        List[str]: The most relevant chunks.
    """
    query_embedding = retrieval_model.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, chunk_embeddings)
    # Retrieve the top-k chunks based on document-query similarity
    if k > len(chunks):
        k = len(chunks)
    top_k = torch.topk(scores, k)  # Retrieve top-5 chunks
    retrieved_chunks = [chunks[idx] for idx in top_k.indices[0]]
    return retrieved_chunks


def answer_question(inference_tokenizer, inference_model, retrieved_chunks, question):
    """Answer a question given the retrieved chunks.

    Args:
        inference_tokenizer (transformers.PreTrainedTokenizer): The tokenizer of the inference model.
        inference_model (transformers.PreTrainedModel): The inference model.
        retrieved_chunks (List[str]): The retrieved chunks.
        question (str): The question to ask.

    Returns:
        str: The answer to the question.
    """
    # Concatenate the retrieved chunks
    context = " ".join(retrieved_chunks)
    # Tokenize the input text
    input_text = f"""Mostly based on the following context and your general knowledge, answer the given question: {context}\nQuestion: {question}"""
    inputs = inference_tokenizer(input_text, return_tensors="pt")
    # Perform the inference
    outputs = inference_model.generate(**inputs, pad_token_id=inference_tokenizer.eos_token_id)
    # Decode the model output
    answer = inference_tokenizer.decode(outputs[0], skip_special_tokens=True)
    # well formatted answer
    answer = answer.replace(context, "").replace(question, "")
    to_delete = "Mostly based on the following context and your general knowledge, answer the given question: \nQuestion:"
    answer = answer.replace(to_delete, "")
    return answer, context