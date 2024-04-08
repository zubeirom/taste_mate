import pandas as pd
from constants import RECIPES
import weaviate.classes as wvc
from weaviate.util import generate_uuid5
import utils
import constants

df = pd.read_csv(RECIPES)

client = utils.connect_db()
recipeStore = client.collections.get(constants.RECIPE_TABLE_NAME)

recipe_objects = list()

for i, row in df.iterrows():
    payload = {
        "recipe_id": row["id"],
        "minutes": row["minutes"],
        "name": row["name"],
        "nutrition": row["nutrition"],
        "steps": row["steps"],
        "description": row["description"],
    }

    # Insert payload into database
    data_obj = wvc.data.DataObject(
        properties=payload,
        uuid=generate_uuid5(payload["recipe_id"])
    )

    recipe_objects.append(data_obj)

# store recipes
response = recipeStore.data.insert_many(recipe_objects)

print(f"Insertion complete with {len(response.all_responses)} objects.")
print(f"Insertion errors: {len(response.errors)}.")

client.close()