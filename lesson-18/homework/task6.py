def process_iris_data(iris_df):
    """
    Processes iris DataFrame by renaming columns to lowercase and selecting specific columns.
    Returns modified DataFrame or None if errors occur.
    """
    try:
        # Create a copy to avoid modifying original DataFrame
        processed_df = iris_df.copy()
        
        # 1. Rename columns to lowercase
        processed_df.columns = processed_df.columns.str.lower()
        print("Columns renamed to lowercase successfully.")
        
        # 2. Select specific columns with error checking
        required_columns = ['sepal_length', 'sepal_width']
        
        # Check if all required columns exist
        missing_cols = [col for col in required_columns if col not in processed_df.columns]
        if missing_cols:
            raise KeyError(f"Missing columns: {missing_cols}")
            
        selected_df = processed_df[required_columns]
        print("\nSelected columns sample:")
        print(selected_df.sample(3, random_state=42))  # Display random sample
        
        return selected_df
    
    except KeyError as ke:
        print(f"Column selection error: {ke}")
        print(f"Available columns: {list(processed_df.columns)}")
        return None
    except Exception as e:
        print(f"Processing failed: {e}")
        return None

# Usage example (assuming you have the iris DataFrame from Task 2):
if __name__ == "__main__":
    from task2 import load_iris_data  # Import Task 2's function
    
    # Load the original data
    original_iris = load_iris_data()
    
    if not original_iris.empty:
        # Process the data
        iris_subset = process_iris_data(original_iris)
        
        if iris_subset is not None:
            print("\nFinal DataFrame shape:", iris_subset.shape)