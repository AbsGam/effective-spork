def validate(user_data):
    errors = {}
    
    # Достаем имя и убираем лишние пробелы
    name = user_data.get("name", "").strip()

    if not name:
        errors["name"] = "Вы должны заполнить эту строку!"
        
    return errors
