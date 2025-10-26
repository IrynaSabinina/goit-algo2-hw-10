# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)  # Set of subjects they can teach
        self.assigned_subjects = set()  # Set of subjects they are assigned to

    def assign_subject(self, subject):
        """Assign a subject to the teacher."""
        self.assigned_subjects.add(subject)

    def __str__(self):
        """Return a formatted string representation of the teacher."""
        return f"{self.first_name} {self.last_name}, {self.age} років, email: {self.email}"

# Функція для створення розкладу занять
def create_schedule(subjects, teachers):
    # Set to track which subjects have been covered
    covered_subjects = set()
    schedule = []

    while subjects:
        # Filter teachers who can still cover subjects
        available_teachers = [teacher for teacher in teachers if teacher.can_teach_subjects & subjects]
        
        if not available_teachers:
            # If no available teacher can cover any remaining subject
            return None
        
        # Sort teachers by the number of uncovered subjects they can teach and by age (youngest first)
        available_teachers.sort(key=lambda t: (-len(t.can_teach_subjects & subjects), t.age))
        
        # Take the best teacher
        best_teacher = available_teachers[0]
        
        # Assign as many subjects as possible from the remaining subjects to the best teacher
        for subject in list(subjects):
            if subject in best_teacher.can_teach_subjects:
                best_teacher.assign_subject(subject)
                subjects.remove(subject)
        
        # Add the teacher to the schedule
        schedule.append(best_teacher)

    return schedule

# Основна частина програми
if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    
    # Список викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
