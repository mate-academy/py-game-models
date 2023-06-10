import sys
sys.path.append(r'D:\python_work\Mate Academy\Django_ORM\projects\py-game-models\venv\Lib\site-packages')

import os
import django

sys.dont_write_bytecode = True
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()
