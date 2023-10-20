class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.srgr = float()

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_attached and course in lecture.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        lyst=[]
        for k in self.grades:
             grades_count += len(self.grades[k])
             lyst.extend(k)
        return float(sum(lyst)/max(len(lyst), 1))

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f'Имя:{self.name}\n' \
               f'Фамилия:{self.surname}\n' \
               f'Средняя оценка за домашнее задание:{self.srgr}\n' \
               f'Курсы в процессе обучени:{courses_in_progress_string}\n' \
               f'Завершенные курсы:{finished_courses_string}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.srgr = float()
        self.courses_in_progress = []

    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        lyst = []
        for k in self.grades.values():
           grades_count += len(self.grades[k])
           lyst.extend(k)
        return float(sum(lyst)/max(len(lyst), 1))

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.srgr}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr < other.srgr


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

lecturer_1 = Lecturer('Kirill', 'Makarov')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Petr', 'Kulakov')
lecturer_2.courses_attached += ['Python']
lecturer_3 = Lecturer('Sergey', 'Zarev')
lecturer_3.courses_attached += ['Python']

cool_rewiewer_1 = Reviewer('Some', 'Buddy')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']
cool_rewiewer_2 = Reviewer('Ostap', 'Bender')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']

student_1 = Student('Denis', 'Sviridov', 'Man')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Roman', 'Malikov', 'Man')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']
student_3 = Student('Sidor', 'Petrov', 'Man')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Python', 5)
student_1.rate_lecture(lecturer_2, 'Python', 7)
student_1.rate_lecture(lecturer_2, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 7)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Python', 9)
student_3.rate_lecture(lecturer_3, 'Python', 5)
student_3.rate_lecture(lecturer_3, 'Python', 6)
student_3.rate_lecture(lecturer_3, 'Python', 7)
cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(student_1, 'Python', 10)
cool_rewiewer_2.rate_hw(student_2, 'Python', 8)
cool_rewiewer_2.rate_hw(student_2, 'Python', 7)
cool_rewiewer_2.rate_hw(student_2, 'Python', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print(f'Перечень лекторов:\n\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print()
print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {str(student_1) > str(student_2)}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()


student_list = [student_1, student_2, student_3]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]
def student_rating(student_list, course_name):
    sum_all = 0
    count_all = [0]
    for study in student_list:
        if study.courses_in_progress == [course_name]:
            sum_all += len(student_list[study])
            count_all.extend(study)
    return float(sum(count_all)/max(len(count_all), 1))

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = [0]
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += len(lecturer_list[lect])
            count_all.extend(lect)
    return float(sum(count_all)/max(len(count_all), 1))

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
