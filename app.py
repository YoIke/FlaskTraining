from flask import Flask, jsonify, request
from userDatabase import UserDatabase

app = Flask(__name__)

# データベースオブジェクトの初期化
usersDb = UserDatabase()

user1 = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'password': 'password123'
}

user2 = {
    'name': 'Bob',
    'email': 'bob@example.com',
    'password': 'password456'
}

user3 = {
    'name': 'Charlie',
    'email': 'charlie@example.com',
    'password': 'password789'
}

usersDb.add_user(user1)
usersDb.add_user(user2)
usersDb.add_user(user3)


# ユーザーを追加するためのエンドポイント
@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    usersDb.add_user(user)
    return jsonify(user), 201


# ユーザーのリストを返すエンドポイント
@app.route('/users', methods=['GET'])
def get_users():
    users = usersDb.get_users()
    return jsonify(users)


# 特定のユーザーを取得するエンドポイント
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = usersDb.get_user(user_id)
    return jsonify(user)


# 特定のユーザーを更新するためのエンドポイント
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.json
    updated_user = usersDb.update_user(user_id, user)
    return jsonify(updated_user)


# 特定のユーザーを削除するためのエンドポイント
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    usersDb.delete_user(user_id)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
