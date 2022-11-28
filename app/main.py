from flask import Flask, request
from service.userService import UserService
from repositories.UserRepository import UserRepository
from service.test_ocr import TestOcr
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY']='004f2af45d3a4e161a7dd2d17fdae47f'

# def token_required(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#         token = None
#         if 'x-access-tokens' in request.headers:
#             token = request.headers['x-access-tokens']
    
#         if not token:
#             return jsonify({'message': 'a valid token is missing'})
#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#             UserRepo = UserRepository()
#             current_user = UserRepo.getUserFromUuid(uuid=data['public_id'])
#         except:
#             return jsonify({'message': 'token is invalid'})
    
#         return f(current_user, *args, **kwargs)
#     return decorator


# test ocr
@app.route('/ocr', methods=['GET'])
def test_ocr():
    test = TestOcr()
    texte = test.test_pytesseract()
    test.test_easyocr()
    return texte

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

@app.route("/login", methods=['POST'])
def login():
    data  = {
        'email': str(request.form.get("email")),
        'mdp': str(request.form.get("mdp")),
    }
    print(data)
    UserServ = UserService()
    return UserServ.login(data)

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