import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

def detect_anomalies(df: pd.DataFrame):
    """Flag anomalies in sales/profit using Isolation Forest."""
    # Prepare data
    X = df[['Sales', 'Profit']]

    # Train model
    model = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly'] = model.fit_predict(X)

    # Plot anomalies
    plt.scatter(df['Sales'], df['Profit'], c=df['Anomaly'], cmap='coolwarm')
    plt.title("Anomaly Detection (Isolation Forest)")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.savefig("data/processed/anomalies.png")  # Save plot
    print("📊 Anomaly plot saved to 'data/processed/'!")
    
    return df

if __name__ == "__main__":
    # Load processed data
    df = pd.read_csv("data/processed/cleaned_superstore.csv")
    
    # Detect anomalies
    df_anomalies = detect_anomalies(df)
    
    # Save results
    df_anomalies.to_csv("data/processed/superstore_with_anomalies.csv", index=False)
    print("✅ Anomalies detected and saved!")