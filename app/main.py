from flask import Flask, request
from service.userService import UserService
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

# @app.route("/users", methods=['GET'])   
# def getUser():
#     UserRepo = UserRepository()
#     return UserRepo.getUsers()

@app.route("/user", methods=['POST'])
def insertUser():
        data  = {
            'nom': str(request.form.get("nom")),
            'prenom': str(request.form.get("prenom")),
            'email': str(request.form.get("email")),
            'mdp': str(request.form.get("mdp")),
        }
        UserServ = UserService()
        return UserServ.insertUser(data)

@app.route("/wine", methods=['POST'])
def insertWine():
    print(request.form)
    return "qzefs"
    # if nom or prenom is None :
    #     return "il ya un probleme avec le nom ou le prenom"
    

@app.route("/user", methods=['GET'])   
def getUser():
    userId = int(request.args.get("user_id"))
    if userId is None : 
            return "l'id de l'utilisateur est érroné"
    UserRepo = UserRepository()
    info = UserRepo.getUser(userId)
    return info