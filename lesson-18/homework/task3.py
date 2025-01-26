import pandas as pd

def load_titanic_data():
    """
    Loads titanic.xlsx into a DataFrame, displays first 5 rows.
    Returns DataFrame on success, empty DataFrame on failure.
    """
    file_path = 'titanic.xlsx'
    titanic_df = pd.DataFrame()

    try:
        # Read Excel file with explicit engine specification
        titanic_df = pd.read_excel(file_path, engine='openpyxl')
        
        # Display header and first 5 rows
        print("Titanic dataset - First 5 rows:")
        print(titanic_df.head(5))
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except pd.errors.EmptyDataError:
        print("Error: Excel file contains no data")
    except ImportError:
        print("Missing dependency: Install openpyxl with 'pip install openpyxl'")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        return titanic_df

if __name__ == "__main__":
    df_titanic = load_titanic_data()
    if not df_titanic.empty:
        print("\nDataset loaded successfully!")
        print(f"Total rows: {len(df_titanic)}")