import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

gemini_api_key = "AIzaSyA7h6nHB9G599q3oTmBWk-sF1da1K6qVZM"

client = AsyncOpenAI(
api_key = gemini_api_key ,
base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    agent= Agent(
        name= "Asistant",
        instructions="you are a friendly agent",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),

    )
    result = await Runner.run(
    agent,
    "how are you !"
    )
    print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())