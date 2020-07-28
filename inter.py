from flask import Flask, jsonify, request,make_response
app = Flask(__name__)

@app.route('/', methods=['POST'])
def login():
    username=request.json['username']
    password=request.json['password']
    a="1234567890"
    b="qwertyuiopasdfghjklzxcvbnm"
    integer=0
    character=0
    for i in password:
        if(i in a):
            integer=1
        elif i in b:
            charater=1
        if(integer==1 and character==1):
            break
    user_check=0
    for i in username:
        if i not in b:
            user_check=1
            break
    if(user_check==1):
        d={"status":"203","msg":"Failure: only characters allowed in username"}
        return make_response(jsonify(d))
    elif(len(password)<6):
        d={"status":"201","msg":"Failure: password should be of length 6"}
        return make_response(jsonify(d))
    elif(integer==0 or character==0):
        d={"status":"202","msg":"Failure: password to have 1 character and 1 number"}
        return make_response(jsonify(d))
    else:
        d={"status":"200","msg":"Success"}
        return make_response(jsonify(d))

if __name__ == '__main__':
    app.run(debug=True)
