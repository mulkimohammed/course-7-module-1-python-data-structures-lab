# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    return (student for student in students if student[2] == major)
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    pass

    
