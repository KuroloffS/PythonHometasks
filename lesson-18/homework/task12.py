import pandas as pd

def analyze_movie_data():
    """
    Analyzes movie data to find:
    1. Director with highest total Facebook likes
    2. 5 longest movies with their directors
    """
    try:
        # Load data with relevant columns and type optimization
        movies = pd.read_csv(
            'movie.csv',
            usecols=['director_name', 'director_facebook_likes', 'movie_title', 'duration'],
            dtype={
                'director_facebook_likes': 'Int32',
                'duration': 'Int16'
            }
        )
        
        # Clean data
        movies = movies.dropna(subset=['director_name']).copy()
        
        # 1. Find director with highest total Facebook likes
        director_likes = movies.groupby('director_name')['director_facebook_likes'].sum()
        top_director = director_likes.idxmax()
        max_likes = director_likes.max()
        
        # 2. Find 5 longest movies
        longest_movies = movies.sort_values('duration', ascending=False).head(5)
        longest_movies = longest_movies[['movie_title', 'duration', 'director_name']]
        
        # Display results
        print(f"Director with Highest Facebook Likes: {top_director} ({max_likes:,} likes)")
        print("\n5 Longest Movies:")
        print(longest_movies.to_string(index=False, header=True))
        
        return top_director, longest_movies
    
    except FileNotFoundError:
        print("Error: movie.csv file not found in current directory")
    except KeyError as e:
        print(f"Missing required column: {e}")
        if 'movies' in locals():
            print("Available columns:", movies.columns.tolist())
    except ValueError as e:
        print(f"Data validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    return None, None

if __name__ == "__main__":
    top_director, longest_movies = analyze_movie_data()
    if top_director:
        print("\nAdditional Stats:")
        print(f"Total directors analyzed: {len(pd.read_csv('movie.csv')['director_name'].unique()):,}")