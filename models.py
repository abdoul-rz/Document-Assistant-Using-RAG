from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer


def load_inference_model(model_="tiiuae/Falcon3-1B-Instruct"):
    """
    Load the model and tokenizer from the Hugging Face model hub
    
    Args:
        model_ (str): The name of the model to load
    Returns:
        tokenizer (transformers.PreTrainedTokenizer): The tokenizer of the model
        model (transformers.PreTrainedModel): The model
    """
    tokenizer = AutoTokenizer.from_pretrained(model_)
    model = AutoModelForCausalLM.from_pretrained(model_)
    return tokenizer, model


def load_retrieval_model(model_="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Load the embedding model from the Hugging Face model hub

    Args:
        model_ (str): The name of the model to load
    Returns:
        model (SentenceTransformer): The embedding model
    """
    return SentenceTransformer(model_)