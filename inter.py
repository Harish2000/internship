from flask import Flask, jsonify, request,make_response
app = Flask(__name__)

@app.route('/', methods=['POST'])
def login():
    username=request.json['username']
    password=request.json['password']
    if(username=="vaibhav" and password=="abcd12"):
        d={"msg":"Success","status":"200"}
        return make_response(jsonify(d))
    elif(username=="vaibhav" and password=="abcd"):
        d={"msg":"Failure: password should be of length 6","status":"201"}
        return make_response(jsonify(d))
    elif(username=="vaibhav" and password=="abcdef"):
        d={"msg":"Failure: password to have 1 character and 1 number","status":"202"}
        return make_response(jsonify(d))
    elif(username=="1234" and password=="abcd12"):
        d={"msg":"Failure: only characters allowed in username","status":"203"}
        return make_response(jsonify(d))
if __name__ == '__main__':
    app.run(debug=True)