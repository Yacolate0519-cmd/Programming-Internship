class CStudent:
    def __init__(self , id , name , deparment , email , birthday):
        self.id = id
        self.name = name
        self.deparment = deparment
        self.__email = email
        self.__birthday = birthday

    
if __name__ == '__main__':
    student1 = CStudent("S109102345" , '張三' , "IECS" , "zs100232@gmail.com" , "2000-02-02")
    student1 = CStudent("S109104533" , '李四' , "IECS" , "ktr002222@gmail.com" , "2004-03-22")
    student1 = CStudent("S109123346" , '張三' , "IECS" , "zs100232@gmail.com" , "1999-04-22")
    student1 = CStudent("S109102355" , '張三' , "IECS" , "zkkse0252@gmail.com" , "2001-05-10")
    student1 = CStudent("S109102785" , '張三' , "IECS" , "zsf23s3d@gmail.com" , "2002-06-04")