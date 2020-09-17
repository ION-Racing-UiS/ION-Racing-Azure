from flask import Flask, g
from config import Config
import os


app = Flask(__name__)
app.config.from_object(Config)

from app import routes