import pandas as pd

def analyze_flight_groups():
    """Analyze flight data with nested yearly/monthly groupings.
    
    Calculates:
    - Total flights per month
    - Average arrival delay per month
    - Maximum departure delay per month
    
    Returns:
        pd.DataFrame: Aggregated statistics with columns:
            - Year (int)
            - Month (int)
            - TotalFlights (int)
            - AverageArrDelay (float)
            - MaxDepDelay (float)
            
    Raises:
        FileNotFoundError: If data file is missing
        KeyError: If required columns are missing
        ValueError: For data validation failures
    
    Requires:
        - flights.parquet in working directory
        - pyarrow package (`pip install pyarrow`)
    """
    try:
        # Load data with optimized column selection
        df = pd.read_parquet(
            'flights',
            engine='pyarrow',
            columns=['Year', 'Month', 'ArrDelay', 'DepDelay']
        )
        
        # Validate dataset structure
        if df.empty:
            raise ValueError("Dataset contains no flight records")
            
        required_columns = ['Year', 'Month', 'ArrDelay', 'DepDelay']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing required columns: {missing_columns}")

        # Clean data
        df = df.dropna(subset=['Year', 'Month']).copy()
        df['ArrDelay'] = df['ArrDelay'].fillna(0)
        df['DepDelay'] = df['DepDelay'].fillna(0)
        
        # Convert to efficient types
        df = df.astype({
            'Year': 'int16',
            'Month': 'int8',
            'ArrDelay': 'float32',
            'DepDelay': 'float32'
        })
        
        # Calculate grouped statistics
        grouped_stats = df.groupby(['Year', 'Month'], observed=True).agg(
            TotalFlights=('ArrDelay', 'size'),
            AverageArrDelay=('ArrDelay', 'mean'),
            MaxDepDelay=('DepDelay', 'max')
        ).reset_index()
        
        # Create display version
        display_stats = grouped_stats.copy()
        display_stats['AverageArrDelay'] = display_stats['AverageArrDelay'].round(2)
        
        # Print formatted results
        print("✈️ Flight Group Statistics:")
        print(display_stats.head(10).to_string(
            index=False,
            formatters={
                'TotalFlights': '{:,.0f}'.format,
                'AverageArrDelay': '{:.2f} min'.format,
                'MaxDepDelay': '{:.0f} min'.format
            }
        ))
        
        # Save full results
        grouped_stats.to_csv('flight_group_stats.csv', index=False)
        print("\n💾 Saved full results to flight_group_stats.csv")
        
        return grouped_stats
        
    except FileNotFoundError:
        print("❌ Error: flights.parquet file not found in working directory")
    except ImportError:
        print("📦 Missing dependency: Install pyarrow - pip install pyarrow")
    except (KeyError, ValueError) as e:
        print(f"🔍 Data validation error: {str(e)}")
        if 'df' in locals():
            print(f"📋 Loaded columns: {df.columns.tolist()}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {str(e)}")
    return None

if __name__ == "__main__":
    analyze_flight_groups()