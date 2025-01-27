import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

def validate_data(df):
    """
    Validates the DataFrame to ensure required columns exist.
    Args:
        df (pd.DataFrame): Input DataFrame.
    Raises:
        ValueError: If required columns are missing.
    """
    required_columns = {'Survived', 'Age', 'Fare'}
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def filter_survived(df):
    """
    Filters passengers who survived.
    Args:
        df (pd.DataFrame): Input DataFrame.
    Returns:
        pd.DataFrame: Filtered DataFrame with only survivors.
    """
    return df[df['Survived'] == 1]


def fill_missing_age(df):
    """
    Fills missing Age values with the mean of Age.
    Args:
        df (pd.DataFrame): Input DataFrame.
    Returns:
        pd.DataFrame: DataFrame with missing Age values filled.
    """
    mean_age = df['Age'].mean()
    df['Age'] = df['Age'].fillna(mean_age)
    return df


def add_fare_per_age(df):
    """
    Adds a new column Fare_Per_Age by dividing Fare by Age.
    Args:
        df (pd.DataFrame): Input DataFrame.
    Returns:
        pd.DataFrame: DataFrame with the new column added.
    """
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df


def process_titanic_data(df):
    """
    Processes Titanic data by applying the pipeline.
    Args:
        df (pd.DataFrame): Input DataFrame.
    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    try:
        # Validate data
        validate_data(df)
        
        # Convert to PyArrow Table for faster processing
        arrow_table = pa.Table.from_pandas(df)
        
        # Filter survivors
        survived_table = arrow_table.filter(pc.equal(arrow_table['Survived'], 1))
        
        # Convert back to pandas for filling missing Age
        survived_df = survived_table.to_pandas()
        survived_df = fill_missing_age(survived_df)
        
        # Add Fare_Per_Age
        processed_df = add_fare_per_age(survived_df)
        
        return processed_df

    except Exception as e:
        print(f"Error processing Titanic data: {e}")
        raise


# Example Usage
if __name__ == "__main__":
    # Example DataFrame
    data = {
        'Survived': [1, 0, 1, 1],
        'Age': [22, None, 24, 30],
        'Fare': [7.25, 71.83, 8.05, 10.50]
    }
    df = pd.DataFrame(data)
    
    # Process the data
    try:
        result_df = process_titanic_data(df)
        print(result_df)
    except Exception as e:
        print(f"Failed to process data: {e}")
