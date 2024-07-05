import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no=0):
      real = self.real + no.real
      imaginary = self.imaginary + no.imaginary
      return str(self.__class__(real, imaginary))
    def __sub__(self, no=0):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return str(self.__class__(real, imaginary))
    #(a+bi)(c+di) = a*c + a*di + bi*c + bdi^2
    def __mul__(self, no=0):
        real = (self.real * no.real) + (self.imaginary * no.imaginary)*(-1)
        imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        return str(self.__class__(real, imaginary))
    #(a+bi)/(c+di) * (c-di)/(c-di) =  a*c + a*di + bi*c + bdi^2 / c^2 - d^2i^2
    def __truediv__(self, no=0):
        real = ((self.real * no.real) + (self.imaginary * (-no.imaginary))*(-1))/((no.real**2) + (no.imaginary**2))
        imaginary = ((self.real * (-no.imaginary)) + (self.imaginary * -no.real)*(-1))/((no.real**2) + (no.imaginary**2))
        return str(self.__class__(real, imaginary))
    #|(a+bi)|^2 = (a+bi)(a-bi) = (a^2 + b^2)^1/2
    def mod(self):
        real = (self.real**2 + self.imaginary**2)**(1/2)
        return str(self.__class__(real, 0))
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
#x-y, x*y, x/y, x.mod(), y.mod()
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [y.__add__(x), x.__sub__(y), x.__mul__(y), x.__truediv__(y), x.mod(), y.mod()]), sep='\n')
