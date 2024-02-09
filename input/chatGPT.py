from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Esti un eminent om politic specializat in afaceri externe"},
    {"role": "user", "content": "Compune o disertatie despre drepturile omului si formateaza citet"}
  ]
)

print(completion.choices[0].message)