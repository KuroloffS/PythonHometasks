import pandas as pd

def analyze_long_movies():
    """
    Analyzes movies over 120 minutes, sorted by director popularity.
    Returns sorted DataFrame or None on error.
    """
    try:
        # Load data with type optimization
        movies = pd.read_csv('movie.csv', usecols=['duration', 'director_facebook_likes', 'movie_title'],
                             dtype={'duration': 'Int16', 'director_facebook_likes': 'Int32'})
        
        # Validate critical columns
        if 'duration' not in movies.columns:
            raise KeyError("Missing 'duration' column in dataset")
            
        # Filter long movies
        long_movies = movies[movies['duration'] > 120]
        if long_movies.empty:
            print("No movies found with duration > 120 minutes")
            return None
            
        # Sort by director popularity
        sorted_movies = long_movies.sort_values('director_facebook_likes', 
                                              ascending=False, 
                                              na_position='last')
        
        # Display results
        print(f"Found {len(sorted_movies)} long movies")
        print("\nTop 5 movies by director popularity:")
        print(sorted_movies[['movie_title', 'duration', 'director_facebook_likes']].head(5).to_string(index=False))
        
        return sorted_movies
        
    except FileNotFoundError:
        print("Error: movie.csv file not found in current directory")
    except KeyError as ke:
        print(f"Data validation error: {ke}")
        if 'movies' in locals():
            print(f"Available columns: {movies.columns.tolist()}")
    except ValueError as ve:
        print(f"Data type error: {ve}\nCheck numeric columns for non-numeric values")
    except Exception as e:
        print(f"Analysis failed: {str(e)}")
    return None

if __name__ == "__main__":
    result = analyze_long_movies()
    if result is not None:
        print("\nFull sorted list available in returned DataFrame")