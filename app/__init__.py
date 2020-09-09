from flask import Flask
# import sys

app = Flask(__name__)
# print(sys.path)
from app import routes