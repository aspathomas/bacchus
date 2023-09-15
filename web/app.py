import os
from flask import Flask
# from service.userService import UserService
from models.model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite://")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

#we define the route /
@app.route('/')
def welcome():
    # return a json
    print('test')
    return 'hello world'

# @app.route("/login", methods=['POST'])
# def login():
#     data  = {
#         'email': str(request.form.get("email")),
#         'mdp': str(request.form.get("mdp")),
#     }
#     print(data)
#     UserServ = UserService()
#     return UserServ.login(data)

# @app.route("/user", methods=['POST'])
# def insertUser():
#     data  = {
#         'nom': str(request.form.get("nom")),
#         'prenom': str(request.form.get("prenom")),
#         'email': str(request.form.get("email")),
#         'mdp': str(request.form.get("mdp")),
#     }
#     UserServ = UserService()
#     return UserServ.insertUser(data)

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))