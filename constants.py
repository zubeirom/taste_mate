import os;
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY=os.getenv("OPENAI_KEY")
WEAVIATE_URL=os.getenv("WEAVIATE_URL")
WEAVIATE_KEY=os.getenv("WEAVIATE_KEY")
GCLOUD_KEY=os.getenv("GCLOUD_KEY")
GCLOUD_PID=os.getenv("GCLOUD_PID")

VOYAGE_KEY=os.getenv("VOYAGE_KEY")

COHERE_KEY=os.getenv("COHERE_KEY")

RECIPES='data/RAW_recipes.csv'

RECIPE_TABLE_NAME='Recipe'