from model import solution
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def main():
    return render_template('/index.html')

@app.route('/get')
def get():
    return render_template('/get.html')

@app.route('/post', methods=['POST'])
def post():
    if(request.method == 'POST'):
        file = request.files['file']
        if not file: return render_template('/index.html')
        filename = file.filename
        img_path = 'flask/static/images/' + str(filename)
        file.save(img_path)

        label, prob = solution(img_path)
        return render_template('/post.html', img_path=img_path[6:], label=label, prob=prob)

app.run(debug=True)