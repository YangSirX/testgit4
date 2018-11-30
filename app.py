from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/index')
def index():
    stu_list=[
        {'name':'小明','age':16,'phone':'12431331'} ,
        {'name':'小明','age':15,'phone':'25341321'} ,
        {'name':'小明','age':14,'phone':'24313232'}
    ]
    return render_template('index.html',stu_list=stu_list)

if __name__ == '__main__':
    app.run()
