class CBArray:
    def __init__(self,content,dtpye=None):
        self.content = content
    def __add__(self,other):
        return self.__init__(self.content + other.content)
a = CBArray([2])

print(type(complex(0,1)))