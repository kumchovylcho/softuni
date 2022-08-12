student_tickets = 0
standard_tickets = 0
kid_tickets = 0
people_counter = 0
name_of_movie = input()
while name_of_movie != "Finish":
    free_space_in_movie_hall = int(input())
    for movie in range(1, free_space_in_movie_hall + 1):
        type_of_tickets = input()
        if type_of_tickets == "student":
            student_tickets += 1
            people_counter += 1
        elif type_of_tickets == "standard":
            standard_tickets += 1
            people_counter += 1
        elif type_of_tickets == "kid":
            kid_tickets += 1
            people_counter += 1
        if type_of_tickets == "End" or people_counter >= free_space_in_movie_hall:
            movie_hall = people_counter / free_space_in_movie_hall * 100
            print(f"{name_of_movie} - {movie_hall:.2f}% full.")
            people_counter = 0
            break
    name_of_movie = input()
total_tickets = student_tickets + standard_tickets + kid_tickets
percentage_student_tickets = student_tickets / total_tickets * 100
percentage_standard_tickets = standard_tickets / total_tickets * 100
percentage_kid_tickets = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")
