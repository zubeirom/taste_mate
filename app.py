import constants
import utils
import weaviate.classes as wvc

client = utils.connect_db() 

try:
    recipes = client.collections.get(constants.RECIPE_TABLE_NAME)
    response = recipes.query.fetch_objects()

    print(f"Found {len(response.objects)} recipes.")


    for query in ["Tagliatelle"]:  # Loop through multiple query terms
        response = recipes.query.near_text(  # Vector search
            query=query,
            limit=2,
            return_metadata=wvc.query.MetadataQuery(distance=True),
        )
    
        print(f"===== Search results for '{query}'. =====")  # Print the query term
        for o in response.objects:
            print(o.properties["name"])            # Show which titles were found
            print(o.properties["description"])      # Show the description
            print(f"{o.metadata.distance:.3f}\n")   # What was the distance?
finally:
    client.close()


