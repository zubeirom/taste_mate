import utils
import weaviate.classes as wvc
import constants
import weaviate

client = utils.connect_db()

try: 
    recipes = client.collections.create(
        name = constants.RECIPE_TABLE_NAME,
        vectorizer_config=wvc.config.Configure.Vectorizer.text2vec_openai(),
        generative_config=wvc.config.Configure.Generative.openai(),
        properties=[
            wvc.config.Property(
                name="recipe_id",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="minutes",
                data_type=wvc.config.DataType.INT,
            ),
            wvc.config.Property(
                name="name",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="nutrition",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="steps",
                data_type=wvc.config.DataType.TEXT,
            ),
            wvc.config.Property(
                name="description",
                data_type=wvc.config.DataType.TEXT,
            ),
        ],
    )
except weaviate.exceptions.UnexpectedStatusCodeError as e:
    print("Table exists already. Skipping creation.")
    print(e)
except Exception as e:
    print("An error occurred while creating the table.")
    print(e)
    

client.close()