from app import create_app
from app.config import settings

app = create_app()

if __name__=='__main__':
    app.run(debug=settings.debug, port=settings.server_port)