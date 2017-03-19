class Person:


    def __init__(self):
        print('생성자가 호출되었습니다.')
    def __init__(self, name, address, gender):
        self.name = name
        self.address = address
        self.gender = gender

    def print(self):
        return 'name:' + self.name + 'address:' + self.address + \
                'gender:' + self.gender

p1 = Person('yeom', 'seoul', 'male')
print(p1.print())