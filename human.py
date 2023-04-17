
class Human:
    def __init__(self, str_: str, int_: int, bool_: bool) -> None:
        self.str_ = str_
        self.int_ = int_
        self.bool_ = bool_


class Student(Human):
    def __init__(self, human: Human, school: str) -> None:
        self.human = human
        self.school = school

    def study(self):
        print(f'I\'m studying in {self.school}')


def main_loop():
    person = Human("abcdefg", 12345, True)
    student = Student(person, 'KNTU')
    student.study()
    if person.bool_ == True:
        return (person.str_)
    elif person.bool_ == False:
        return (person.int_)


if __name__ == '__main__':
    main_loop()
