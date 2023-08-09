def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    :param collection: словарь
    :param key: ключ
    :param default: значение по умолчанию
    :return: значение по ключу
    """
    return collection.get(key, default)
