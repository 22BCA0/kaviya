class Student:

  def __init__(self, name,              roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa 


def sort_Students (student_list):
#Sort the just of students in           deascending order of CGPA
    sorted_students =                    sorted(student_list,
               key=lambda student:               student.cgpa, reverse=True)
  #Syntax - lambda arg:exp
    return sorted_students


# Examples usage:
Students = [
Student ("Hari", "A123", 7.8),
Student ("Srikanth", "A124", 8.9),
Student ("Saumya", "A125", 9.1),
Student ("Mahidhar", "A126", 9.9),
]

sorted_students = sort_Students         (Students)

sorted_students =                       sort_Students(Students)

#print the sorted list of students

for student in sorted_students:

  print("Name: {}, Roll Number: {},      CGPA: {}".format(student.name,
                                        
student.roll_number,
                    student.cgpa))