class Example:
    static_value = 0

    def __init__(self , value):
        self.instance_value = value

    def add_total_object(n):
        Example.static_value = n
    
    def get_total_object():
        return Example.static_value

    @classmethod
    def class_method(cls):
        return f'我是類別方法，可以存取{cls.static_value}'

    def instance_method(self):
        return f'我是實例方法，可以存取{self.instance_value}'
    
if __name__ == '__main__':
    obj = Example('Instance Value')

    Example.add_total_object(15)

    print(Example.get_total_object())