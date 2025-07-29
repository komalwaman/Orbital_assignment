import re

def is_palindrome(text: str) -> bool:
  clean = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
  return clean == clean[::-1]

def get_words(text: str):
  return re.findall(r"[a-zA-Z'-]+", text)
