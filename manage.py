#!/usr/bin/env python3
from flask_script import Manager
from app import create_app, config
from flask_migrate import Migrate, MigrateCommand
from app import db

app = create_app(config)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
