from typing import Dict, List

import openai


def get_response(messages: List[Dict]) -> List[Dict]:
    """Get a response from OpenAI.

    Args:
        messages: A list of messages from the user and the bot.

    Returns:
        A list of messages from the user and the bot.
    """
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=messages,
        )
        messages.append(res.choices[0].message)
    except Exception as e:
        messages.append({"role": "system", "content": f"Error: {e}"})

    return messages
