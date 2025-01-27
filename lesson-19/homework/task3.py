import pandas as pd

def analyze_titanic_classes():
    """Analyze Titanic passenger classes with comprehensive statistics.
    
    Performs grouped aggregations to calculate:
    - Average age per class
    - Total fare per class
    - Passenger count per class
    
    Returns:
        pd.DataFrame: Aggregated statistics with columns:
            - Pclass (int): Passenger class
            - AverageAge (float): Mean age in class
            - TotalFare (float): Sum of fares in class
            - PassengerCount (int): Total passengers in class
            
    Raises:
        FileNotFoundError: If data file is missing
        KeyError: If required columns are missing
        ValueError: For data validation failures
    
    Requires:
        - titanic.xlsx in working directory
        - openpyxl package (`pip install openpyxl`)
    """
    try:
        # Load data with optimized column selection
        df = pd.read_excel(
            'titanic.xlsx',
            engine='openpyxl',
            usecols=['Pclass', 'Age', 'Fare'],
            dtype={'Pclass': 'int8', 'Age': 'float32', 'Fare': 'float32'}
        )
        
        # Validate dataset structure
        if df.empty:
            raise ValueError("Dataset contains no records")
            
        required_columns = ['Pclass', 'Age', 'Fare']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing required columns: {missing_columns}")
            
        # Validate numeric data types
        if not pd.api.types.is_numeric_dtype(df['Pclass']):
            raise ValueError("Pclass must be numeric data")
            
        # Calculate statistics in single efficient aggregation
        class_stats = df.groupby('Pclass', observed=True).agg(
            AverageAge=('Age', 'mean'),
            TotalFare=('Fare', 'sum'),
            PassengerCount=('Age', 'size')  # Count all passengers regardless of age
        ).reset_index()
        
        # Create display version with formatted values
        display_stats = class_stats.copy()
        display_stats['AverageAge'] = display_stats['AverageAge'].round(1)
        display_stats['TotalFare'] = display_stats['TotalFare'].astype(int)
        
        # Print formatted results
        print("Passenger Class Statistics:")
        print(display_stats.to_string(index=False, formatters={
            'AverageAge': '{:.1f}'.format,
            'TotalFare': '€{:,.0f}'.format
        }))
        
        # Save full precision results
        class_stats.to_csv('titanic_class_stats.csv', index=False)
        print("\nSaved full precision results to titanic_class_stats.csv")
        
        return class_stats
        
    except FileNotFoundError:
        print("Error: titanic.xlsx file not found in working directory")
    except ImportError:
        print("Missing dependency: Install openpyxl - pip install openpyxl")
    except (KeyError, ValueError) as e:
        print(f"Data validation error: {str(e)}")
        if 'df' in locals():
            print(f"Loaded columns: {df.columns.tolist()}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    return None

if __name__ == "__main__":
    analyze_titanic_classes()