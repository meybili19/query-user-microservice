from flask import jsonify
from src.models.models import db, User

# Route to query user by ID
def get_all_users():
    try:
        
        users = User.query.all()

        if not users:
            return jsonify({'error': 'No users found'}), 404

        return jsonify([
            {
                'id': user.id,
                'identification': user.identification,
                'name': user.name,
                'email': user.email,
                'type': user.type,
                'created_at': user.created_at
            } for user in users
        ]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def query_user(id):
    try:
        user = User.query.get(id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'id': user.id,
            'identification': user.identification,
            'name': user.name,
            'email': user.email,
            'type': user.type,
            'created_at': user.created_at
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400