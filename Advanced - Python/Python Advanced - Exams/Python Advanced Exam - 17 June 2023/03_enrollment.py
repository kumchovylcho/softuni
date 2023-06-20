def gather_credits(credits_needed, *args):
    current_credits = 0
    enrolled_courses = set()
    for course, credits in args:
        if course in enrolled_courses:
            continue

        if current_credits < credits_needed:
            current_credits += credits
            enrolled_courses.add(course)

            if current_credits >= credits_needed:
                break

            continue

        break

    if credits_needed > current_credits:
        return f"You need to enroll in more courses! You have to gather {credits_needed - current_credits} credits more."

    output = []
    for course in sorted(enrolled_courses):
        output.append(course)

    # output = [course for course in sorted(enrolled_courses)]

    return f"Enrollment finished! Maximum credits: {current_credits}.\n" \
           f"Courses: {', '.join(output)}"