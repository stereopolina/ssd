# lab work
# This Class violates all SOLID Principles, fix it in a Logical way ;
import abc
import ActionsInLife

class Hobby(ActionsInLife):
    def add_hobby(self, hobby: str) -> int:
        self.hobbies.append(hobby)
        return len(self.hobbies)



class Human(ActionsInLife):
    def __init__(self, name: str, nickname: str, hobbies=[]):
        if hobbies is None:
            hobbies = list()
        self.name = name
        self.nickname = nickname
        # self.salary = salary
        self.hobbies = hobbies

    def say_hello(self):
        pass

    def calculate_tax(self):  # is not related to human action, more to
                            # bureaucracy
        pass

    # def add_hobby(self, hobby: str) -> int:
    #     self.hobbies.append(hobby)
    #     return len(self.hobbies)


    def create_nickName(self, post_fix: str):
        self.nickname = self.name + post_fix

    # @abc.abstractmethod
    # def pray(self):
    #     pass
    #
    # @abc.abstractmethod
    # def play_sports(self):
    #     pass
    #
    # @abc.abstractmethod
    # def get_married(self):
    #     pass
    #
    # @abc.abstractmethod
    # def own_company(self):
    #     pass
    #
    # @abc.abstractmethod
    # def become_employee(self):
    #     pass


class Arabic(Human):
    def say_hello(self):
        return 'مرحبا'


class English(Human):
    def say_hello(self):
        return 'hello'


class Bureaucracy(Human):
    def __init__(self, salary: int):
        self.salary = salary


    def calculate_tax(self, percentage: int):
        pass
        salary = self.salary * percentage




human = Human()
human.say_hello('Arabic')