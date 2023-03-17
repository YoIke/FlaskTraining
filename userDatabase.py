class UserDatabase:
    def __init__(self):
        self.users = []
        self.next_id = 1

    # ユーザーを追加する関数
    def add_user(self, user):
        user['id'] = self.next_id
        self.users.append(user)
        self.next_id += 1

    # 全てのユーザーのリストを返す関数
    def get_users(self):
        return self.users

    # 特定のIDのユーザーを返す関数
    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return {'error': 'User not found'}

    # 特定のIDのユーザーを更新する関数
    def update_user(self, user_id, new_user):
        for user in self.users:
            if user['id'] == user_id:
                user.update(new_user)
                return user
