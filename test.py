class A:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return self.a
    
    def __repr__(self):
        return self.a

if __name__ == "__main__":
    a = A("dez")
    b = A("<vfbgdf")
    c = A("dcegvfdrfb")
    l = [a, b, c]
    print(l)
    for elem in l:
        print(str(elem) == "dez")