import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables (for database credentials later)
load_dotenv()

import chardet
from pathlib import Path

def load_data(file_path):
    # Convert string path to Path object
    file_path = Path(file_path)
      # Try multiple encodings
    for encoding in ['utf-8', 'latin1', 'ISO-8859-1', 'utf-16']:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"Successfully read with {encoding} encoding!")
            df['Order Date'] = pd.to_datetime(df['Order Date'])
            df['Ship Date'] = pd.to_datetime(df['Ship Date'])
            df['Profit Margin'] = df['Profit'] / df['Sales'] 
            return df
        except UnicodeDecodeError:
            continue
            
    raise ValueError("Failed to read CSV with common encodings")

df = load_data("kpi-dashboard/data/raw/sample.csv")

# Basic dataframe checks (check if the data is loaded correctly)
def basic_checks(df):
    print(df.head())  # First 5 rows
    print(df.shape)   # (rows, columns)
    print(df.columns) # Column names
    print(df.info())  # Data types and non-null counts

def save_to_sql(df: pd.DataFrame, table_name: str) -> None:
    """
    Save DataFrame to PostgreSQL database.
    
    Args:
        df (pd.DataFrame): DataFrame to save
        table_name (str): Name of the table in database
        
    Raises:
        ValueError: If DB_URL environment variable is not set
        SQLAlchemyError: If database connection/writing fails
    """
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("DB_URL not found in environment variables")
        
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"✅ Data saved to SQL table '{table_name}'!")
        
        # Verify the data was saved
        row_count = engine.execute(f"SELECT COUNT(*) FROM {table_name}").scalar()
        print(f"✓ Verified {row_count} rows in table")
        
    except Exception as e:
        print(f"❌ Error saving to database: {str(e)}")
        raise

if __name__ == "__main__":
    # Define the path to our raw data file in the data/raw directory
    raw_data_path = "data/raw/sample.csv"
    
    # Load the CSV file into a pandas DataFrame using our custom load_data function
    # This function handles different encodings and returns a clean DataFrame
    df = load_data(raw_data_path)
    
    # Optional: Save the DataFrame to a PostgreSQL database
    # Commented out until database connection is configured in .env file
    # save_to_sql(df, "sales_data")
    
    # Save the processed DataFrame to a new CSV file in the data/processed directory
    # index=False prevents pandas from adding a new index column
    df.to_csv("data/processed/cleaned_superstore.csv", index=False)
    
    # Print confirmation message that data has been saved successfully
    print("📁 Processed data saved to 'data/processed/'!")



