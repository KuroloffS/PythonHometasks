import pandas as pd

def analyze_titanic_ages():
    """
    Calculates minimum, maximum, and sum of passenger ages from titanic.xlsx
    Handles missing data and various edge cases
    """
    try:
        # Load data with type optimization
        df = pd.read_excel('titanic.xlsx', engine='openpyxl', usecols=['Age'])
        
        # Validate dataset
        if df.empty:
            raise ValueError("Dataset is empty")
            
        # Convert to numeric type safely
        ages = pd.to_numeric(df['Age'], errors='coerce')
        
        # Check for valid ages
        valid_ages = ages.dropna()
        if valid_ages.empty:
            print("No valid age data available")
            return None

        # Calculate statistics
        age_stats = {
            'Minimum Age': valid_ages.min(),
            'Maximum Age': valid_ages.max(),
            'Sum of Ages': valid_ages.sum(),
            'Valid Entries': len(valid_ages),
            'Missing Values': ages.isna().sum()
        }
        
        # Format output
        print("Passenger Age Analysis:")
        print(f"- Youngest passenger: {age_stats['Minimum Age']:.1f} years")
        print(f"- Oldest passenger: {age_stats['Maximum Age']:.1f} years")
        print(f"- Total years lived: {age_stats['Sum of Ages']:,.1f}")
        print(f"- Passengers with age data: {age_stats['Valid Entries']}")
        print(f"- Passengers without age data: {age_stats['Missing Values']}")
        
        return age_stats
    
    except FileNotFoundError:
        print("Error: titanic.xlsx file not found in current directory")
    except KeyError:
        print("Error: Dataset is missing the 'Age' column")
        if 'df' in locals():
            print(f"Available columns: {df.columns.tolist()}")
    except ValueError as ve:
        print(f"Data error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    return None

if __name__ == "__main__":
    results = analyze_titanic_ages()
    if results:
        print("\nAdditional Statistics:")
        print(f"Average age: {results['Sum of Ages']/results['Valid Entries']:.1f} years")