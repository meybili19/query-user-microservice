from flask import jsonify
from models import db, User

# Route to query user by ID
def query_user(id):
    try:
        # Search for the user by its ID
        user = User.query.get(id)

        # Check if the user exists
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Return user data
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'created_in': user.created_in
            }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400