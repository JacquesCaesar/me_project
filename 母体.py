class ObjectView:
    """
        万物之父
    """
    def __init__(self):
        pass

    def main(self):
        pass

class ObjectModel:
    def __init__(self):
        pass

class ObjectController:
    def __init__(self):
        pass

if __name__ == '__main__':
    view = ObjectView()
    view.main()


class PeopleView:
    def __init__(self, ):
        self.__controller = PeopleController()

    def act(self):
        pass

    def touch(self):
        pass

    def see(self):
        pass

    def smell(self):
        pass

    def eat(self):
        pass

    def hear(self):
        pass

class PeopleController:
    def __init__(self):
        self.model=PeopleModel()

    def feel(self):
        pass

    def vision(self):
        pass

    def touch(self):
        pass

    def hearing(self):
        pass

    def smell(self):
        pass

    def taste(self):
        pass

class PeopleModel:
    def __init__(self):
        self.__data=[]

