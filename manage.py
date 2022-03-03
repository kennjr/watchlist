from app import create_app, datab
from flask_script import Manager, Server
from app.models import User

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_ctx():
    return dict(app=app, db=datab, user=User)

if __name__ == '__main__':
    manager.run()
