import streamlit as st
from recommender import recommend_similar_movies, get_all_titles
from difflib import get_close_matches

st.set_page_config(page_title="🎬 Movie Recommendation System", layout="centered")

st.markdown(
    "<h1 color: #FF4B4B;'>🎬 Movie Recommendation System</h1>",
    unsafe_allow_html=True,
)

with st.container():
    st.subheader("🔍 Search for a Movie")
    user_input = st.text_input("Type part of a movie title", placeholder="e.g. The Matrix (1999)")

    all_titles = get_all_titles()
    suggestions = get_close_matches(user_input.strip().lower(), [t.lower() for t in all_titles], n=5, cutoff=0.4)
    matched_titles = [t for t in all_titles if t.lower() in suggestions]

    selected_title = None
    if matched_titles:
        selected_title = st.selectbox("✅ Closest Matches Found:", matched_titles)
    elif user_input:
        st.warning("⚠️ No close matches found. Try typing more of the title.")

    top_n = st.slider("📌 Number of Recommendations", min_value=3, max_value=20, value=5)

    recommend_btn = st.button("🎯 Recommend")

if recommend_btn and selected_title:
    with st.container():
        st.markdown(f"### 🎞️ Top {top_n} Recommendations for: *{selected_title}*")
        recommendations = recommend_similar_movies(selected_title, top_n)
        if recommendations is not None:
            recommendations.columns = ['🎬 Title', '📂 Genres', '⭐ Avg Rating']
            st.dataframe(
                recommendations.style.format({"⭐ Avg Rating": "{:.2f}"}).set_properties(
                    **{"text-align": "left", "font-size": "16px"}
                ),
                height=400
            )
        else:
            st.error("❌ Movie not found in dataset.")
