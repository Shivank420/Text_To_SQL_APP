# Google Gemini SQL Query Generator

This project creates an interactive web application using Streamlit, which allows users to ask questions in natural language (either by typing or speaking) and receive the corresponding SQL query. The app uses Google Gemini's generative AI model to convert the questions into SQL queries and executes them against an SQLite database. The results of the SQL query are displayed within the app.

## Features

- **Text Input:** Users can type their SQL-related questions and get the generated SQL query.
- **Voice Input:** Users can ask their question via voice, which is transcribed into text using the Google Speech Recognition API.
- **SQL Query Generation:** The app uses the Google Gemini model to generate SQL queries based on the user’s question.
- **SQL Query Execution:** Once the SQL query is generated, the user has the option to run it against an SQLite database and view the results.

## Requirements

- Python 3.7 or higher
- Streamlit
- SQLite3 (for the database)
- Google Gemini API key (for accessing Google's generative AI model)
- SpeechRecognition (for voice input)
- dotenv (for managing environment variables)

## Setup Instructions

### 1. Clone the repository:

```bash
git clone <your-repository-url>
cd <your-repository-directory>
