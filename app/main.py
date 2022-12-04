#from service.userService import UserService
from flask import Flask, request, make_response, jsonify, send_from_directory
from service.test_ocr import TestOcr
from models.model import db
from service.userService import UserService
from service.wineService import WineService
from service.commentaireService import CommentaireService
from service.noteService import NoteService
from service.processingPicture import ProcessingPicture
from models.users import Users
import jwt
from functools import wraps


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin2022@localhost:5432/urbanisation'
app.config['UPLOAD_FOLDER']='logs'

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

#-------------------------------------------#
# user
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

#-------------------------------------------#
# vin
# récupère les vins
@app.route("/wines", methods=['GET'])
def getWine():
    WineServ = WineService()
    return WineServ.getWines()

# met une description
@app.route("/wine/description", methods=['PUT'])
@token_required
def putDescription(me):
    data  = {
        'user': me,
        'wine_id': int(request.form.get("wine_id")),
        'description': str(request.form.get("description"))
    }
    WineServ = WineService()
    return WineServ.putDescription(data)

# met une description
@app.route("/wine/insert", methods=['POST'])
@token_required
def insertWine(me):
    data  = {
        'user': me,
        'nom': str(request.form.get("nom")),
        'region': str(request.form.get("region")),
        'couleur': str(request.form.get("couleur")),
        'est_petillant': bool(request.form.get("est_petillant")),
        'prix_moyen': int(request.form.get("prix_moyen")),
        'description': str(request.form.get("description")),
    }
    WineServ = WineService()
    return WineServ.insert(data)


#-------------------------------------------#
# commentaire
# commentaire depuis utilisateur
@app.route("/comments/user", methods=['POST'])
@token_required
def getCommentairesFromUser(me):
    user_id = int(request.form.get("user_id"))
    CommServ = CommentaireService()
    return CommServ.getFromUser(user_id)

# commentaire depuis vin
@app.route("/comments/wine", methods=['POST'])
def getCommentairesFromWine():
    wine_id = int(request.form.get("wine_id"))
    CommServ = CommentaireService()
    return CommServ.getFromWine(wine_id)

# ajouter un commentaire
@app.route("/comment", methods=['POST'])
@token_required
def insertCommentaire(me):
    data  = {
        'user': me,
        'wine_id': int(request.form.get("wine_id")),
        'commentaire': str(request.form.get("commentaire"))
    }
    CommServ = CommentaireService()
    return CommServ.insert(data)

# supprimer un commentaire
@app.route("/comment/delete", methods=['PUT'])
@token_required
def deleteCommentaire(me):
    data  = {
        'user': me,
        'commentaire_id': int(request.form.get("commentaire_id"))
    }
    CommServ = CommentaireService()
    return CommServ.delete(data)


#-------------------------------------------#
# note
# note depuis utilisateur
@app.route("/notes/user", methods=['POST'])
@token_required
def getNotesFromUser(me):
    user_id = int(request.form.get("user_id"))
    NoteServ = NoteService()
    return NoteServ.getFromUser(user_id)

# note depuis vin
@app.route("/notes/wine", methods=['POST'])
def getNotesFromWine():
    wine_id = int(request.form.get("wine_id"))
    NoteServ = NoteService()
    return NoteServ.getFromWine(wine_id)

# ajouter une note
@app.route("/note", methods=['POST'])
@token_required
def insertNote(me):
    data  = {
        'user': me,
        'wine_id': int(request.form.get("wine_id")),
        'note': int(request.form.get("note"))
    }
    NoteServ = NoteService()
    return NoteServ.insert(data)

# supprimer une note
@app.route("/note/delete", methods=['PUT'])
@token_required
def deleteNote(me):
    data  = {
        'user': me,
        'note_id': int(request.form.get("note_id"))
    }
    NoteServ = NoteService()
    return NoteServ.delete(data)

#-------------------------------------------#
# process
@app.route('/processing', methods=['POST'])
def process():
    file = request.files['file']
    processPicture = ProcessingPicture()
    return processPicture.process(file)

# test ocr
@app.route('/ocr', methods=['GET'])
@token_required
def test_ocr(me):
    print("test")
    test = TestOcr()
    texte = test.test_pytesseract()
    #test.test_easyocr()
    return texte