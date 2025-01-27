import pandas as pd
import pyarrow.csv as pacsv

# Function to load and validate the movie data
def load_movie_data(file_path):
    """
    Load and validate movie data from a CSV file using PyArrow for efficiency.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the movie data.
    """
    try:
        # Read the CSV file using PyArrow
        table = pacsv.read_csv(file_path)
        df = table.to_pandas()

        # Validate the essential columns
        required_columns = {"director_name", "color", "num_critic_for_reviews"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"The CSV file must contain the columns: {required_columns}")

        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the movie data: {e}")

# Function to create subsets of the DataFrame
def create_subsets(df):
    """
    Create two subsets of the movie DataFrame.

    Parameters:
        df (pd.DataFrame): The original movie DataFrame.

    Returns:
        pd.DataFrame, pd.DataFrame: Two smaller DataFrames.
    """
    subset1 = df[["director_name", "color"]].drop_duplicates()
    subset2 = df[["director_name", "num_critic_for_reviews"]].drop_duplicates()
    return subset1, subset2

# Function to perform joins and count rows
def perform_joins(subset1, subset2):
    """
    Perform left and full outer joins on the subsets and count the rows.

    Parameters:
        subset1 (pd.DataFrame): First subset of data.
        subset2 (pd.DataFrame): Second subset of data.

    Returns:
        int, int: Row counts for the left join and full outer join.
    """
    # Left join
    left_join_df = subset1.merge(subset2, on="director_name", how="left")
    left_join_count = len(left_join_df)

    # Full outer join
    full_outer_join_df = subset1.merge(subset2, on="director_name", how="outer")
    full_outer_join_count = len(full_outer_join_df)

    return left_join_count, full_outer_join_count

# Main execution block
def main():
    """
    Main function to execute the task.
    """
    file_path = "movie.csv"  # Update with the actual path to your CSV file

    try:
        # Load and validate the data
        movie_df = load_movie_data(file_path)

        # Create subsets
        subset1, subset2 = create_subsets(movie_df)

        # Perform joins and count rows
        left_count, full_outer_count = perform_joins(subset1, subset2)

        # Display results
        print(f"Number of rows in the left join: {left_count}")
        print(f"Number of rows in the full outer join: {full_outer_count}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
