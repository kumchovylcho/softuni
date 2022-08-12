number = int(input())
cuts = number - 2
print("+ " + cuts * "- " + "+")
for col in range(number - 2):
    print("| " + cuts * "- " + "|")
print("+ " + cuts * "- " + "+")