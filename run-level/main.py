from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

gemini_api_key = "AIzaSyA7h6nHB9G599q3oTmBWk-sF1da1K6qVZM"

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
 
)
model = OpenAIChatCompletionsModel(
     model = "gemini-2.5-flash",
     openai_client= external_client,
 )
config = RunConfig(
    model = model,
    model_provider= external_client,
    tracing_disabled=True
)

agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant"
    )
result = Runner.run_sync(
    agent,"Hello ! how are you" , run_config= config
) 
print(result.final_output)
