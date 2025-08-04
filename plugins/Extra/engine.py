# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import openai
import os # Import the os module to access environment variables

async def ai(query):
    # Retrieve the OpenAI API key from environment variables
    # It's crucial that OPENAI_API_KEY is set in your deployment environment (e.g., Render)
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    # Ensure the API key is available before making the request
    if not openai.api_key:
        raise ValueError("OpenAI API key not found in environment variables.")

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=query,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.9,
        timeout=5
    )
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        # Extract the question from the user's message
        # Assumes the command is like "/ask What is the capital of France?"
        question = message.text.split(" ", 1)[1]
        
        # Generate response using OpenAI API
        response = await ai(question)
        
        # Send the generated response back to the user
        await m.edit(f"{response}")
    except IndexError:
        # Handle cases where the user didn't provide a question after the command
        await m.edit("Please provide a question after the command. Example: `/ask What is Python?`")
    except ValueError as ve:
        # Handle specific errors like missing API key
        await m.edit(f"Configuration error: {ve}")
    except Exception as e:
        # Catch any other unexpected errors during the process
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)

