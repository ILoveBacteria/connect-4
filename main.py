from server import app
import os

if __name__ == '__main__':
    app.run(host=os.environ.get('HOST_ADDR', None), debug=os.environ.get('DEBUG', None))
