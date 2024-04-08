import os
from dotenv import load_dotenv
import weaviate
from weaviate.client import WeaviateClient
from constants import WEAVIATE_URL, WEAVIATE_KEY, OPENAI_KEY

load_dotenv()

def connect_db() -> WeaviateClient:

    client = weaviate.connect_to_wcs(
        cluster_url=WEAVIATE_URL,
        auth_credentials=weaviate.auth.AuthApiKey(WEAVIATE_KEY),
        headers={"X-OpenAI-Api-Key": OPENAI_KEY}
    )

    return client

