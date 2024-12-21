class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

def calculate_averages(students):
    averages = {}
    for name, marks in students.items():
        student = Student(name, marks)
        averages[name] = round(student.average(), 2)
    return averages

def find_top_performer(averages):
    top_student = max(averages, key=averages.get)
    return top_student

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average_marks = calculate_averages(students)
top_performer = find_top_performer(average_marks)
print("Average Marks:", average_marks)
print("Top Performer:", top_performer)