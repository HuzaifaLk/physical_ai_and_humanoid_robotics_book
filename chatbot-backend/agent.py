import os
from dotenv import load_dotenv
import cohere
import openai
from qdrant_client import QdrantClient, models

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize clients
cohere_client = cohere.Client(COHERE_API_KEY)
openai.api_key = OPENAI_API_KEY
qdrant_client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def retrieve_context(query: str, collection_name = "physical-ai-and-humanoid-robotics-book"):
    """
    Retrieves context from the Qdrant vector database based on the user's query.
    """
    if not all([QDRANT_URL, QDRANT_API_KEY, COHERE_API_KEY]):
        raise ValueError("Qdrant or Cohere API keys/URL are not set in environment variables.")

    try:
        # Embed the query using Cohere
        query_embedding = cohere_client.embed(
            texts=[query],
            model="embed-english-v3.0",
            input_type="search_query"
        ).embeddings[0]

        # Search for relevant vectors in Qdrant
        search_result = qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=5,
            with_payload=True
        )

        # Extract context from payload
        context = [hit.payload['text'] for hit in search_result]
        return context

    except Exception as e:
        print(f"An error occurred during context retrieval: {e}")
        return None

def generate_grounded_answer(query: str, context: list):
    """
    Generates an answer using the OpenAI API based on the provided context.
    """
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")

    if not context:
        return "I'm sorry, I couldn't find any relevant information to answer your question. Please try rephrasing it."

    try:
        # Construct the prompt for the language model
        system_prompt = (
            "You are an expert assistant for the 'Physical AI & Humanoid Robotics' book. "
            "Answer the user's question based ONLY on the following provided context. "
            "If the context does not contain the answer, state that you cannot answer."
        )
        
        user_prompt = f"Context:\n{''.join(context)}\n\nQuestion: {query}"

        # Call the OpenAI API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"An error occurred during answer generation: {e}")
        raise

def get_answer(question: str):
    """
    Main orchestration function to get an answer for a given question.
    """
    print(f"Retrieving context for question: '{question}'")
    context = retrieve_context(question)
    
    print("Generating grounded answer...")
    answer = generate_grounded_answer(question, context)
    
    print("Answer generation complete.")
    return answer

if __name__ == '__main__':
    # Example usage for testing
    test_question = "What is ROS 2?"
    answer = get_answer(test_question)
    print(f"\nQuestion: {test_question}")
    print(f"Answer: {answer}")
