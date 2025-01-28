from flask import Flask
from flask_cors import CORS
from src.config.config import Config
from src.models.models import db
from src.routes.routes import get_all_users

# Create the application
app = Flask(__name__)

CORS(app)

# Application configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the route to query user
@app.route('/users', methods=['GET'])
def get_users():
    return get_all_users()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
