class Student:
    def __init__(self, name, roll_number, cgpa):
      self.name=name
      self.roll_number=roll_number
      self.cgpa=cgpa

def sort_students(student_list):

  sorted_students = sorted(student_list,
                          key =lambda student:student.cgpa,reverse=True)
  return sorted_students
    
    
students = [
    Student("dinesh","cb45",10.0),
    Student("balaji","cb46",9.9),
    Student("kowshick","cb47",9.5),
    Student("boopathi","cb48",8.5)]


sorted_students=sort_students(students)
   
   
for student in sorted_students:
    print("Name: {},Roll Number: {},CGPA: {}".format(student.name, student.roll_number,student.cgpa))
   
   

 
    
    
    


 
