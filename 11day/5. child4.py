#메서드 재정의 : 부모로부터 상속받은 메서드를 현재 클래스에 맞게 수정하여 사용.
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print('x : ', self.x, ', y : ', self.y, end='')

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # 메서드 재정의. 부모가 준 메서드 자기 한테 맞게 고쳐씀
    def printPoint(self):
        super().printPoint()
        print( ', z : ', self.z)
    # 함수 재정의
#   def printPoint(self):
#       print('x : ', self.x, ', y : ', self.y, ', z : ', self.z)

def main():
    p1 = Point2D(1, 2)
    p1.printPoint()
    print()

    p2 = Point3D(4, 5, 6)
    p2.printPoint()

main()
