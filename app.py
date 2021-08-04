from InfineLoopMethod import main
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        args = request.args.get('q', default=1, type=int)
        newArgs = main(args)
    return render_template('index.html', newArgs=newArgs, args=args)


if __name__ == '__main__':
    app.run(debug=True)
