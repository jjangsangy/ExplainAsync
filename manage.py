# -*- coding: utf-8 -*-
import os
import multiprocessing

from ExplainAsync import create_app
from manager import Manager

app = create_app()
manager = Manager()

@manager.command
def runserver():
    return app.run(host=os.getenv('HOST', '127.0.0.1'),
                   port=int(os.getenv('PORT', 8000)),
                   workers=multiprocessing.cpu_count())

if __name__ == '__main__':
    manager.main()
