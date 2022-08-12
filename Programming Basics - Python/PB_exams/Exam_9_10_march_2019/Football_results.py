result_of_first_match = input()
result_of_second_match = input()
result_of_third_match = input()
wins = 0
loses = 0
draws = 0
if int(result_of_first_match[0]) > int(result_of_first_match[2]):
    wins += 1
elif int(result_of_first_match[2]) > int(result_of_first_match[0]):
    loses += 1
else:
    draws += 1
if int(result_of_second_match[0]) > int(result_of_second_match[2]):
    wins += 1
elif int(result_of_second_match[2]) > int(result_of_second_match[0]):
    loses += 1
else:
    draws += 1
if int(result_of_third_match[0]) > int(result_of_third_match[2]):
    wins += 1
elif int(result_of_third_match[2]) > int(result_of_third_match[0]):
    loses += 1
else:
    draws += 1
print(f"Team won {wins} games.\nTeam lost {loses} games.\nDrawn games: {draws}")
