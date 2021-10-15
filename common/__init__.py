from .utils import get_config, FilePathTemplate
from .bot import MethodEnum

cfg = get_config()
fpt = FilePathTemplate()

APP_ID = cfg["APP_ID"]
APP_SECRET = cfg["APP_SECRET"]
APP_VERIFICATION_TOKEN = cfg["APP_VERIFICATION_TOKEN"]