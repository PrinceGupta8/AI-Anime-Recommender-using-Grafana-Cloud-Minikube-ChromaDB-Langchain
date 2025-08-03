from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import model_name,GROQ_API_KEY


class AnimeRecommendationPipeline:
    def __init__(self, persist_dir="chroma_db"):
        try:
            vector_builder = VectorStoreBuilder(
                csv_path="data/anime_updated.csv",
                persist_dir=persist_dir
            )
            retriever = vector_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever, model_name, GROQ_API_KEY)
        except Exception as e:
            print(f"[ERROR in __init__]: {e}")
            self.recommender = None  # explicitly set to None
    
    def recommend(self, query: str):
        try:
            response = self.recommender.get_recommendation(query=query)
            return response
        except Exception as e:
            print(f"[ERROR in recommend]: {e}")
            return ["⚠️ Failed to generate recommendation."]


    
      
     
