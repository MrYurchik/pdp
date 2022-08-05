"""
singleton
the singleton pattern is a software design pattern that restricts the instantiation of a class to one "single" instance. This is useful when exactly one object is needed to coordinate actions across the system.
Робимо клас з якого всі екземпляри будуть мати одну айдішку
"""
class Singleton:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance


a = Singleton()
b = Singleton()
print(f"Id a instance is {id(a)}. Id b instance is {id(b)}.")
print(a is b)
