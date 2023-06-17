import random
import string
from temp_db import url_store

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(length))
        # Check if the generated short URL is already in use
        if short_url not in url_store:
            return short_url
