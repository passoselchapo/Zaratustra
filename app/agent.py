
import os
import google.generativeai as genai

def call_llm_agent(user_message: str) -> str:
    # Configure Google Generative AI with API key from environment variables
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Initialize the Gemini model for text generation
    model = genai.GenerativeModel('gemini-pro') # Using a general text generation model

    try:
        # Send the user message to the Gemini model
        response = model.generate_content(user_message)
        assistant_response = response.text
    except Exception as e:
        # Handle potential errors from the API call
        print(f"Error calling Gemini API: {e}")
        assistant_response = "I'm sorry, I couldn't process your request at the moment due to an internal error."

    return assistant_response
