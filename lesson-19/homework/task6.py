import pandas as pd

def classify_age(age: float) -> str:
    """Classify passenger age into Child/Adult categories.
    
    Args:
        age: Passenger's age in years
        
    Returns:
        'Child' for ages < 18, 'Adult' otherwise
    """
    return 'Child' if age < 18 else 'Adult'

def process_titanic_age_groups():
    """Process Titanic data to create age group classification column.
    
    Returns:
        pd.DataFrame: Modified DataFrame with Age_Group column
        None: If errors occur
        
    Requires:
        - titanic.xlsx in working directory
        - openpyxl package (`pip install openpyxl`)
    """
    try:
        # Load data with optimized settings
        df = pd.read_excel(
            'titanic.xlsx',
            engine='openpyxl',
            usecols=['PassengerId', 'Age'],
            dtype={'Age': 'float32'}
        )
        
        # Validate dataset structure
        if df.empty:
            raise ValueError("Dataset contains no passenger records")
            
        if 'Age' not in df.columns:
            raise KeyError("Missing required 'Age' column")
        
        # Create age groups using vectorized approach
        df['Age_Group'] = df['Age'].apply(classify_age)
        
        # Analyze results
        print("🧒👩 Age Group Distribution:")
        print(df['Age_Group'].value_counts().to_string())
        
        # Save results
        df[['PassengerId', 'Age', 'Age_Group']].to_csv('titanic_age_groups.csv', index=False)
        print("\n💾 Saved results to titanic_age_groups.csv")
        
        return df
        
    except FileNotFoundError:
        print("❌ Error: titanic.xlsx file not found in working directory")
    except ImportError:
        print("📦 Missing dependency: Install openpyxl - pip install openpyxl")
    except (KeyError, ValueError) as e:
        print(f"🔍 Data validation error: {str(e)}")
        if 'df' in locals():
            print(f"📋 Loaded columns: {df.columns.tolist()}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {str(e)}")
    return None

if __name__ == "__main__":
    processed_data = process_titanic_age_groups()
    if processed_data is not None:
        print("\nSample records:")
        print(processed_data[['PassengerId', 'Age', 'Age_Group']].head(10).to_string(index=False))