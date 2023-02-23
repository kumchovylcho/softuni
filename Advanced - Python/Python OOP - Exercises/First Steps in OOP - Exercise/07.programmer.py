class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int):
        if self.language == language:
            self.skills += skills_earned

            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int):
        if self.language == new_language:
            return f"{self.name} already knows {new_language}"

        if self.skills < skills_needed:
            return f"{self.name} needs {skills_needed - self.skills} more skills"

        old_language = self.language
        self.language = new_language

        return f"{self.name} switched from {old_language} to {new_language}"


# class Programmer:
#
#     def __init__(self, name, language, skills: int):
#         self.name = name
#         self.language = language
#         self.skills = int(skills)
#
#     def watch_course(self, course_name, language, skills_earned: int):
#         if self.language == language:
#             self.skills += int(skills_earned)
#             return f"{self.name} watched {course_name}"
#         return f"{self.name} does not know {language}"
#
#     def change_language(self, new_language, skills_needed: int):
#         if self.skills >= skills_needed and self.language != new_language:
#             old_language = self.language
#             self.language = new_language
#             return f"{self.name} switched from {old_language} to {new_language}"
#         elif self.skills >= skills_needed and self.language == new_language:
#             return f"{self.name} already knows {new_language}"
#         return f"{self.name} needs {skills_needed - self.skills} more skills"
