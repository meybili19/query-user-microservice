from flask import Flask
from config import Config
from models import db
from routes import query_user

# Create the application
app = Flask(__name__)

# Application configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the route to query user
@app.route('/users/<int:id>', methods=['GET'])
def query_user_route(id):
    return query_user(id)

if __name__ == '__main__':
    app.run(debug=True)