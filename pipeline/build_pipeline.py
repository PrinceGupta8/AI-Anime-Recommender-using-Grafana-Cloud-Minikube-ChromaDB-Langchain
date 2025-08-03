from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
load_dotenv()

def Main():
    try:
        loader=AnimeDataLoader(original_data="data/anime_with_synopsis.csv",processed_data="data/anime_updated.csv")
        processed_csv=loader.save_and_load_data()

        vector_builder=VectorStoreBuilder(processed_csv)
        vector_builder.Build_and_save()
    except Exception as e:
        print(e)
    

if __name__=="__main__":
    Main()