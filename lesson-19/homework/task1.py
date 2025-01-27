import sqlite3
import pandas as pd

def get_customer_invoice_counts():
    """Retrieves invoice counts per customer from Chinook database.
    
    Returns:
        DataFrame: Customer invoice counts with columns:
            - CustomerId
            - FirstName
            - LastName
            - InvoiceCount
            
    Raises:
        FileNotFoundError: If database file is missing
        DatabaseError: For SQL-related issues
    """
    db_path = 'chinook.db'
    
    try:
        # Connect to database using context manager
        with sqlite3.connect(db_path) as conn:
            # Define optimized SQL query
            query = """
                SELECT 
                    c.CustomerId,
                    c.FirstName,
                    c.LastName,
                    COUNT(i.InvoiceId) AS InvoiceCount
                FROM customers c
                INNER JOIN invoices i
                    ON c.CustomerId = i.CustomerId
                GROUP BY c.CustomerId
                ORDER BY InvoiceCount DESC;
            """
            
            # Execute query and load results
            result_df = pd.read_sql_query(query, conn)
            
            # Validate results
            if result_df.empty:
                print("Warning: No customer invoice data found")
            else:
                print("Top 5 Customers by Invoice Count:")
                print(result_df.head().to_string(index=False))
                
            return result_df
            
    except FileNotFoundError:
        print(f"Error: Database file not found at {db_path}")
    except sqlite3.Error as db_err:
        print(f"Database Error: {str(db_err)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
    return pd.DataFrame()

if __name__ == "__main__":
    invoice_counts = get_customer_invoice_counts()
    if not invoice_counts.empty:
        print("\nSummary Statistics:")
        print(f"Total customers with invoices: {len(invoice_counts)}")
        print(f"Average invoices per customer: {invoice_counts['InvoiceCount'].mean():.1f}")