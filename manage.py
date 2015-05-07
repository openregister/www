import os

from flask.ext.script import Server, Manager
from app import app

manager = Manager(app)
manager.add_option("-c", "--config", dest="config_filename", required=True)
port = int(os.environ.get('PORT', 8000))
manager.add_command("runserver", Server(host='0.0.0.0', port=port))

if __name__ == '__main__':
    manager.run()
