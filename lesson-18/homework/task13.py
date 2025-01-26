import pandas as pd

def clean_flights_data():
    """
    Processes flights data by:
    1. Identifying missing values
    2. Filling numerical column nulls with column means
    Returns cleaned DataFrame or None on error
    """
    try:
        # Load data with validation
        flights = pd.read_parquet('flights', engine='pyarrow')
        
        # Initial missing values report
        print("Initial Missing Values Summary:")
        print(flights.isna().sum().sort_values(ascending=False))
        
        # Select numerical columns with missing values
        numerical_cols = flights.select_dtypes(include='number').columns
        cols_to_fill = [col for col in numerical_cols if flights[col].isna().any()]
        
        if not cols_to_fill:
            print("\nNo numerical columns with missing values found")
            return flights
            
        # Fill missing values with column means
        print("\nFilling missing values in columns:")
        for col in cols_to_fill:
            col_mean = flights[col].mean()
            flights[col].fillna(col_mean, inplace=True)
            print(f"- {col}: filled {flights[col].isna().sum()} missing values with mean {col_mean:.2f}")
        
        # Final missing values report
        print("\nRemaining Missing Values Summary:")
        print(flights.isna().sum().sort_values(ascending=False))
        
        return flights
        
    except FileNotFoundError:
        print("Error: flights.parquet file not found in current directory")
    except ImportError:
        print("Missing dependency: Install pyarrow with 'pip install pyarrow'")
    except Exception as e:
        print(f"Data cleaning failed: {str(e)}")
    return None

if __name__ == "__main__":
    cleaned_flights = clean_flights_data()
    if cleaned_flights is not None:
        print("\nSample of cleaned data:")
        print(cleaned_flights[['year', 'month', 'dep_delay', 'arr_delay']].head())