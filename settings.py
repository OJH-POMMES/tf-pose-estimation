import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

KINTONE_TOKEN = os.environ.get("kintone_token")
KINTONE_DOMAIN = os.environ.get("kintone_domain")
KINTONE_APP = os.environ.get('kintone_app')
