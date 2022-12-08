import streamlit as st
from streamlit_chat import message
import os
import openai
openai.api_key = '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'

st.title("챗봇 쫑긋 👍 Version 2")

def get_response(prompt_text):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt_text,
      temperature=0.7,
      max_tokens=512,
      top_p=1.0,
      frequency_penalty=0.3,
      presence_penalty=0,
      stop=["You:"]
    )
    return response.choices[0].text
while True:
    prompt_text = input("You: ")
    message("당신 : " + prompt_text,is_user=True)
    response_text = get_response(prompt_text)
    message("쫑긋👍 ver2 : " + response_text)
    if prompt_text == "Bye":
        break
