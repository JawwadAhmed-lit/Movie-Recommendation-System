# Movie Recommendation System using Content-Based Filtering

## Project Overview

This repository contains a complete implementation of a Content-Based Movie Recommendation System. The system is designed to recommend movies based on their content features such as genres, keywords, cast, and crew. The project is built with Python and leverages machine learning libraries to preprocess the data, build a content-based filtering model, and deploy it as a web application using Streamlit.

## Features

- **Data Preprocessing**: The movie dataset is cleaned and processed, focusing on features relevant for content-based recommendations.
- **Content-Based Recommendation**: The recommendation engine suggests movies similar to a user-input movie by calculating the cosine similarity between movie feature vectors.
- **Web Application**: The model is deployed using a web interface built with Streamlit, allowing users to input a movie title and receive recommendations in real-time.

## Tech Stack

- **Programming Language**: Python

- **Libraries/Frameworks**:
  - Pandas (Data manipulation)
  - Scikit-learn (TF-IDF vectorization and cosine similarity computation)
  - NLTK (Text preprocessing)
  - Streamlit (Web application)
  - Pickle (Saving/loading models and data)

## Dataset

The dataset used for this project is the TMDB 5000 Movie Dataset. It includes detailed metadata for over 5,000 movies, with features such as movie budget, genres, keywords, cast, crew, and more.

- **Data Source**: [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The dataset has been split into two CSV files:

- `movies.csv`: Contains basic movie metadata.
- `credits.csv`: Contains cast and crew information for each movie.

### Key Features Used:

- Genres
- Keywords
- Cast
- Crew (Director)

## Recommendation System

### Content-Based Filtering:

The recommendation engine uses a Content-Based Filtering approach. The model creates a TF-IDF vector for each movie based on its content features and calculates the Cosine Similarity between the vectors to find similar movies.

- **TF-IDF Vectorization**: Transforms text data (genres, keywords, cast, and crew) into numerical vectors.
- **Cosine Similarity**: Measures the cosine of the angle between two vectors to determine how similar they are. Values closer to 1 indicate more similarity.

### Steps:

1. **Data Preprocessing**: Remove unwanted columns, process text data, and clean missing values.
2. **Feature Extraction**: Create vectors from the movie's content using TF-IDF.
3. **Similarity Calculation**: Compute pairwise cosine similarities between all movie vectors.
4. **Recommendation**: For a given movie, return the top 5 most similar movies.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and create a pull request. Any bug fixes, feature additions, or improvements are appreciated.

### Contributors

- **Raunak Sarmacharya**
- **Jawwad Ahmed**
