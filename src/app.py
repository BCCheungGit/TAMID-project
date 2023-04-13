
# the file that we run to start the website
from src import create_app


#dunder main
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)