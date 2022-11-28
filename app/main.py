#from service.userService import UserService
from flask import Flask, request, make_response, jsonify
from service.test_ocr import TestOcr
from models.model import db
from service.userService import UserService
from service.wineService import WineService
from models.users import Users
import jwt
from functools import wraps


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin2022@localhost:5432/urbanisation'

db.init_app(app)

with app.app_context():
    db.create_all()

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
    
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, '004f2af45d3a4e161a7dd2d17fdae47f', algorithms=["HS256"])
            current_user = Users.query.filter_by(uuid=data['uuid']).first()
        except:
            return jsonify({'message': 'token is invalid'})
    
        return f(current_user, *args, **kwargs)
    return decorator


# route users
@app.route("/login", methods=['POST'])
def login():
    data  = {
        'email': str(request.form.get("email")),
        'mdp': str(request.form.get("mdp")),
    }
    print(data)
    UserServ = UserService()
    return UserServ.login(data)

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


# test wine
@app.route("/wines", methods=['GET'])
@token_required
def insertWine(me):
    WineServ = WineService()
    return WineServ.getWines()
    # imagefile = flask.request.files.get('imagefile', '')
    
# @app.route("/user", methods=['GET'])   
# def getUser():
#     userId = int(request.args.get("user_id"))
#     if userId is None : 
#             return "l'id de l'utilisateur est érroné"
#     UserRepo = UserRepository()
#     info = UserRepo.getUser(userId)
#     return info


# test ocr
@app.route('/ocr', methods=['GET'])
@token_required
def test_ocr(me):
    print("test")
    test = TestOcr()
    texte = test.test_pytesseract()
    #test.test_easyocr()
    return texte