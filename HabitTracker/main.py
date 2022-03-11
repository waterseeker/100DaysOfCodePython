import os
from dotenv import load_dotenv
import requests

load_dotenv()
TEST_ENV_VARIABLE = os.getenv('TEST_ENV_VARIABLE')
print(TEST_ENV_VARIABLE)

# requests.post()
