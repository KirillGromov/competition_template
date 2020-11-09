from app import app
from app.config import Configurations



if __name__ == "__main__":
    app.secret_key ="12345678qwerty"
    app.run(debug = True)
