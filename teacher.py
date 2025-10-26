class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)  # A set of subjects the teacher can teach
        self.assigned_subjects = set()  # Subjects assigned to the teacher
    
    def assign_subject(self, subject):
        self.assigned_subjects.add(subject)
