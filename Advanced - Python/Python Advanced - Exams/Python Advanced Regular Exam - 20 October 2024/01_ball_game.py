from collections import deque


def main(strengths: list[int], accuracies: deque[int], points_to_score_goal: int) -> list[str]:
    scored_goals = 0

    while strengths and accuracies:
        last_strength = strengths.pop()
        first_accuracy = accuracies.popleft()

        sum_of_strength_and_acc = last_strength + first_accuracy
        if sum_of_strength_and_acc == points_to_score_goal:
            scored_goals += 1
        elif sum_of_strength_and_acc < points_to_score_goal:
            if last_strength > first_accuracy:
                strengths.append(last_strength)
            elif last_strength < first_accuracy:
                accuracies.appendleft(first_accuracy)
            elif last_strength == first_accuracy:
                strengths.append(sum_of_strength_and_acc)
        elif sum_of_strength_and_acc > points_to_score_goal:
            strengths.append(last_strength - 10)
            accuracies.append(first_accuracy)

    output = []
    if scored_goals == 3:
        output.append("Paul scored a hat-trick!")
    elif not scored_goals:
        output.append("Paul failed to score a single goal.")
    elif scored_goals >= 3:
        output.append("Paul performed remarkably well!")
    elif 0 < scored_goals < 3:
        output.append("Paul failed to make a hat-trick.")

    if scored_goals:
        output.append(f"Goals scored: {scored_goals}")

    if strengths:
        output.append(f"Strength values left: {', '.join(str(x) for x in strengths)}")
    if accuracies:
        output.append(f"Accuracy values left: {', '.join(str(x) for x in accuracies)}")

    return output


result = main(
    [int(x) for x in input().split()],
    deque(int(x) for x in input().split()),
    100
)

print("\n".join(result))
