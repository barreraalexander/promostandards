from app import create_app
from app.config import settings

flask_app = create_app()

if __name__=='__main__':
    # flask_app.run(debug=settings.debug, port=settings.server_port)
    flask_app.run(debug=settings.debug, port=settings.server_port, host= '0.0.0.0')