import pandas as pd

def calculate_iris_statistics():
    """
    Calculates mean, median, and standard deviation for numerical columns in iris.json
    Returns DataFrame with statistics or None on error
    """
    try:
        # Load data with type validation
        df = pd.read_json('iris.json', orient='columns')
        
        # Validate dataset structure
        if df.empty:
            raise ValueError("Dataset is empty")
            
        # Select numerical columns
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) == 0:
            raise ValueError("No numerical columns found in dataset")
        
        # Calculate statistics
        stats = pd.DataFrame({
            'mean': df[numeric_cols].mean(),
            'median': df[numeric_cols].median(),
            'std_dev': df[numeric_cols].std()
        }).T
        
        # Format output
        print("Numerical Column Statistics:")
        print(stats.to_string(float_format="{:,.3f}".format))
        
        # Return both statistics and original dataframe
        return stats, df, numeric_cols
    
    except FileNotFoundError:
        print("Error: iris.json file not found")
    except ValueError as ve:
        print(f"Data validation error: {ve}")
    except pd.errors.JSONDecodeError:
        print("Error: Invalid JSON format")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    return None, None, None

if __name__ == "__main__":
    stats_df, iris_df, numeric_columns = calculate_iris_statistics()
    if stats_df is not None:
        print("\nAdditional Information:")
        print(f"Total samples: {len(iris_df)}")
        print(f"Analyzed columns: {', '.join(numeric_columns)}")