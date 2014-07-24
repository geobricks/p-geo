from flask import Blueprint
from flask import Flask
from flask import Response
from flask.ext.cors import cross_origin
from utils import config as c
from ftplib import FTP
import json

browse = Blueprint('browse', __name__)

@browse.route('/')
def index():
    return 'Welcome to the Browse module!'

@browse.route('/<source_name>')
@cross_origin(origins='*')
def list_products(source_name):
    config = c.Config(source_name.upper())
    ftp = FTP(config.json['source']['ftp']['base_url'])
    ftp.login()
    ftp.cwd(config.json['source']['ftp']['data_dir'])
    l = ftp.nlst()
    ftp.quit()
    return Response(json.dumps(l), content_type = 'application/json; charset=utf-8')