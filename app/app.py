import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender",layout="wide")

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline=init_pipeline()
st.title("Anime Recommender System")

query=st.text_input("Enter your anime prefernces eg. : light hearted anime with school settings")
if query:
    response=pipeline.recommend(query=query)
    st.success(response)