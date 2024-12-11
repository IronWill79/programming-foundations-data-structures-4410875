''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]
total_students = len(student_pet_count_list)
total_pets = 0

for count in student_pet_count_list:
  total_pets += count

average_pets = total_pets / total_students

print(average_pets)

