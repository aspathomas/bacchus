from flask import Flask, request
from repositories.UserRepository import UserRepository
from service.test_ocr import TestOcr

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
    userId = int(request.args.get("user_id"))
    if userId is None : 
            return "l'id de l'utilisateur est érroné"
    UserRepo = UserRepository()
    info = UserRepo.getUser(userId)
    return info

@app.route("/user", methods=['POST'])
def insertUser():
    nom = str(request.form.get("nom"))
    prenom = str(request.form.get("prenom"))
    print(nom)
    print(prenom)
    # if nom or prenom is None :
    #     return "il ya un probleme avec le nom ou le prenom"
    UserRepo = UserRepository()
    isInsert = UserRepo.insertUser(nom, prenom)
    if isInsert is True: 
        return "reussi"
    
    return "echec"