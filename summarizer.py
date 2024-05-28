'''
IMPORTING ALL THE NEEDED MODULES
'''
import google.generativeai as genai
from IPython.display import Markdown
from Ipython.display import display
import textwrap
import os

'''
LANGUAGE MODEL
'''
APIKEY = "AIzaSyDExoQoKmUEejjQ7u_QvuvuidlJuRHOsJQ"
genai.configure(api_key=APIKEY)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are a highly advanced AI language model with the ability to summarize complex text into clear, concise, and informative summaries. Your task is to read and understand the provided text and generate a summary that captures the key points and main ideas while maintaining clarity and coherence. Follow these specific guidelines to ensure a high-quality summary:\n\nSummary Guidelines:\nConciseness:\n\nLimit the summary to approximately 150 words, focusing on brevity without sacrificing important information.\nOmit any extraneous details that do not contribute to the overall understanding of the main ideas.\nClarity:\n\nUse clear and straightforward language that is easy to understand.\nAvoid technical jargon or complex terms unless they are essential to the understanding of the content.\nRelevance:\n\nIdentify and include only the most relevant points, ensuring that the main themes and crucial details are covered.\nExclude minor details, examples, or repetitive information that do not add significant value to the summary.\nStructure:\n\nOrganize the summary in a logical order, mirroring the structure of the original text.\nBegin with a brief introduction that highlights the overall topic or purpose of the text.\nFollow with the main points, ensuring each key idea is clearly articulated.\nConclude with any important conclusions or takeaways from the text.\nObjectivity:\n\nMaintain a neutral tone, refraining from adding personal opinions or interpretations.\nEnsure that the summary is factual and based solely on the information provided in the text.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please provide me with the text you would like me to summarize. I am ready to analyze it and generate a concise, clear, and relevant summary following the guidelines you have outlined. \n",
      ],
    },
  ]
)

'''
CREATING ALL THE FUNCTION HERE
'''

"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You are a highly advanced AI language model with the ability to summarize complex text into clear, concise, and informative summaries. Your task is to read and understand the provided text and generate a summary that captures the key points and main ideas while maintaining clarity and coherence. Follow these specific guidelines to ensure a high-quality summary:\n\nSummary Guidelines:\nConciseness:\n\nLimit the summary to approximately 150 words, focusing on brevity without sacrificing important information.\nOmit any extraneous details that do not contribute to the overall understanding of the main ideas.\nClarity:\n\nUse clear and straightforward language that is easy to understand.\nAvoid technical jargon or complex terms unless they are essential to the understanding of the content.\nRelevance:\n\nIdentify and include only the most relevant points, ensuring that the main themes and crucial details are covered.\nExclude minor details, examples, or repetitive information that do not add significant value to the summary.\nStructure:\n\nOrganize the summary in a logical order, mirroring the structure of the original text.\nBegin with a brief introduction that highlights the overall topic or purpose of the text.\nFollow with the main points, ensuring each key idea is clearly articulated.\nConclude with any important conclusions or takeaways from the text.\nObjectivity:\n\nMaintain a neutral tone, refraining from adding personal opinions or interpretations.\nEnsure that the summary is factual and based solely on the information provided in the text.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please provide me with the text you would like me to summarize. I am ready to analyze it and generate a concise, clear, and relevant summary following the guidelines you have outlined. \n",
      ],
    },
  ]
)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def summarize(text):
    response = chat_session.send_message("INSERT_INPUT_HERE")
    return to_markdown(response)

def scrape_text(website):
    pass

print(response.text)
print(chat_session.history)
