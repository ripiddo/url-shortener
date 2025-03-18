from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from urlshortener import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('mysqldb', MigrateCommand)

if __name__ == '__main__':
    manager.run()
