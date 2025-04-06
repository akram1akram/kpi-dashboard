# KPI Dashboard with Anomaly Detection and AI Chat Bot

This project is a comprehensive KPI dashboard solution that combines anomaly detection using Isolation Forest algorithm, AI-powered analysis, and an interactive chat bot interface.

## Project Structure

kpi-dashboard/
├── chat-bot/
│ ├── static/
│ │ └── chat-interface.html
│ ├── .env # DeepSeek API key
│ ├── app.py # Flask application for chat bot
│ └── requirements.txt # Chat bot dependencies
├── data/
│ ├── processed/ # Processed data files
│ └── raw/
│ └── sample.csv # Original data
├── src/
│ ├── anomaly_detection.py # Isolation Forest implementation
│ ├── anomaly_explanation.py # AI-powered anomaly analysis
│ └── data_processing.py # Data preprocessing scripts
├── .env # Project-wide API keys
└── requirements.txt # Project dependencies

## Components

### 1. Data Processing
- Location: `src/data_processing.py`
- Purpose: Preprocesses raw data for analysis
- Input: `data/raw/sample.csv`
- Output: Processed files in `data/processed/`

### 2. Anomaly Detection
- Location: `src/anomaly_detection.py`
- Purpose: Identifies anomalies in KPI data using Isolation Forest
- Features:
  - Isolation Forest algorithm implementation
  - Unsupervised anomaly detection
  - Efficient for high-dimensional data
  - Handles both numerical and categorical features
  - Scores data points based on isolation ease

### 3. Anomaly Explanation
- Location: `src/anomaly_explanation.py`
- Purpose: AI-powered analysis of detected anomalies
- Features:
  - DeepSeek API integration
  - Natural language explanations
  - Actionable insights
  - Contextual analysis of anomalies

### 4. Chat Bot Interface
- Location: `chat-bot/`
- Components:
  - Flask backend (`app.py`)
  - Web interface (`static/chat-interface.html`)
  - DeepSeek API integration

## Setup and Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
```

2. Install project dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- Main project `.env`:
```
API_KEY=your_main_api_key_here
```
- Chat bot `.env`:
```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

## Anomaly Detection Process

The project uses Isolation Forest algorithm for anomaly detection:

1. **Data Preparation**
   - Feature selection
   - Data normalization
   - Handling missing values

2. **Isolation Forest Implementation**
   - Unsupervised learning approach
   - Identifies anomalies by isolation
   - Parameters:
     - n_estimators: Number of trees
     - contamination: Expected proportion of outliers
     - random_state: For reproducibility

3. **Scoring**
   - Anomaly scores assigned to each data point
   - -1: Anomalous points
   - 1: Normal points

4. **Analysis**
   - Results stored in processed data
   - Anomalies explained by AI
   - Visualized in dashboard

## Integration with Google Looker Studio

1. Get the ngrok URL from terminal
2. In Looker Studio:
   - Add a new "Custom HTML" block
   - Paste the iframe code:
```html
<iframe
    src="YOUR_NGROK_URL"
    width="100%"
    height="500px"
    frameborder="0"
    style="border: 1px solid #ccc; border-radius: 4px;"
></iframe>
```
# KPI Dashboard with Anomaly Detection and AI Chat Bot

[Previous sections remain the same...]

## Dashboard Integration Options

### 1. Google Looker Studio Integration (Requires Private Access)
- Embed chat bot directly in Looker Studio dashboard
- Requires private access/enterprise account
- Integration via Custom HTML block
```html
<iframe
    src="YOUR_NGROK_URL"
    width="100%"
    height="500px"
    frameborder="0"
    style="border: 1px solid #ccc; border-radius: 4px;"
></iframe>
```

### 2. Alternative Integration Option (Blogger.com)
Due to Looker Studio private access limitations, this project demonstrates integration using Blogger.com:
- Dashboard report and chat bot embedded together
- Free and accessible solution
- Steps to implement:
  1. Export Looker Studio report as embed code
  2. Create new post on Blogger.com
  3. Add dashboard embed code
  4. Add chat bot iframe code
  5. Arrange elements as desired
  6. Publish and share publicly

Benefits of Blogger.com approach:
- No access restrictions
- Free hosting
- Easy to maintain
- Public accessibility
- Flexible layout options


## Dependencies

### Main Project
- pandas
- numpy
- scikit-learn (for Isolation Forest)
- python-dotenv
- openai

### Chat Bot
- Flask
- Flask-CORS
- openai
- python-dotenv
- ngrok (for testing)

## Data Flow
1. Raw data ingestion (`data/raw/`)
2. Data processing and cleaning
3. Isolation Forest anomaly detection
4. AI-powered analysis
5. Results visualization in dashboard
6. Interactive analysis via chat bot

## Notes
- Isolation Forest is particularly effective for high-dimensional data
- Algorithm complexity: O(n log n)
- Contamination parameter should be tuned based on domain knowledge
- Keep both Flask server and ngrok running for chat bot
- Ensure all API keys are properly configured

## Future Improvements
- Enhanced Isolation Forest parameters tuning
- Additional anomaly detection algorithms
- Automated data pipeline
- Advanced AI analysis features
- Cloud deployment for chat bot
- Real-time data processing

## Troubleshooting
- Check API keys in both .env files
- Verify data file paths
- Monitor processing logs
- Ensure proper port configuration (5001)
- Review Isolation Forest parameters if detection accuracy is off

## Author
Akram Al Abdouni

