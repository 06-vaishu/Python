from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)

