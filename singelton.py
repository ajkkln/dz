class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Пример использования
singleton1 = Singleton()
singleton2 = Singleton()

print(f"ID первого экземпляра: {id(singleton1)}")
print(f"ID второго экземпляра: {id(singleton2)}")
