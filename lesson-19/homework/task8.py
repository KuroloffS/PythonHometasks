import pandas as pd

def classify_duration(duration: float) -> str:
    """Classify movie duration into standardized categories.
    
    Args:
        duration: Movie length in minutes
        
    Returns:
        'Short' (<60), 'Medium' (60-120), 'Long' (>120)
        'Invalid' for negative/non-numeric values
        'Unknown' for missing values
    """
    try:
        if pd.isna(duration):
            return 'Unknown'
        if duration < 0:
            return 'Invalid'
        return ('Short' if duration < 60 else
                'Medium' if duration <= 120 else 
                'Long')
    except TypeError:
        return 'Invalid'

def process_movie_durations():
    """Analyze movie durations with classification system.
    
    Returns:
        pd.DataFrame: Movies with duration classifications
        None: If errors occur
        
    Requires:
        - movie.csv in working directory
    """
    try:
        # Load data with optimized settings
        df = pd.read_csv(
            'movie.csv',
            usecols=['movie_title', 'duration'],
            dtype={'duration': 'Int16'}
        )
        
        # Validate dataset structure
        if df.empty:
            raise ValueError("Dataset contains no movie records")
            
        required_columns = ['movie_title', 'duration']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing required columns: {missing_columns}")
        
        # Create classification column
        df['Duration_Class'] = df['duration'].apply(classify_duration)
        
        # Analyze results
        print("🎥 Movie Duration Classification Distribution:")
        print(df['Duration_Class'].value_counts().to_string())
        
        # Save results
        df.to_csv('classified_movies.csv', index=False)
        print("\n💾 Saved results to classified_movies.csv")
        
        return df
        
    except FileNotFoundError:
        print("❌ Error: movie.csv file not found in working directory")
    except (KeyError, ValueError) as e:
        print(f"🔍 Data validation error: {str(e)}")
        if 'df' in locals():
            print(f"📋 Loaded columns: {df.columns.tolist()}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {str(e)}")
    return None

if __name__ == "__main__":
    processed_movies = process_movie_durations()
    if processed_movies is not None:
        print("\nSample classifications:")
        print(processed_movies[['movie_title', 'duration', 'Duration_Class']]
              .head(10)
              .to_string(index=False))