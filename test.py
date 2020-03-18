# # class Animal(object):
# #     def run(self):
# #         print('animal is running......')
# # class Dog(Animal):
# #     def run(self):
# #         print('dog is running....')
# # class Cat(Animal):
# #     def run(self):
# #         print('cat is running....')
# # class Timer(object):
# #     def run(self):
# #         print('is not Animal is running....')
# # d = Dog()
# # c = Cat()
# # d.run()
# # c.run()
# # te = Animal(Timer)
# # te.run()
# # class Student(object):
# #     def __int__(self,name,score):
# #         self.name = name
# #         self.score = score
# #     def set_score(self):
# #         self.
# # # s = Student()
# #廖雪峰课程使用property
class Screen(object):
    @property
    def width(self):
        self._width
    @width.setter
    def width(self,value):
        self._width = value
    @property
    def height(self):
        self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return 786432

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')