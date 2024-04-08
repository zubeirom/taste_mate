import weaviate
from weaviate.client import WeaviateClient
import constants

def connect_db() -> WeaviateClient:
    client = weaviate.connect_to_wcs(
        cluster_url=constants.WEAVIATE_URL,
        auth_credentials=weaviate.auth.AuthApiKey(constants.WEAVIATE_KEY),
        headers={
            "X-Cohere-Api-Key": constants.COHERE_KEY,
            "X-VoyageAI-Api-Key": constants.VOYAGE_KEY
        }
    )

    return client
