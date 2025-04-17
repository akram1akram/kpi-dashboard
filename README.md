KPI Dashboard with Anomaly Detection and AI Chat Bot
This project is a comprehensive KPI dashboard solution that combines anomaly detection using Isolation Forest algorithm, AI-powered analysis, and an interactive chat bot interface.

Visit the live dashboard viewer hosted on GitHub Pages: https://<your-username>.github.io/<your-repo-name>/ (Replace placeholders with your actual GitHub Pages URL)

Project Structure
kpi-dashboard/
├── chat-bot/
│   ├── static/
│   │   └── chat-interface.html # Served by Render
│   ├── .env # DeepSeek API key (on Render)
│   ├── app.py # Flask application for chat bot (on Render)
│   └── requirements.txt # Chat bot dependencies (on Render)
├── data/
│   ├── processed/ # Processed data files
│   └── raw/
│       └── sample.csv # Original data
├── src/
│   ├── anomaly_detection.py # Isolation Forest implementation
│   ├── anomaly_explanation.py # AI-powered anomaly analysis
│   └── data_processing.py # Data preprocessing scripts
├── .env # Project-wide API keys (local)
├── index.html # Dashboard viewer HTML (hosted on GitHub Pages)
└── requirements.txt # Project dependencies (local)

Components
1. Data Processing
Location: src/data_processing.py

Purpose: Preprocesses raw data for analysis

Input: data/raw/sample.csv

Output: Processed files in data/processed/

2. Anomaly Detection
Location: src/anomaly_detection.py

Purpose: Identifies anomalies in KPI data using Isolation Forest

Features:

Isolation Forest algorithm implementation

Unsupervised anomaly detection

Efficient for high-dimensional data

Handles both numerical and categorical features

Scores data points based on isolation ease

3. Anomaly Explanation
Location: src/anomaly_explanation.py

Purpose: AI-powered analysis of detected anomalies

Features:

DeepSeek API integration

Natural language explanations

Actionable insights

Contextual analysis of anomalies

4. Chat Bot Interface (Hosted on Render)
Location: chat-bot/ (Codebase)

Service URL: https://kpi-dashboard-live.onrender.com/ (Example URL)

Components:

Flask backend (app.py)

Web interface (static/chat-interface.html) - Served via Flask

DeepSeek API integration

5. Dashboard Viewer (Hosted on GitHub Pages)
Location: index.html (Codebase)

Service URL: https://<your-username>.github.io/<your-repo-name>/ (Example URL)

Purpose: Displays Looker Studio report and embeds the Chat Bot via iframes.

Setup and Installation (Local Development/Analysis)
Create and activate virtual environment:

python -m venv venv
source venv/bin/activate  # For Mac/Linux
# venv\Scripts\activate  # For Windows

Install project dependencies:

pip install -r requirements.txt

Set up environment variables:

Main project .env (for local scripts):

API_KEY=your_main_api_key_here

Chat bot .env (for local testing, mirror Render env vars):

DEEPSEEK_API_KEY=your_deepseek_api_key_here

Anomaly Detection Process
The project uses Isolation Forest algorithm for anomaly detection:

Data Preparation

Feature selection

Data normalization

Handling missing values

Isolation Forest Implementation

Unsupervised learning approach

Identifies anomalies by isolation

Parameters:

n_estimators: Number of trees

contamination: Expected proportion of outliers

random_state: For reproducibility

Scoring

Anomaly scores assigned to each data point

-1: Anomalous points

1: Normal points

Analysis

Results stored in processed data

Anomalies explained by AI

Visualized in dashboard

Integration with Google Looker Studio
(This describes embedding the locally running chatbot via ngrok for testing purposes within Looker Studio)

Run the chatbot Flask app locally (python chat-bot/app.py).

Run ngrok to expose your local server (ngrok http 5001 - assuming Flask runs on 5001).

Get the ngrok forwarding URL (e.g., https://xxxx-xx-xx-xx-xx.ngrok-free.app).

In Looker Studio:

Add a new "URL embed" component.

Paste the ngrok URL.

Dashboard Integration
The primary dashboard view is provided by the index.html file hosted on GitHub Pages. This HTML file embeds:

The Google Looker Studio report using its embed URL.

The AI Chat Bot using the URL of the deployed Render service (e.g., https://kpi-dashboard-live.onrender.com/).

(The section detailing Blogger.com integration has been removed).

Dependencies
Main Project (Local Analysis Scripts)
pandas

numpy

scikit-learn (for Isolation Forest)

python-dotenv

openai

Chat Bot (Hosted on Render)
Flask

Flask-CORS

openai

python-dotenv

gunicorn (typically used by Render)

Data Flow
Raw data ingestion (data/raw/)

Data processing and cleaning (src/)

Isolation Forest anomaly detection (src/)

AI-powered analysis (src/)

Results visualization in Looker Studio report (embedded)

Interactive analysis via chat bot (embedded)

Integrated view via index.html on GitHub Pages

Notes
Isolation Forest is particularly effective for high-dimensional data.

Algorithm complexity: O(n log n).

Contamination parameter should be tuned based on domain knowledge.

Chatbot requires the Render service to be running.

Ensure all API keys are properly configured as environment variables on Render for the chatbot.

Future Improvements
Enhanced Isolation Forest parameters tuning

Additional anomaly detection algorithms

Automated data pipeline for processing/detection

Advanced AI analysis features

Real-time data processing integration

Troubleshooting
Chatbot: Check Render logs, API keys on Render, Render service status.

Dashboard Viewer (index.html): Ensure GitHub Pages deployment is successful, check iframe URLs are correct and accessible.

Local Scripts: Check local API keys, data file paths, Python environment, processing logs. Review Isolation Forest parameters if detection accuracy is off.

Author
Akram Al Abdouni