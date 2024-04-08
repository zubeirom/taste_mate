import pandas as pd
from constants import RECIPES
import weaviate.classes as wvc
from weaviate.util import generate_uuid5
import utils
import constants

def populate_list(object_list, df):

    for i, row in df.iterrows():
        payload = {
            "recipe_id": str(row["id"]),
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
    
        object_list.append(data_obj)
    
        if len(object_list) >= 3000:
            return object_list
    


def execute():
    df = pd.read_csv(RECIPES)
    
    client = utils.connect_db()
    
    recipeStore = client.collections.get(constants.RECIPE_TABLE_NAME)
    
    raw_list = populate_list([], df)

    chunk_size = 300

    splitted_list = [raw_list[i:i+chunk_size] for i in range(0, len(raw_list), chunk_size)]

    recipe_objects = splitted_list[3]

    print(f"Inserted {len(recipe_objects)} objects.")

    # store recipes
    response = recipeStore.data.insert_many(recipe_objects)

    print(f"Insertion complete with {len(response.all_responses)} objects.")
    print(f"Insertion errors: {len(response.errors)}.")

    client.close()


execute()