import os 
from .encrypt import AES_Encrypt, generate_captcha_key, enc
from .reserve import reserve
import logging

def _fetch_env_variables(env_name, action):
    try:
        logging.info("_fetch_env_variables()")
        logging.info(f"action: {action}")
        logging.info(f"os.environ: {os.environ}")
        return os.environ[env_name] if action else ""
    except KeyError:
        logging.info(f"Environment variable {env_name} is not configured correctly.")
        return None

def get_user_credentials(action):
    usernames = _fetch_env_variables('USERNAMES', action)
    passwords = _fetch_env_variables('PASSWORDS', action)
    logging.info(f"get_user_credentials: usernames: {usernames}, passwords: {passwords}")
    return usernames, passwords