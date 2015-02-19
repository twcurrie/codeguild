class A(object):
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        super(B,self).m()
    
class C(A):
    def m(self):
        print("m of C called")
        super(C,self).m()

class D(B,C):
    def m(self):
        print("m of D called")
        super(D,self).m()
