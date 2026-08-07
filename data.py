class UserRepository:
    def __init__(self):
        # Тот самый список пользователей []
        self.users = []
        self._next_id = 1

    def save(self, user_data: dict):
        """Принимает словарь с данными и сохраняет его в список"""
        # Добавляем ID к пришедшим данным
        user_data['id'] = self._next_id
        
        # Кладем готовый словарь в список []
        self.users.append(user_data)
        
        self._next_id += 1
        return user_data

    def get_all(self):
        return self.users

