def adding_players(new_player, all_players_dict):
    player, position_type, skill = [item if item[0].isalpha() else int(item) for item in new_player.split(" -> ")]
    all_players_dict[player] = all_players_dict.get(player, {'roles': {}})
    all_players_dict[player]['roles'][position_type] = all_players_dict[player]['roles'].get(position_type, skill)
    if position_type in all_players_dict[player]['roles'] and all_players_dict[player]['roles'][position_type] < skill:
        all_players_dict[player]['roles'][position_type] = skill
    return all_players_dict


def player_vs_player(both_players, all_players_dict):
    first_player, second_player = both_players.split(" vs ")
    if first_player and second_player in all_players_dict:
        for first_player_roles in all_players_dict[first_player]['roles']:
            if first_player_roles in all_players_dict[second_player]['roles']:
                total_points_first_player = sum(all_players_dict[first_player]['roles'].values())
                total_points_second_player = sum(all_players_dict[second_player]['roles'].values())
                if total_points_first_player > total_points_second_player:
                    all_players_dict.pop(second_player)
                    break
                elif total_points_second_player > total_points_first_player:
                    all_players_dict.pop(first_player)
                    break
    return all_players_dict


def show_result(dict_to_sort):
    for player, total_points in sorted(dict_to_sort.items(), key=lambda item: (-sum(item[1]['roles'].values()), item[0])):
        print(f"{player}: {sum(total_points['roles'].values())} skill")
        for role, points in sorted(total_points['roles'].items(), key=lambda item: (-item[1], item[0])):
            print(f"- {role} <::> {points}")


players = {}
command = input()
while command != "Season end":
    if "->" in command:
        players = adding_players(command, players)
    elif "vs" in command:
        players = player_vs_player(command, players)
    command = input()
show_result(players)
