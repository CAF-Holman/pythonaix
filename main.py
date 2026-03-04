import os

# To Import API Key
from dotenv import load_dotenv

# Importing Google Gemini AI
from google import genai

# To import API Key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("Missing GEMINI_API_KEY in .env file")

# Create New Instance of Gemini Client
client = genai.Client(api_key=api_key)

# First attempt at calling AI. Hard Coded request.
response = client.models.generate_content(
    model='gemini-2.5-flash', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
print(response.text)  # Print response from AI


# Main Section of Code
def main():
    print("Hello from pythonai!")

if __name__ == "__main__":
    main()
