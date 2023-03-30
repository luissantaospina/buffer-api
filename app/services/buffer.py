class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Buffer(metaclass=SingletonMeta):
    buffer = []

    def get_buffer(self):
        return self.buffer
    
    def set_buffer(self, message):
        return self.buffer.append(message)
