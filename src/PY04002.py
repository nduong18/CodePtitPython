import sys
class Rectangle:
    def __init__(self, cd, cr, ms):
        self.cd = cd
        self.cr = cr
        self.ms = ms

    def perimeter(self):
        return (self.cd + self.cr) * 2
    def area(self):
        return self.cd * self.cr
    def color(self):
        return self.ms.title()


x,y,z = input().split()
if int(x) > 0 and int(y) > 0:
    r = Rectangle(int(x), int(y), z)
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')
sys.exit()

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))