import re


def slugify(value: str) -> str:
    cleaned = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", cleaned)
    return slug.strip("-")
