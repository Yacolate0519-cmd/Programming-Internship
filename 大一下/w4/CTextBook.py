from CBook import CBook

class CTextBook(CBook):
    def __init__(self , title , publisher , cost_price , isbn , courseID , teacherID , universityID):
        super().__init__(title , publisher , cost_price , isbn)
        self.__courseID = courseID
        self.__teacherID = teacherID
        self.universityID = universityID

    @property
    def courseID(self):
        return self.__courseID
    
    @courseID.setter
    def setCourseID(self , newCourseID):
        self.__courseID = newCourseID
