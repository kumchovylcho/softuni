def naughty_or_nice_list(*args, **kwargs):
    santa_dict = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    santa_list = args[0]

    for i in args[1:]:
        num, cmd = [int(x) if x.isdigit() else x for x in i.split('-')]
        counter = 0
        name = ""
        current = ""
        for check in santa_list:
            if num == check[0]:
                counter += 1
                current = check
                name = check[1]
        if counter == 1:
            santa_dict[cmd].append(name)
            santa_list.remove(current)

    for key, cmd_value in kwargs.items():
        counter_name = 0
        current_kwargs = ""
        current = ""
        for pos, (current_num, current_name) in enumerate(santa_list):
            if key == current_name:
                counter_name += 1
                current_kwargs = current_name
                current = pos
        if counter_name == 1:
            santa_list.pop(current)
            santa_dict[cmd_value].append(current_kwargs)

    for left_kid in santa_list:
        santa_dict['Not found'].append(left_kid[1])

    result = ''
    for key, value in santa_dict.items():
        if value:
            result += f"{key}: {', '.join(value)}\n"
    return result
