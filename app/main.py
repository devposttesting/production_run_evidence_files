"""Gemini Tales - interactive AI storytelling agent."""
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def next_story_segment(profile: dict, transcript: list[str]) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=_build_prompt(profile, transcript),
    )
    return response.text


def _build_prompt(profile: dict, transcript: list[str]) -> str:
    turns = "\n".join(transcript[-6:])
    return (
        f"You are a children's storyteller. Child: {profile['name']}, "
        f"age {profile['age']}, language {profile['language']}.\n"
        f"Recent turns:\n{turns}\nContinue the story with one short segment."
    )
