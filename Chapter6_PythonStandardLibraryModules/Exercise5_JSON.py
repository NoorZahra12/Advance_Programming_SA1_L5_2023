# Create a JSON file named 'StudentJson.json' with the following details

# Ask the user to enter the student name, ID, and course and write these contents to the JSON file. 2.Read the contents 
# from the JSON file and display the individual values.
# Expected Output :
# Details of the Student are
#   	Name: Alpha
#   	ID: 1
#   	course: BSc CC
# Append another dictionary as follows as key value pair for student 1 in StudentDetails dictionary to form a nested dictionay. 
# Later update the JSON file.
#  "CourseDetails":{ 
#              		 "Group": "A",
#              		 "Year": 2
# 		}
# Print the individual vlaues of the Student details reading from JSON file.
# Expected Output :

# Details of the Student are
# 		  Name: Alpha
# 		  ID: 1
#  		 course: BSc CC
#  		 Group: A
#  		 Year: 2

# importing json library
import json

# making a function to write student info in json file
def write_to_json():
    # empty dictionary for student
    student_details = {}

    # Ask the user to enter details
    student_details['Name'] = input("Enter student name: ")
    student_details['ID'] = int(input("Enter student ID: "))
    student_details['course'] = input("Enter student course: ")

    # Write the details to the JSON file
    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_details, json_file)

    print("Details of the Student are written to StudentJson.json.")

# Step 2: Read and display individual values from JSON file
def read_and_display():
    # Read the details from the JSON file
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    # Display individual values
    print("\nDetails of the Student are")
    print(f"    Name: {student_details['Name']}")
    print(f"    ID: {student_details['ID']}")
    print(f"    Course: {student_details['course']}")

# Step 3: Append and update JSON file with additional details
def append_and_update():
    # Read the existing details from the JSON file
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    # Append CourseDetails as a nested dictionary
    student_details['CourseDetails'] = {
        'Group': input("Enter group: "),
        'Year': int(input("Enter year: "))
    }

    # Update the JSON file with the appended details
    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_details, json_file)

    print("\nDetails of the Student are updated in StudentJson.json.")

# Step 4: Print individual values from the updated JSON file
def print_updated_details():
    # Read the updated details from the JSON file
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)

    # Display individual values including the new CourseDetails
    print("\nDetails of the Student are")
    print(f"    Name: {student_details['Name']}")
    print(f"    ID: {student_details['ID']}")
    print(f"    Course: {student_details['course']}")
    print(f"    Group: {student_details['CourseDetails']['Group']}")
    print(f"    Year: {student_details['CourseDetails']['Year']}")

# Step 1: Write student details to JSON file
write_to_json()

# Step 2: Read and display individual values from JSON file
read_and_display()

# Step 3: Append and update JSON file with additional details
append_and_update()

# Step 4: Print individual values from the updated JSON file
print_updated_details()
