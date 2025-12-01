from application import create_app

import os


if __name__ == "__main__":
    app = create_app()

    app.debug = True

    from livereload import Server

    server = Server(app)

    server.watch("application/__init__.py")
    server.watch("application/main_routes.py")
    server.watch("application/csv_handler_routes.py")
    server.watch("application/templates/")
    server.watch("application/static/")
    server.serve(
        port=int(os.environ.get("PORT", 5000)), host="127.0.0.1", restart_delay=1
    )
