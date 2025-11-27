import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")



    client = genai.Client(api_key=api_key)

    argument_list = sys.argv
    if len(argument_list) < 2:
        print("Please provide a string as an argument to this program")
        sys.exit(1)
    else:
        user_prompt = argument_list[1]
        messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        content_response = client.models.generate_content(model="gemini-2.0-flash-001",contents=messages)
        print(content_response.text)
        print(f"Prompt tokens: {content_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {content_response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()