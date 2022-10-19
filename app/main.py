from flask import Flask
import psycopg2
from service.test_ocr import TestOcr
from models.userModel import User
app = Flask(__name__)
app.debug = True

@app.route('/ocr', methods=['GET'])
def test_ocr():
    test = TestOcr()
    texte = test.test_pytesseract()
    test.test_easyocr()
    return texte

@app.route("/user", methods=['GET'])   
def getUser():
    user = User()
    info = user.getUser(1)
    print (info)
    return info