from flask import Flask,request,current_app
app = Flask(__name__)




@app.route('/')
def index():
    with app.test_request_context('/'):
        a = request.path
        b = request.method
        c = current_app.name
    print(a)
    print(b)
    print(c)
    return 'Home Page'


@app.route('/career/')
def career():
    with app.test_request_context('/'):
        a = request.path
        b = request.method
        c = current_app.name
    print(a)
    print(b)
    print(c)
    return 'Career Page'


@app.route('/feedback/')
def feedback():
    with app.test_request_context('/'):
        a = request.path
        b = request.method
        c = current_app.name
    print(a)
    print(b)
    print(c)
    return 'Feedback Page'


@app.route('/user/<id>')
def user_profile(id):
    with app.test_request_context('/'):
        a = request.path
        b = request.method
        c = current_app.name
    print(a)
    print(b)
    print(c)
    return "Profile page of user #{}".format(id)

if __name__ == "__main__":
    app.run(debug=True)