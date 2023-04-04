import openai


def get_response(prompt):
    messages = [
        {"role": "system", "content": "Ship you to the moon."},
    ]
    messages.append({"role": "user", "content": prompt})
    try:
        chat = openai.ChatCompletion.create(model="davinci", messages=messages)
    except Exception as e:
        return e
    reply = chat.choices[0].message.content
    return reply
