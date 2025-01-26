import pandas as pd

def analyze_flights_data():
    """
    Analyzes flights data by extracting specific columns and counting unique destinations.
    Returns tuple: (selected DataFrame, unique destination count) or (None, None) on error
    """
    try:
        # Load data with validation
        flights_df = pd.read_parquet('flights', engine='pyarrow')
        
        # Validate required columns
        required_cols = ['origin', 'dest', 'carrier']
        missing_cols = [col for col in required_cols if col not in flights_df.columns]
        if missing_cols:
            raise KeyError(f"Missing required columns: {missing_cols}")

        # Extract and display specified columns
        selected_data = flights_df[required_cols]
        print("First 5 rows of selected columns:")
        print(selected_data.head().to_string(index=False))
        
        # Calculate unique destinations
        unique_dest_count = selected_data['dest'].nunique()
        print(f"\nNumber of unique destinations: {unique_dest_count}")
        
        return selected_data, unique_dest_count
    
    except FileNotFoundError:
        print("Error: flights.parquet file not found in current directory")
    except ImportError:
        print("Missing dependency: Install pyarrow with 'pip install pyarrow'")
    except KeyError as ke:
        print(f"Data validation error: {ke}")
        if 'flights_df' in locals():
            print(f"Available columns: {list(flights_df.columns)}")
    except Exception as e:
        print(f"Analysis failed: {str(e)}")
    return None, None

if __name__ == "__main__":
    df_flights, destinations = analyze_flights_data()
    if df_flights is not None:
        print("\nAdditional statistics:")
        print(f"Total flights analyzed: {len(df_flights):,}")
        print("Top 5 carriers:")
        print(df_flights['carrier'].value_counts().head(5))