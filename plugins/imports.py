from flask import Flask, url_for, request, render_template
from lxml import html
from lxml import etree
import lxml
import json
from urllib.parse import quote
from urllib.request import urlopen,Request
