import chainlit as cl
from openai import OpenAI
import os

from dotenv import load_dotenv

#Load environment variables
load_dotenv()

#Initialize OpenAI client
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Initialize chat histroy when chat starts
@cl.on_chat_start
def start():
    cl.user_session.set("messages",[])
#Handle user messages
@cl.on_message
async def main(message:cl.Message):
    #Get history
    messages=cl.user_session.get("messages")

    #Add user message
    messages.append({
        "role":"user",
        "content":message.content
    })

    #LLM response
    response=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages

    )

    answer=response.choices[0].message.content

    #Send respoonse to user
    await cl.Message(content=answer).send()

    #Save assistant response to history
    messages.append({
        "role":"assistant",
        "content":answer
    })
    #Update history
    cl.user_session.set("messages",messages)
