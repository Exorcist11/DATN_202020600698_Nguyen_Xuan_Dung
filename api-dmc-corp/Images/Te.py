import random
import string
import time

def generate_custom_id(prefix):
    timestamp = str(int(time.time()))
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{timestamp}-{random_chars}"

custom_id = generate_custom_id('USER')

print(custom_id)
