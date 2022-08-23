class Party:
    def __init__(self):
        self.people = []


party = Party()
person_name = input()
while person_name != "End":
    party.people.append(person_name)
    person_name = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
