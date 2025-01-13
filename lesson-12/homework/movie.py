import requests
import random

API_KEY = "eb1df15e49e5e5935d5c0fb31b11ac00"  
BASE_URL = "https://api.themoviedb.org/3"

def get_genres():
    """Fetch movie genres from TMDb."""
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    genres = response.json()["genres"]
    return {genre["id"]: genre["name"] for genre in genres}

def get_movies_by_genre(genre_id):
    """Fetch movies from a specific genre."""
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "with_genres": genre_id,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["results"]

def recommend_movie():
    """Recommend a movie based on user-selected genre."""
    genres = get_genres()
    print("Available Genres:")
    for genre_id, genre_name in genres.items():
        print(f"{genre_id}: {genre_name}")

    try:
        genre_id = int(input("Enter the genre ID for your preferred genre: "))
        if genre_id not in genres:
            print("Invalid genre ID. Please try again.")
            return

        movies = get_movies_by_genre(genre_id)
        if not movies:
            print(f"No movies found for the genre: {genres[genre_id]}")
            return

        movie = random.choice(movies)
        print(f"\nWe recommend: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Rating: {movie['vote_average']} / 10")
    except ValueError:
        print("Please enter a valid number.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


recommend_movie()
