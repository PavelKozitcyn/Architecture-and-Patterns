import os
from wsgiref.simple_server import make_server
from wsgi_static_middleware import StaticMiddleware

from design_framework.main import Framework
from urls import routes, fronts

BASE_DIR = os.path.dirname(__name__)
STATIC_DIRS = [os.path.join(BASE_DIR, 'templates/style')]

application = Framework(routes, fronts)

app_with_static = StaticMiddleware(application, static_root='style', static_dirs=STATIC_DIRS)

with make_server('', 8080, app_with_static) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()

# from wsgiref.simple_server import make_server
#
# from design_framework.main import Framework
# from urls import routes, fronts
#
#
# application = Framework(routes, fronts)
#
# with make_server('', 8080, application) as httpd:
#     print("Запуск на порту 8080...")
#     httpd.serve_forever()
