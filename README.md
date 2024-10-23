# Reddit Sentiment Analysis and Solution Generator

## Overview

This project is an AI agent that analyzes Reddit posts and comments to identify user frustrations and potential market gaps. It then generates reports with possible money-making solutions to these problems. The system includes a simple dashboard UI where you can input a list of subreddits to monitor and receive email reports summarizing the findings.

## Features

- Data Collection: Fetches data from specified subreddits using the Reddit API.
- NLP Analysis: Processes text data to detect sentiments, frustrations, and common topics.
- Solution Generation: Suggests potential solutions to identified problems using AI.
- Dashboard UI: Allows management of subreddits and displays AI-suggested subreddits.
- Email Reports: Sends scheduled reports summarizing key insights and potential opportunities.

## Prerequisites

- Python 3.8 or higher
- MongoDB
- Node.js and npm (for frontend)
- Reddit API Credentials
- Email Service API Key
- (Optional) OpenAI API Key for solution generation
- (Optional) Cursor.com account for integration

## Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/dean-rough/reddit-sentiment-solution.git
   cd reddit-sentiment-solution
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

4. Configure environment variables:
   Create a `.env` file in the root directory and add your API keys and credentials.

## Configuration

### API Keys and Accounts Needed

1. Reddit API Credentials:
   - Create a Reddit account and obtain Client ID and Client Secret from [Reddit Apps](https://www.reddit.com/prefs/apps).

2. Email Service API Key:
   - Choose between SendGrid, Mailgun, or SMTP server and obtain the necessary credentials.

3. OpenAI API Key (Optional):
   - Sign up at [OpenAI](https://platform.openai.com/signup/) and create an API key.

4. MongoDB Account:
   - Set up a MongoDB Atlas account or use a local MongoDB installation.

Refer to the respective service documentation for detailed steps on obtaining these credentials.

## Usage

1. Start the backend server:
   ```bash
   cd backend
   python src/api.py
   ```

2. Start the frontend development server:
   ```bash
   cd frontend
   npm start
   ```

3. Access the dashboard at `http://localhost:3000`

## Project Structure

```
reddit-sentiment-solution/
├── backend/
│   ├── src/
│   │   ├── api.py
│   │   └── reddit_analyzer.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── package-lock.json
├── .env
├── .gitignore
└── README.md
```

## Cursor.com Integration (Optional)

To integrate with Cursor.com for enhanced code editing and AI assistance:

1. Create a Cursor.com account at [Cursor.com](https://www.cursor.com/signup).
2. Install Cursor IDE from [Cursor.com downloads](https://www.cursor.com/download).
3. Open the project in Cursor IDE.
4. Configure AI assistance in Settings > AI Integration.
5. Use AI commands like `// Explain this code` or `// Optimize this function` for assistance.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.# reddit-sentiment-solution
# reddit-scanner
