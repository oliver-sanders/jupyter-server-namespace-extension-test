from t_namespace.t_jps_extension.app import MyExtensionApp


def _jupyter_server_extension_points():
    """
    Returns a list of dictionaries with metadata describing
    where to find the `_load_jupyter_server_extension` function.
    """
    return [
        {
            "module": "t_namespace.t_jps_extension.app",
            "app": MyExtensionApp
        }
    ]
