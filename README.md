# goit-algo2-hw-10

The program will assign lecturers to subjects based on the greedy algorithm described below. If all subjects are successfully covered, it will print the schedule with lecturers and their assigned subjects. If it's not possible to cover all subjects, it will display a message indicating the failure.

### File Structure

Here is a breakdown of the key files in this project:

goit-algo2-hw-10/
│
├── main.py          # The main script to execute the scheduling process
├── schedule.py      # Contains the logic for assigning lecturers to subjects
└── teacher.py       # Contains the definition of the Teacher class

**main.py**

This is the main entry point of the program. It initializes the subjects, teachers, and calls the create_schedule function to generate the schedule.

**schedule.py**

Contains the create_schedule function that implements the greedy algorithm for assigning lecturers to subjects.

**teacher.py**

Defines the Teacher class with attributes like name, age, email, and a set of subjects the teacher can teach. It also contains the logic for assigning subjects to teachers.

## Algorithm Explanation
### Greedy Approach:

The greedy algorithm is used to minimize the number of lecturers needed while ensuring all subjects are taught. The steps are as follows:

Input: A list of subjects and a list of teachers with their available subjects.

Selection: At each step, select the teacher who can teach the most number of subjects that are still uncovered. If there are multiple candidates, select the youngest teacher (based on age).

Assignment: Assign the selected teacher to all subjects they can cover and remove these subjects from the list of uncovered subjects.

Repeat: Continue this process until all subjects are covered or no teacher can cover the remaining subjects.

Output: A list of teachers and the subjects they are assigned to.

### Criteria:

If it's not possible to cover all subjects with the available teachers, the program outputs a message saying it cannot generate a valid schedule.