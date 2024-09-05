class a:
    def __init__(self,b):
        self.b = b
    def __lt__(self,other):
        if (self.b<other.b):
            return "Object 1 is less than Object 2"
        else:
            return "Object 2 is less than Object 1"

object1 = a(1)
object2 = a(2)
print("Passed values", object1.b,object2.b)
print(object1.b < object2.b)