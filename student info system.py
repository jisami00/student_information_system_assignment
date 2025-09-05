# Name: Jessa Mae R. Forrosuelo #
# Code: 2770                    #

import csv
import os

students = {}  
filename = "students.csv"

def display_menu():
    """Display the main menu"""
    print("\n=========== Student Information System =============")
    print("1. Add Student")
    print("2. Display Students") 
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")
    print("====================================================")

def add_student(student_id=None, name=None, age=None, grades=None):
    """Add a new student with default parameters"""
    global students
    
    if not student_id:
        student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists!")
        return
    
    if not name:
        name = input("Enter Name: ")
    if not age:
        age = int(input("Enter Age: "))
    if not grades:
        grades_input = input("Enter grades (comma-separated): ")
        grades = [float(x.strip()) for x in grades_input.split(',') if x.strip()]
    
    student_info = (student_id, name)
    students[student_id] = {
        'info': student_info,
        'age': age,
        'grades': grades
    }
    print(f"Student {name} added successfully!")

def display_students(*args, **kwargs):
    """Display all students with variable arguments"""
    global students
    
    if not students:
        print("No students found!")
        return
    
    print(f"\n{'ID':<10} {'Name':<15} {'Age':<5} {'Grades':<20} {'Average':<8}")
    print("-" * 65)
    
    
    for student_id, data in students.items():
        info_tuple = data['info']
        name = info_tuple[1]  # Accessing tuple element
        age = data['age']
        grades = data['grades']
        
        # average calculation
        calc_average = lambda grade_list: sum(grade_list) / len(grade_list) if grade_list else 0
        avg = calc_average(grades)
        
        
        grades_str = ""
        for i, grade in enumerate(grades):
            if i > 0:
                grades_str += ", "
            grades_str += str(grade)
        
        print(f"{student_id:<10} {name:<15} {age:<5} {grades_str:<20} {avg:<8.2f}")

def update_student():
    """Update student information"""
    global students
    
    if not students:
        print("No students to update!")
        return
    
    student_id = input("Enter Student ID to update: ")
    if student_id not in students:
        print("Student not found!")
        return
    
    print("Leave blank to keep current value:")
    current_data = students[student_id]
    
    # Update name diri
    new_name = input(f"Current name: {current_data['info'][1]} | New name: ")
    if new_name:
        # Update tuple by creating new one
        students[student_id]['info'] = (student_id, new_name)
    
    # update age 
    new_age = input(f"Current age: {current_data['age']} | New age: ")
    if new_age:
        students[student_id]['age'] = int(new_age)
    
    # update grades 
    print(f"Current grades: {current_data['grades']}")
    choice = input("(a)dd grade, (r)emove grade, (u)pdate all, or (s)kip: ").lower()
    
    if choice == 'a':
        new_grade = float(input("Enter new grade: "))
        students[student_id]['grades'].append(new_grade)  # List append
    elif choice == 'r':
        if current_data['grades']:
            grade_to_remove = float(input("Enter grade to remove: "))
            if grade_to_remove in current_data['grades']:
                students[student_id]['grades'].remove(grade_to_remove)  # List remove
    elif choice == 'u':
        new_grades = input("Enter all grades (comma-separated): ")
        students[student_id]['grades'] = [float(x.strip()) for x in new_grades.split(',')]
    
    print("Student updated successfully!")

def delete_student():
    """Delete a student record"""
    global students
    
    if not students:
        print("No students to delete!")
        return
    
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        name = students[student_id]['info'][1]
        del students[student_id]  # Dictionary deletion
        print(f"Student {name} deleted successfully!")
    else:
        print("Student not found!")

def save_to_file(filename=filename):
    """Save student data to CSV file"""
    global students
    
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Age', 'Grades'])  
            
            
            for student_id in students.keys():
                data = students[student_id]
                name = data['info'][1]
                age = data['age']
                grades_str = ','.join(map(str, data['grades']))
                writer.writerow([student_id, name, age, grades_str])
        
        print(f"Data saved to {filename} successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

def load_from_file(filename=filename):
    """Load student data from CSV file"""
    global students
    
    if not os.path.exists(filename):
        print(f"File {filename} not found!")
        return
    
    try:
        students.clear()  
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            
            for row in reader:
                if len(row) >= 4:
                    student_id, name, age, grades_str = row
                    grades = [float(x) for x in grades_str.split(',') if x]
                    
                    students[student_id] = {
                        'info': (student_id, name),
                        'age': int(age),
                        'grades': grades
                    }
        
        print(f"Data loaded from {filename} successfully!")
        print(f"Loaded {len(students)} students")
    except Exception as e:
        print(f"Error loading file: {e}")

def demonstrate_data_structures():
    """Demonstrate various data structure operations"""
    print("\n=== Data Structure Demonstrations ===")
    
    if students:
        # Tuple
        sample_student = next(iter(students.values()))
        info_tuple = sample_student['info']
        print(f"Tuple length: {len(info_tuple)}")
        
        # List 
        all_grades = []
        for data in students.values():
            all_grades.extend(data['grades'])  # List extend
        
        if all_grades:
            print(f"All grades: {all_grades}")
            print(f"Highest grade: {max(all_grades)}")
            print(f"Lowest grade: {min(all_grades)}")
            print(f"Grade slice [0:3]: {all_grades[0:3]}")  # List slicing
        
        # Dictionary ..
        print(f"Student IDs: {list(students.keys())}")
        print(f"Number of students: {len(students)}")

def main():
    """Main program loop"""
    print("YourName_2770 - Student Management System")
    
    load_from_file()
    
    while True:  
        display_menu()
        
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                add_student()
            elif choice == '2':
                display_students()
                demonstrate_data_structures()
            elif choice == '3':
                update_student()
            elif choice == '4':
                delete_student()
            elif choice == '5':
                save_to_file()
            elif choice == '6':
                load_from_file()
            elif choice == '7':
                save_to_file()  
                print("Thank you for using Student Management System!")
                break 
            else:
                print("Invalid choice! Please try again.")
                continue  
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Saving data...")
            save_to_file()
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__": main()