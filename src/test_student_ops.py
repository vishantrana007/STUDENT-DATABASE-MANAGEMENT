from student_ops import (
    insert_student, 
    get_all_students, 
    find_student, 
    find_students_with_filter,
    update_student, 
    delete_student,
    create_indexes
)

# ------------------ INDEXING ------------------
print("=== CREATING INDEXES ===")
create_indexes()  # Run once for optimized retrieval
print()

# ------------------ CREATE ------------------
print("=== CREATE OPERATION ===")
student_id = insert_student({
    "name": "Vishant Rana",
    "age": 22,
    "course": {
        "name": "Python Backend",
        "duration": "3 months",
        "level": "Beginner"
    },
    "enrollment_date": "2025-09-30",
    "status": "active"
})
print(f"Inserted Student ID: {student_id}\n")

# ------------------ READ ------------------
print("=== READ OPERATION ===")
all_students = get_all_students()
print("All Students:")
for student in all_students:
    print(student)
print()

found_student = find_student({"name": "Vishant Rana"})
print("Find Student by Name:")
for student in found_student:
    print(student)
print()

# ------------------ ADVANCED QUERY (Filtering/Search) ------------------
print("=== ADVANCED QUERIES ===")

students_age_gt_20 = find_students_with_filter({"age": {"$gt": 20}})
print("Students with Age > 20:")
for student in students_age_gt_20:
    print(student)
print()

students_python_course = find_students_with_filter({"course.name": {"$regex": "^Python"}})
print("Students enrolled in Python Backend:")
for student in students_python_course:
    print(student)
print()

students_age_in_list = find_students_with_filter({"age": {"$in": [18, 22]}})
print("Students with Age 18 or 22:")
for student in students_age_in_list:
    print(student)
print()

# ------------------ UPDATE ------------------
print("=== UPDATE OPERATION ===")
updated_count = update_student(student_id, {"age": 23, "course.duration": "6 months"})
print(f"Number of records updated: {updated_count}\n")

# ------------------ DELETE ------------------
print("=== DELETE OPERATION ===")
deleted_count = delete_student(student_id)
print(f"Number of records deleted: {deleted_count}\n")

# ------------------ FINAL VERIFICATION ------------------
print("=== FINAL DATABASE STATE ===")
all_students_final = get_all_students()
for student in all_students_final:
    print(student)
