import pandas as pd

def load_movie_data():
    """
    Loads movie.csv into a DataFrame and displays a random sample of up to 10 rows.
    Returns DataFrame on success, empty DataFrame on failure.
    """
    file_path = 'movie.csv'
    movie_df = pd.DataFrame()

    try:
        # Load CSV with optimized parsing and memory management
        movie_df = pd.read_csv(file_path, engine='python', on_bad_lines='warn')
        
        # Display appropriate sample based on data size
        if movie_df.empty:
            print("Warning: Dataset contains no records")
        else:
            sample_size = min(10, len(movie_df))
            print(f"\nRandom sample of {sample_size} rows:")
            print(movie_df.sample(sample_size, random_state=42))  # Seed for reproducibility
            
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except pd.errors.EmptyDataError:
        print("Error: CSV file contains no data")
    except pd.errors.ParserError as pe:
        print(f"CSV parsing error: {pe}\nCheck file format or encoding")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        return movie_df

if __name__ == "__main__":
    df_movies = load_movie_data()
    if not df_movies.empty:
        print("\nDataset summary:")
        print(f"Total movies: {len(df_movies)}")
        print(f"Columns: {list(df_movies.columns)}")