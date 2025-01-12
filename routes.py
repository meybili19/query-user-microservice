from flask import jsonify
from models import db, User

# Route to query user by ID
def get_all_users():
    try:
        # Obtener todos los usuarios
        users = User.query.all()

        # Verificar si hay usuarios
        if not users:
            return jsonify({'error': 'No users found'}), 404

        # Retornar los datos de los usuarios
        return jsonify([
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password,
                'created_in': user.created_in
            } for user in users
        ]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Ruta para obtener un usuario por ID
def query_user(id):
    try:
        # Buscar el usuario por su ID
        user = User.query.get(id)

        # Verificar si el usuario existe
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Retornar los datos del usuario
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'created_in': user.created_in
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400