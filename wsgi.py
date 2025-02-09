import os

# Detect if we're running via `flask run` and don't monkey patch
if not os.getenv("FLASK_RUN_FROM_CLI"):
    from gevent import monkey

    monkey.patch_all()

from CTFd import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False, threaded=True, host="0.0.0.0",
            port=8000, ssl_context=("/etc/ssl/server.crt", "/etc/ssl/server.key"))
