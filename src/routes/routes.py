from flask import jsonify
from src.models.models import db, User

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