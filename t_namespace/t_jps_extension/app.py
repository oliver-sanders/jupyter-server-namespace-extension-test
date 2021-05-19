import tornado

from jupyter_server.extension.application import ExtensionApp
from jupyter_server.base.handlers import JupyterHandler


class MyHandler(JupyterHandler):

    @tornado.web.authenticated
    def get(self):
        self.write('hello world')


class MyExtensionApp(ExtensionApp):

    name = 'test_namespace_extension'

    def initialize_handlers(self):
        self.handlers.extend([
            ('hello', MyHandler)
        ])


launch_instance = MyExtensionApp.launch_instance
