import pandas as pd

def analyze_movie_groups():
    """Analyze movie data by color and director groups.
    
    Calculates:
    - Total critic reviews per group
    - Average duration per group
    
    Returns:
        pd.DataFrame: Aggregated statistics with columns:
            - color (str): Film color type
            - director_name (str): Director name
            - TotalCriticReviews (int): Sum of critic reviews
            - AverageDuration (float): Mean movie duration
            
    Raises:
        FileNotFoundError: If data file is missing
        KeyError: If required columns are missing
        ValueError: For data validation failures
    
    Requires:
        - movie.csv in working directory
    """
    try:
        # Load data with optimized settings
        df = pd.read_csv(
            'movie.csv',
            usecols=['color', 'director_name', 'num_critic_for_reviews', 'duration'],
            dtype={
                'color': 'category',
                'director_name': 'string',
                'num_critic_for_reviews': 'Int32',
                'duration': 'Int16'
            }
        )
        
        # Validate dataset
        if df.empty:
            raise ValueError("Dataset contains no records")
            
        required_columns = ['color', 'director_name', 'num_critic_for_reviews', 'duration']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing required columns: {missing_columns}")
        
        # Clean data
        df = df.dropna(subset=['director_name']).copy()
        df['num_critic_for_reviews'] = df['num_critic_for_reviews'].fillna(0)
        
        # Calculate grouped statistics
        grouped_stats = df.groupby(['color', 'director_name'], observed=True).agg(
            TotalCriticReviews=('num_critic_for_reviews', 'sum'),
            AverageDuration=('duration', 'mean')
        ).reset_index()
        
        # Create display version
        display_stats = grouped_stats.copy()
        display_stats['AverageDuration'] = display_stats['AverageDuration'].round(1)
        
        # Print formatted results
        print("🎬 Movie Group Statistics:")
        print(display_stats.head(10).to_string(
            index=False,
            formatters={
                'TotalCriticReviews': '{:,.0f}'.format,
                'AverageDuration': '{:.1f} min'.format
            }
        ))
        
        # Save full results
        grouped_stats.to_csv('movie_group_stats.csv', index=False)
        print("\n💾 Saved full results to movie_group_stats.csv")
        
        return grouped_stats
        
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
    analyze_movie_groups()