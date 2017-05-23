# -*- coding: utf-8 -*-
from ExplainAsync import create_app
from manager import Manager

app = create_app()
manager = Manager()

@manager.command
def runserver():
    return app.run(host='0.0.0.0',
                   port=8000,
                   log_config=None)

if __name__ == '__main__':
    manager.main()
