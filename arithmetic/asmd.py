from arithmetic.complex import Complex

class ArithmeticOperations:
    def __init__(self):
        pass

    @staticmethod
    def __add__(C1,C2):
        x1=C1.real
        y1=C1.imaginary
        x2=C2.real
        y2=C2.imaginary
        x=x1+x2
        y=y1+y2
        C=Complex(x,y)
        return C

    @staticmethod
    def __sub__(C1,C2):
        x1=C1.real
        y1=C1.imaginary
        x2=C2.real
        y2=C2.imaginary
        x=x1-x2
        y=y1-y2
        C=Complex(x,y)
        return C

    @staticmethod
    def __mul__(C1,C2):
        x1=C1.real
        y1=C1.imaginary
        x2=C2.real
        y2=C2.imaginary
        x=x1*x2 + y1*y2
        y=x2*y1-x1*y2
        C=Complex(x,y)
        return C

    @staticmethod
    def __div__(C1,C2):
        if C2==0:
            raise ValueError("division by zero not permitted")
        else:
            x1=C1.real
            y1=C1.imaginary
            x2=C2.real
            y2=C2.imaginary
            r2=(x2**2)+(y2**2)
            x=(x1*x2 - y1*y2)/r2
            y=(x1*y2 + x2*y1)/r2
            C=Complex(x,y)
            return C
            
            

