from flask import Flask
# the file that we run to start the website
from website import create_app

app = Flask(__name__)

#dunder main
if __name__ == '__main__':
    app1 = create_app(app)
    app1.run(debug=True)