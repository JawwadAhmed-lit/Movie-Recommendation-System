import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image, ImageOps, ImageDraw
from io import BytesIO


def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=224894ed894d0995436faeb81b30773c&language=en-US')
    data = response.json()
    poster_path = data.get('poster_path', '')
    return "https://image.tmdb.org/t/p/w500/" + poster_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


def add_rounded_corners(image, radius):
    # Create a mask with rounded corners
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, image.size[0], image.size[1]], radius=radius, fill=255)

    # Apply the mask to the image
    rounded_image = Image.new("RGBA", image.size)
    rounded_image.paste(image, (0, 0), mask=mask)

    return rounded_image


moviesList = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(moviesList)
movieTitles = movies['title'].values

st.set_page_config(layout="wide", page_title="Movie Recommendation App")
st.title('Movie Recommendation')

selected_movie_name = st.selectbox('Select a movie', movieTitles)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i, (name, poster) in enumerate(zip(names, posters)):
        with cols[i]:
            response = requests.get(poster)
            img = Image.open(BytesIO(response.content)).convert("RGBA")
            img_with_rounded_corners = add_rounded_corners(img, radius=20)

            # Use HTML and CSS to center the image and title together, no bold font
            st.markdown(f"""
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 10px;">
                    <img src="{poster}" style="border-radius: 15px; width: 150px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                    <p style="text-align:center; font-size:16px; line-height:1.2; color: #333333; margin-top: 8px;">{name}</p>
                </div>
                """, unsafe_allow_html=True)
#made changes
