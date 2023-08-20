import pandas as pd
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ff77153128fecc44e0000709ee2b9368&language=en-US'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



#Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] #This code compares the title of the movie to the movie that was given in the function it then give us the index of th movie
    distances = similarity[movie_index] #This code is used to make distacnes to the indexes of the similarity matrix
    movies_list = sorted(enumerate(distances),reverse=True, key=lambda x:x[1])[1:6] #Movies are sorted in the the desending order and top 5 movies are stroed in the movieslist

    recomanded_movies = []
    recommanded_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id # It retrieves the movie ID of each recommended movie using the index obtained from movies_list.


        recomanded_movies.append(movies.iloc[i[0]].title) #Title of the movies is stored in the recomanded movies list

        # fetch poster from Api
        recommanded_movies_poster.append(fetch_poster(movie_id)) #poster_URL of the movies is stored in the recomanded movies list fetch_poster retrives the URL
    return recomanded_movies,recommanded_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Select the movie?',
movies['title'].values)

if st.button('Recommend'):
    col1, col2, col3, col4, col5 = st.columns(5)


    names, posters = recommend(selected_movie_name)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])