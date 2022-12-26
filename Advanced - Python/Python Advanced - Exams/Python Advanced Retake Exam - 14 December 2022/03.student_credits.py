def students_credits(*args):
    student_results = {}
    for arg in args:
        course, credits_, max_points, d_points = [int(x) if x.isdigit() else x for x in arg.split("-")]
        credits_received = (d_points / max_points) * credits_
        student_results[course] = credits_received
    output = []
    all_of_diyans_credits = sum(student_results.values())
    if all_of_diyans_credits >= 240:
        output.append(f"Diyan gets a diploma with {all_of_diyans_credits:.1f} credits.")
    elif all_of_diyans_credits < 240:
        output.append(f"Diyan needs {240 - all_of_diyans_credits:.1f} credits more for a diploma.")
    for course, points in sorted(student_results.items(), key=lambda point: -point[1]):
        output.append(f"{course} - {points:.1f}")
    return '\n'.join(output)
