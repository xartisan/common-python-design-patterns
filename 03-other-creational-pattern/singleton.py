class SingletonType(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonType, cls).__call__(
                *args, **kwargs)
        return cls._instance[cls]
