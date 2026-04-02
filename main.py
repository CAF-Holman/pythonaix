import argparse
import os
from prompts import *
from call_function import *


# To Import API Key
from dotenv import load_dotenv

# Importing Google Gemini AI
from google import genai
from google.genai import types

# To import API Key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("Missing GEMINI_API_KEY in .env file")

# Take argument from command line for passing to Gemini
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output") # Adding Verbose output option
args = parser.parse_args() # Now we can access `args.user_prompt`

# List for user prompts
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# Create New Instance of Gemini Client
client = genai.Client(api_key=api_key)

# Calling Geminin Client
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=messages,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        temperature=0,
        tools=[available_functions]
        ),
)

# Get metadata of response
usage = response.usage_metadata

# Verify that response has metadata
if usage is None:
    raise RuntimeError("Response metadata is None")

# Output section
# If user enables verbose mode
if args.verbose is True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print("Reponse:")


# Print Calling Function statement
if response.function_calls:
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
else:
# Response from Gemini
    print(response.text)  # Print response from AI


# Main Section of Code
def main():
    print("Hello from pythonai!")

if __name__ == "__main__":
    main()
