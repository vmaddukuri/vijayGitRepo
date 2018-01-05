class Application:
    """defined setters & getter for the private member"""
    def __init__(self):
        self.__name = None
        self.__version = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


if __name__ == '__main__':
    app = Application()
    print(app.name)  #
    app.name = "pip"  # set value to the property
    print(app.name)