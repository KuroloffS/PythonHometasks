def analyze_titanic_data(titanic_df):
    """
    Analyzes Titanic data by filtering passengers over 30 and counting genders.
    Returns tuple: (filtered DataFrame, gender counts) or (None, None) on error
    """
    try:
        # Validate input DataFrame
        if titanic_df.empty:
            raise ValueError("Input DataFrame is empty")
            
        # Check required columns exist
        required_cols = ['Age', 'Sex']
        missing_cols = [col for col in required_cols if col not in titanic_df.columns]
        if missing_cols:
            raise KeyError(f"Missing columns: {missing_cols}")

        # 1. Filter passengers over 30
        over_30 = titanic_df[titanic_df['Age'] > 30]
        print(f"Found {len(over_30)} passengers over 30 years old")
        
        # 2. Count gender distribution
        gender_counts = over_30['Sex'].value_counts()
        
        # Display results
        print("\nGender distribution:")
        print(gender_counts.to_string())
        
        return over_30, gender_counts
    
    except KeyError as ke:
        print(f"Data validation error: {ke}")
        print(f"Available columns: {list(titanic_df.columns)}")
        return None, None
    except TypeError as te:
        print(f"Data type error: {te}\nCheck Age column format")
        return None, None
    except Exception as e:
        print(f"Analysis failed: {e}")
        return None, None

# Usage example (assuming you have the Titanic DataFrame from Task 3):
if __name__ == "__main__":
    from task3 import load_titanic_data  # Import Task 3's function
    
    # Load original data
    original_titanic = load_titanic_data()
    
    if not original_titanic.empty:
        # Perform analysis
        filtered_data, counts = analyze_titanic_data(original_titanic)
        
        if filtered_data is not None:
            print("\nSample of filtered passengers:")
            print(filtered_data[['Name', 'Age', 'Sex']].head(3).to_string(index=False))