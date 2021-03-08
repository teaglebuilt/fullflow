from jupyter_server.utils import url_path_join
from extension.interface import APIHandler


def _jupyter_server_extension_points():
    return [{
        "module": "extension"
    }]


def _load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    web_app.add_handlers(
        host_pattern,
        [
            (
                url_path_join(web_app.settings['base_url'], r'/fullflow'), APIHandler
            )
        ]
    )