import pandas as pd
from pathlib import Path
import logging
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables first
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a single client instance to be used throughout
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

class AnomalyExplainer:
    def __init__(self):
        """Initialize the AnomalyExplainer with file paths"""
        self.processed_dir = Path("data/processed")
        # Create processed directory if it doesn't exist
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        
        self.anomaly_report_path = self.processed_dir / "anomaly_report.csv"
        self.superstore_data_path = self.processed_dir / "superstore_with_anomalies.csv"
        self.client = client

    def create_prompt(self, row: pd.Series) -> str:
        """Create a prompt for the API based on the anomaly data"""
        prompt = f"""
        Analyze this sales data point and explain why it might be considered anomalous:
        - Order ID: {row['Order ID']}
        - Product Name: {row['Product Name']}
        - Category: {row['Category']}
        - Sales: ${row['Sales']:.2f}
        - Quantity: {row['Quantity']}
        - Discount: {row['Discount']:.2%}
        - Profit: ${row['Profit']:.2f}

        Please provide:
        1. A brief explanation of why this transaction might be unusual
        2. A specific recommendation for investigation or action

        Format your response as two lines:
        Line 1: Explanation
        Line 2: Recommendation
        """
        return prompt.strip()

    def get_explanation(self, row: pd.Series) -> tuple:
        """Get explanation from DeepSeek API using OpenAI client"""
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert at analyzing sales data anomalies. Analyze the data and provide an explanation and recommendation."
                    },
                    {
                        "role": "user", 
                        "content": self.create_prompt(row)
                    }
                ]
            )

            explanation = response.choices[0].message.content.strip()
            parts = explanation.split("\n")
            return parts[0], parts[1] if len(parts) > 1 else "No specific recommendation."

        except Exception as e:
            logger.error(f"Error in get_explanation: {str(e)}")
            raise

    def process_anomalies(self, anomaly_column: str = 'Anomaly') -> None:
        """Process all rows, adding explanations for anomalies (-1) and '0' for normal rows (1)"""
        try:
            # Read the original data
            logger.info(f"Reading data from {self.superstore_data_path}")
            df = pd.read_csv(self.superstore_data_path)
            logger.info(f"Loaded {len(df)} rows of data")
            
            # Initialize new columns with '0' for all rows
            df['Explanation'] = '0'
            df['Recommendation'] = '0'
            
            # Get indices of anomalies (where value is -1)
            anomaly_indices = df[df[anomaly_column] == -1].index
            logger.info(f"Found {len(anomaly_indices)} anomalies to process")
            
            # Process only the anomalous rows
            for idx in anomaly_indices:
                row = df.iloc[idx]
                explanation, recommendation = self.get_explanation(row)
                
                # Update the explanations for anomalous rows
                df.at[idx, 'Explanation'] = explanation
                df.at[idx, 'Recommendation'] = recommendation
                
                logger.info(f"Processed anomaly for Order ID: {row['Order ID']}")
            
            # Save the complete dataset with explanations
            logger.info(f"Saving results to {self.anomaly_report_path}")
            df.to_csv(self.anomaly_report_path, index=False)
            logger.info(f"Successfully saved anomaly report")
            
        except Exception as e:
            logger.error(f"Error processing anomalies: {str(e)}")
            raise

    def display_report(self) -> pd.DataFrame:
        """Read and display the anomaly report"""
        try:
            if not self.anomaly_report_path.exists():
                logger.warning("No anomaly report found. Run process_anomalies first.")
                return None
            
            # Read the report
            df = pd.read_csv(self.anomaly_report_path)
            
            # Display summary
            logger.info(f"Found {len(df)} analyzed anomalies")
            
            # Set display options for better readability
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_colwidth', None)
            
            return df
            
        except Exception as e:
            logger.error(f"Error reading anomaly report: {str(e)}")
            return None

if __name__ == "__main__":
    explainer = AnomalyExplainer()
    try:
        # Process all anomalies (marked with -1)
        explainer.process_anomalies()
        
        # Read and display some results
        df = pd.read_csv(explainer.anomaly_report_path)
        print("\nSample of processed results:")
        # Show only anomalous rows
        print(df[df['Anomaly'] == -1][['Order ID', 'Explanation', 'Recommendation']].head())
        
    except Exception as e:
        print(f"Error: {str(e)}")

