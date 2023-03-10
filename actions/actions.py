# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import openai
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

CHAT_GPT_CUSTOM_ACTION_ = 'ChatGPT (custom_action): '

# To reduce configuration file parsing time overhead
OPENAI_ENGINE_VERSION = "text-davinci-003"
OPENAPI_API_KEY = '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'
MAX_TOKENS = 1024
TEXT_PROPERTY_NAME = 'text'
OPEN_AI_GPT_METHOD_NAME = "open_ai_gpt"
VERY_FIRST = 0
TEMPERATURE_CHOICE = 0.5
STOP_AT = None
NUMBER_OF_QUERY = 1


def ask_chatgpt(user_message_text):
    # OpenAI API Key
    openai.api_key = OPENAPI_API_KEY

    # Use OpenAI API to get the response for the given user text and intent
    response = openai.Completion.create(
        engine=OPENAI_ENGINE_VERSION,
        prompt=user_message_text,
        max_tokens=MAX_TOKENS,
        n=NUMBER_OF_QUERY,
        stop=STOP_AT,
        temperature=TEMPERATURE_CHOICE,
    ).choices[VERY_FIRST].text

    # Return the response from OpenAI
    return response


class OpenAiGpt(Action):

    def name(self) -> Text:
        return OPEN_AI_GPT_METHOD_NAME

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the latest user text
        user_text = tracker.latest_message.get(TEXT_PROPERTY_NAME)
        openai.api_key = OPENAPI_API_KEY

        prompt = self.buildprompt(user_text)
        # Dispatch the response from OpenAI to the user
        dispatcher.utter_message(CHAT_GPT_CUSTOM_ACTION_ + ask_chatgpt(user_text))

        return []

    @staticmethod
    def buildprompt(user_text):
        return (f"The user said: {user_text}\n"
                f"ChatGPT: "
                )
