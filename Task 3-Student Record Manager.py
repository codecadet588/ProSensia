# day3_student_record_manager.py

def add_student(record_set, name, grade):
    """Add a new student as a tuple if name is unique"""
    if not name or not grade.isdigit():
        return record_set
    grade = int(grade)
    # Ensure unique student names
    record_set = {r for r in record_set if r[0].lower() != name.lower()}
    record_set.add((name.capitalize(), grade))
    return record_set

def view_all_students(record_set):
    """Print all student records"""
    for name, grade in sorted(record_set, key=lambda x: x[1], reverse=True):
        print(f"{name}: {grade}")

def get_top_student(record_set):
    """Return student with highest grade"""
    return max(record_set, key=lambda x: x[1], default=None)

def filter_students(record_set, min_grade):
    """Return students above a certain grade"""
    return [s for s in record_set if s[1] >= min_grade]

records = set()

while True:
    entry = input('Enter "Name, Grade" or type exit: ').strip()
    if entry.lower() == "exit":
        break
    try:
        name, grade = [x.strip() for x in entry.split(",")]
        records = add_student(records, name, grade)
    except ValueError:
        print("Invalid format. Use: Name, Grade")

print("\nAll Students:")
view_all_students(records)

top_student = get_top_student(records)
if top_student:
    print(f"\nTop Student: {top_student[0]} with {top_student[1]}")

if records:
    grades = [g for _, g in records]
    avg = sum(grades) / len(grades)
    above_avg = filter_students(records, avg)
    print(f"\nTotal Students: {len(records)}")
    print(f"Class Average: {avg:.2f}")
    print("Students above average:", ", ".join([s[0] for s in above_avg]))
