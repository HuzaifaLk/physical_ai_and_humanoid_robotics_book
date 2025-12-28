import typer
import os
import logging
from dotenv import load_dotenv

# Load .env from this backend folder so environment vars are available
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

print(os.getenv("QDRANT_URL"))

# from ingestion import (
#     crawl_and_extract_content,
#     chunk_text,
#     generate_embeddings,
#     get_qdrant_client,
#     store_embeddings_in_qdrant
# )

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = typer.Typer()

@app.command()
def main(url: str = typer.Argument(..., help="The root URL of the Docusaurus book to ingest.")):
    """
    Ingests content from a Docusaurus book URL, chunks it,
    generates embeddings, and stores them in Qdrant.
    """
    load_dotenv() # Load environment variables from .env file

    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    cohere_api_key = os.getenv("COHERE_API_KEY")

    if not qdrant_url:
        logging.error("QDRANT_URL environment variable not set.")
        raise typer.Exit(code=1)
    if not qdrant_api_key:
        logging.error("QDRANT_API_KEY environment variable not set.")
        raise typer.Exit(code=1)
    if not cohere_api_key:
        logging.error("COHERE_API_KEY environment variable not set.")
        raise typer.Exit(code=1)

    logging.info(f"Starting ingestion for URL: {url}")
    logging.info(f"Qdrant URL: {qdrant_url}")
    logging.info(f"Cohere API Key (first 5 chars): {cohere_api_key[:5]}*****")

    # Orchestration of User Story 1: Content Extraction
    # extracted_content = crawl_and_extract_content(url)
    # logging.info(f"Extracted {len(extracted_content)} content items.")
    
    # Orchestration of User Story 2: Content Chunking
    # all_chunks = []
    # for item in extracted_content:
    #     chunks = chunk_text(item["text"])
    #     for i, chunk in enumerate(chunks):
    #         all_chunks.append({
    #             "url": item["url"],
    #             "title": item["title"],
    #             "text_chunk": chunk,
    #             "chunk_id": f"{item['url']}-{i}" # Simple ID for now
    #         })
    # logging.info(f"Generated {len(all_chunks)} text chunks.")

    # Orchestration of User Story 2: Embedding Generation
    # if all_chunks:
    #     texts_to_embed = [chunk["text_chunk"] for chunk in all_chunks]
    #     embeddings = generate_embeddings(texts_to_embed, cohere_api_key)
    #     if embeddings:
    #         logging.info(f"Generated {len(embeddings)} embeddings.")
    #         # Attach embeddings to chunks
    #         for i, embedding in enumerate(embeddings):
    #             all_chunks[i]["embedding"] = embedding
    #     else:
    #         logging.error("Failed to generate embeddings.")
    #         raise typer.Exit(code=1)
    # else:
    #     logging.warning("No chunks to embed.")

    # Orchestration of User Story 3: Qdrant Client Initialization
    # COLLECTION_NAME = "docusaurus_book" # Define a constant for the collection name
    # VECTOR_SIZE = 1024 # Cohere embed-english-v3.0 typically has 1024 dimensions
    # 
    # qdrant_client = get_qdrant_client(qdrant_url, qdrant_api_key, COLLECTION_NAME, VECTOR_SIZE)
    # logging.info(f"Qdrant client initialized for collection '{COLLECTION_NAME}'.")

    # Orchestration of User Story 3: Storing Embeddings
    # if all_chunks:
    #     store_embeddings_in_qdrant(qdrant_client, COLLECTION_NAME, all_chunks)
    #     logging.info("Embeddings successfully stored in Qdrant.")
    # else:
    #     logging.warning("No chunks with embeddings to store.")

if __name__ == "__main__":
    app()


from ingestion import (
    crawl_and_extract_content,
    import typer
    import os
    import logging
    from dotenv import load_dotenv

    # Load .env from this backend folder so environment vars are available
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

    print(os.getenv("QDRANT_URL"))

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = typer.Typer()

@app.command()
def main(url: str = typer.Argument(..., help="The root URL of the Docusaurus book to ingest.")):
    """
    Ingests content from a Docusaurus book URL, chunks it,
    generates embeddings, and stores them in Qdrant.
    """
    load_dotenv() # Load environment variables from .env file

    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    cohere_api_key = os.getenv("COHERE_API_KEY")

    if not qdrant_url:
        logging.error("QDRANT_URL environment variable not set.")
        raise typer.Exit(code=1)
    if not qdrant_api_key:
        logging.error("QDRANT_API_KEY environment variable not set.")
        raise typer.Exit(code=1)
    if not cohere_api_key:
        logging.error("COHERE_API_KEY environment variable not set.")
        raise typer.Exit(code=1)

    logging.info(f"Starting ingestion for URL: {url}")
    logging.info(f"Qdrant URL: {qdrant_url}")
    logging.info(f"Cohere API Key (first 5 chars): {cohere_api_key[:5]}*****")

    # Orchestration of User Story 1: Content Extraction
    extracted_content = crawl_and_extract_content(url)
    logging.info(f"Extracted {len(extracted_content)} content items.")
    
    # Orchestration of User Story 2: Content Chunking
    all_chunks = []
    for item in extracted_content:
        chunks = chunk_text(item["text"])
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "url": item["url"],
                "title": item["title"],
                "text_chunk": chunk,
                "chunk_id": f"{item['url']}-{i}" # Simple ID for now
            })
    logging.info(f"Generated {len(all_chunks)} text chunks.")

    # Orchestration of User Story 2: Embedding Generation
    if all_chunks:
        texts_to_embed = [chunk["text_chunk"] for chunk in all_chunks]
        embeddings = generate_embeddings(texts_to_embed, cohere_api_key)
        if embeddings:
            logging.info(f"Generated {len(embeddings)} embeddings.")
            # Attach embeddings to chunks
            for i, embedding in enumerate(embeddings):
                all_chunks[i]["embedding"] = embedding
        else:
            logging.error("Failed to generate embeddings.")
            raise typer.Exit(code=1)
    else:
        logging.warning("No chunks to embed.")

    # Orchestration of User Story 3: Qdrant Client Initialization
    COLLECTION_NAME = "docusaurus_book" # Define a constant for the collection name
    VECTOR_SIZE = 1024 # Cohere embed-english-v3.0 typically has 1024 dimensions
    
    qdrant_client = get_qdrant_client(qdrant_url, qdrant_api_key, COLLECTION_NAME, VECTOR_SIZE)
    logging.info(f"Qdrant client initialized for collection '{COLLECTION_NAME}'.")

    # Orchestration of User Story 3: Storing Embeddings
    if all_chunks:
        store_embeddings_in_qdrant(qdrant_client, COLLECTION_NAME, all_chunks)
        logging.info("Embeddings successfully stored in Qdrant.")
    else:
        logging.warning("No chunks with embeddings to store.")

if __name__ == "__main__":
    app()