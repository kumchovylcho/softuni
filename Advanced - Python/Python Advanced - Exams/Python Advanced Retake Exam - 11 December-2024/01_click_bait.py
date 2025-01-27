from collections import deque


def calculate_and_return_to_collection(collection: list[int],
                                       _remainder: int,
                                       only_positive_remainder=True,
                                       return_to_collection=True) -> list[int]:
    if not return_to_collection:
        collection.append(_remainder if only_positive_remainder else -_remainder)
        return collection

    if only_positive_remainder and _remainder > 0:
        collection.append(_remainder)

    return collection


links = deque(int(x) for x in input().split())
articles = [int(x) for x in input().split()]
target_engagement = int(input())
final_feed = []

while links and articles:
    link = links.popleft()
    article = articles.pop()

    smaller = min(link, article)
    bigger = max(link, article)

    remainder = bigger % smaller
    if bigger == article:
        final_feed = calculate_and_return_to_collection(final_feed, remainder, return_to_collection=False)
        articles = calculate_and_return_to_collection(articles, remainder * 2)
    elif bigger == link:
        final_feed = calculate_and_return_to_collection(final_feed, remainder, return_to_collection=False, only_positive_remainder=False)
        links = calculate_and_return_to_collection(links, remainder * 2)
    elif smaller == bigger:
        final_feed = calculate_and_return_to_collection(final_feed, 0, return_to_collection=False)


print(f"Final Feed: {', '.join(str(x) for x in final_feed)}")
total_engagement = sum(final_feed)
if total_engagement >= target_engagement:
    print(f"Goal achieved! Engagement Value: {total_engagement}")
elif total_engagement < target_engagement:
    print(f"Goal not achieved! Short by: {target_engagement - total_engagement}")