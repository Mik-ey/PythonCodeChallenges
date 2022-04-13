class Calculator:
    def __init__(self, *args):
        self.handled_exceptions = args
        self.error = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.error = exc_type
        return isinstance(exc_type, self.handled_exceptions)
