from typing import Callable


def list_roman_emperors(*args, **kwargs) -> str:
    def generate_output(collection: dict, initial_msg: str, sort_key: Callable) -> list[str]:
        if not collection:
            return []

        sorted_data = [initial_msg, ]
        for emperor, rule in sorted(collection.items(), key=sort_key):
            sorted_data.append(f"****{emperor}: {rule}")

        return sorted_data


    successful_emperors = {}
    unsuccessful_emperors = {}
    for emperor, success in args:
        if emperor not in kwargs:
            continue

        (successful_emperors if success else unsuccessful_emperors)[emperor] = kwargs[emperor]

    output = [f"Total number of emperors: {len(kwargs)}"]
    output.extend(generate_output(successful_emperors, "Successful emperors:", lambda kv: (-kv[1], kv[0])))
    output.extend(generate_output(unsuccessful_emperors, "Unsuccessful emperors:", lambda kv: (kv[1], kv[0])))

    return "\n".join(output)
