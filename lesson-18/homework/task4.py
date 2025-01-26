import pandas as pd

def load_flights_data():
    """
    Loads flights.parquet file into a DataFrame and displays summary info.
    Returns DataFrame on success, empty DataFrame on failure.
    """
    file_path = 'flights'
    flights_df = pd.DataFrame()

    try:
        # Read Parquet file with explicit engine specification
        flights_df = pd.read_parquet(file_path, engine='pyarrow')
        
        # Display dataset summary
        print("Flights dataset summary:")
        flights_df.info()
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ImportError:
        print("Missing dependency: Install pyarrow with 'pip install pyarrow'")
    except Exception as e:
        print(f"Error loading Parquet file: {e}")
    finally:
        return flights_df

if __name__ == "__main__":
    df_flights = load_flights_data()
    if not df_flights.empty:
        print("\nFirst 3 rows:")
        print(df_flights.head(3))