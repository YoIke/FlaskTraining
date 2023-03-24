class UserDatabase:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def add_user(self, user):
        if not all(key in user for key in ['name', 'email', 'password']):
            raise ValueError('User object must have name, email and password keys')
        user['id'] = self.next_id
        self.users[self.next_id] = user
        self.next_id += 1

    def get_users(self):
        return [user for user in self.users.values()]

    def get_user(self, user_id):
        return self.users.get(user_id, {'error': 'User not found'})

    def update_user(self, user_id, new_user):
        if not all(key in new_user for key in ['name', 'email', 'password']):
            raise ValueError('User object must have name, email and password keys')
        user = self.users.get(user_id, {})
        user.update(new_user)
        self.users[user_id] = user
        return user

    def delete_user(self, user_id):
        self.users.pop(user_id, None)
