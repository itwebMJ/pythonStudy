class Member:
    def __init__(self, id='', pwd='', email=''):
        self.__id = id
        self.__pwd = pwd
        self.__email = email

    def __str__(self):
        return 'id : ' + self.__id + ' / pwd : ' + self.__pwd + ' / email : ' + self. __email

def main():
    m1 = Member('aaa', '111', 'aaa@email.com')
    m2 = Member('bbb', '222', 'bbb@email.com')
    m3 = Member('ccc', '333', 'ccc@email.com')

    print(m1)
    print(m2)
    print(m3)
main()
