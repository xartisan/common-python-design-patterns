class LazyProperty:

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, instance, owner):
        if not instance:
            return None

        value = self.method(instance)
        setattr(instance, self.method_name, value)
        return value


class Test:

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print(f'Initializing self._resource which is {self._resource}')
        self._resource = tuple(range(5))
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)

    print(t.resource)
    print(t.resource)


if __name__ == '__main__':
    main()
