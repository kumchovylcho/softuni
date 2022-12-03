def add_songs(*args):
    result = {}
    for title, lst in args:
        result[title] = result.get(title, [])
        for lyric in lst:
            result[title].append(lyric)
    final_result = ""
    for key, value in result.items():
        final_result += f"- {key}\n"
        for text in value:
            final_result += f"{text}\n"
    return final_result
