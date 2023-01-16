class Intersection:

    def __init__(self, lines_of_info: int):
        self.lines_of_info = lines_of_info
        self.longest_intersection = []

    def read_ranges(self):
        for _ in range(self.lines_of_info):
            range_one, range_two = self.split_data(input())
            self.check_intersections(range_one, range_two)

    @staticmethod
    def split_data(first_and_second_ranges: str):
        data = first_and_second_ranges.split("-")
        first_range, second_range = [int(x) for x in data[0].split(",")], [int(x) for x in data[1].split(",")]
        return first_range, second_range

    def check_intersections(self, first_r: list, second_r: list):
        first_start, first_end = first_r
        second_start, second_end = second_r
        first_set = set(range(first_start, first_end + 1))
        second_set = set(range(second_start, second_end + 1))
        check_longest_intersection = first_set.intersection(second_set)
        if len(self.longest_intersection) < len(check_longest_intersection):
            self.longest_intersection = check_longest_intersection

    def __repr__(self):
        return f"Longest intersection is [{', '.join(str(x) for x in self.longest_intersection)}]" \
               f" with length {len(self.longest_intersection)}"


intersection = Intersection(int(input()))
intersection.read_ranges()
print(intersection)



# lines = int(input())   # not my solution
# max_intersection = 0
# combined_intersection = set()
# set_a = set()
# set_b = set()
#
# for i in range(lines):
#     data = input().split("-")
#     range_1 = [int(i) for i in data[0].split(",")]
#     range_2 = [int(i) for i in data[1].split(",")]
#     for i in range(range_1[0], range_1[1] + 1):
#         set_a.add(i)
#     for i in range(range_2[0], range_2[1] + 1):
#         set_b.add(i)
#     sets_intersection = set_a.intersection(set_b)
#     if len(sets_intersection) > max_intersection:
#         max_intersection = len(sets_intersection)
#         combined_intersection = sets_intersection
#     set_a.clear()
#     set_b.clear()
#
#
# print(f"Longest intersection is [", end="")
# print(*combined_intersection, sep=", ", end="")
# print(f"] with length {max_intersection}")