from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import sqlite3 
import google.generativeai as genai
import speech_recognition as sr

# Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    return rows

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database is named STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
    
    For example:
    Example 1: "How many entries of records are present?"
    should yield: SELECT COUNT(*) FROM STUDENT;
    
    Example 2: "Tell me all the students studying in Data Science class?" 
    should yield: SELECT * FROM STUDENT WHERE CLASS="Data Science";
    
    IMPORTANT: Return only the SQL statement as plain text with no triple backticks or Markdown formatting.
    """
]

# Streamlit app
st.title("Google Gemini SQL Query Generator")
st.subheader("Ask your question (text or voice) and get the SQL query")

# Voice Input Section
st.subheader("🎙️ Or Speak Your Question")

if st.button("🎤 Record Voice"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now.")
        audio = recognizer.listen(source)
        st.success("Recording complete! Transcribing...")
        try:
            spoken_text = recognizer.recognize_google(audio)
            # Store the recognized text in session state so it appears in the text_input
            st.session_state["input"] = spoken_text
            st.write(f"You said: **{spoken_text}**")
        except sr.UnknownValueError:
            st.error("Could not understand audio")
        except sr.RequestError as e:
            st.error(f"Speech recognition error: {e}")

# Text Input Section
question = st.text_input(
    "📝 Type your question:",
    key="input", 
    value=st.session_state.get("input", "")
)

# Button to generate the SQL query
if st.button("🧠 Ask Gemini") and question:
    try:
        response = get_gemini_response(question, prompt)
        # Store the generated SQL in session_state so it persists across re-runs
        st.session_state["generated_query"] = response
        st.subheader("🧾 Generated SQL Query")
        st.code(response, language='sql')
    except Exception as e:
        st.error(f"Something went wrong: {e}")

# If we have a stored query, offer the option to run it
if "generated_query" in st.session_state:
    if st.button("▶️ Run SQL Query"):
        try:
            query_to_execute = st.session_state["generated_query"]
            dataa = read_sql_query(query_to_execute, 'student.db')
            st.subheader("📊 Query Results")
            if dataa:
                for row in dataa:
                    st.write(row)
            else:
                st.info("No data found for the query.")
        except Exception as e:
            st.error(f"Something went wrong while executing the query: {e}")
