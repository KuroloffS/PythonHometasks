import pandas as pd

def process_flight_pipeline():
    """Process flight data with pipeline transformations.
    
    Pipeline Steps:
    1. Filter flights with departure delay >30 minutes
    2. Calculate delay per scheduled flight hour
    
    Returns:
        pd.DataFrame: Processed flight data with new column
        None: If errors occur
        
    Requires:
        - flights.parquet in working directory
        - pyarrow package (`pip install pyarrow`)
    """
    try:
        # Load data with optimized settings
        df = pd.read_parquet(
            'flights',
            engine='pyarrow',
            columns=['DepDelay', 'CRSElapsedTime'],
            dtype={
                'DepDelay': 'float32',
                'CRSElapsedTime': 'float32'
            }
        )
        
        # Validate dataset structure
        if df.empty:
            raise ValueError("Dataset contains no flight records")
            
        required_columns = ['DepDelay', 'CRSElapsedTime']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing required columns: {missing_columns}")

        # Pipeline Step 1: Filter delays
        filtered = df[df['DepDelay'] > 30].copy()
        
        # Pipeline Step 2: Calculate delay ratio
        filtered['Delay_Per_Hour'] = filtered.apply(
            lambda x: x['DepDelay'] / x['CRSElapsedTime'] if x['CRSElapsedTime'] > 0 else pd.NA,
            axis=1
        )
        
        # Clean results
        filtered = filtered.dropna(subset=['Delay_Per_Hour'])
        
        # Analyze results
        print("🛫 Flight Delay Analysis:")
        print(f"Total qualifying flights: {len(filtered):,}")
        print(f"Average delay per hour: {filtered['Delay_Per_Hour'].mean():.2f}")
        
        # Save results
        filtered.to_csv('flight_delays_analysis.csv', index=False)
        print("\n💾 Saved results to flight_delays_analysis.csv")
        
        return filtered
        
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
    processed_flights = process_flight_pipeline()
    if processed_flights is not None:
        print("\nSample records:")
        print(processed_flights.head(10).to_string(index=False))