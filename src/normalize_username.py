import re


def normalize_username(value: str) -> str:
    cleaned = value.strip().lower()
    return re.sub(r"[^a-z0-9_-]", "", cleaned)
