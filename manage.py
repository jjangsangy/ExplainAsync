# -*- coding: utf-8 -*-
import os

from ExplainAsync import create_app
from manager import Manager

app = create_app()
manager = Manager()

@manager.command
def runserver():
    return app.run(host='0.0.0.0',
                   port=int(os.getenv('PORT', 8000)),
                   workers=4,
                   log_config=None)

if __name__ == '__main__':
    manager.main()
