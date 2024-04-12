# (c) JigarVarma2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "25341679"))
	API_HASH = os.environ.get("API_HASH", "1a0656fa7566a46075cfe3f21676424c")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6966212073:AAFyS64VJhonSo6LTLl3SI2JE_UL2bw6M1c")
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ps133427:CXPgsWwW8oWDPTID@cluster0.y3itm2x.mongodb.net")
