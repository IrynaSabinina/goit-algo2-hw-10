def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_teacher_cover = 0

        for teacher in teachers:
            cover = len(teacher.can_teach_subjects & remaining_subjects)
            if cover > best_teacher_cover or (cover == best_teacher_cover and teacher.age < best_teacher.age):
                best_teacher = teacher
                best_teacher_cover = cover

        if not best_teacher:
            return None

        for subject in best_teacher.can_teach_subjects & remaining_subjects:
            best_teacher.assign_subject(subject)
            remaining_subjects.remove(subject)

        schedule.append(best_teacher)

    return schedule
