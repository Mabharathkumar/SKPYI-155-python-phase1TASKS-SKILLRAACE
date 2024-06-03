def remove_common_characters(name1, name2):
    list1 = list(name1)
    list2 = list(name2)
    for char in list1[:]:
        if char in list2:
            list1.remove(char)
            list2.remove(char)
    return list1, list2
def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    name1_list, name2_list = remove_common_characters(name1, name2)
    remaining_count = len(name1_list) + len(name2_list)
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames) > 1:
        split_index = (remaining_count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]
def get_flames_result(flame_char):
    if flame_char == 'F':
        return "Friends"
    elif flame_char == 'L':
        return "Lovers"
    elif flame_char == 'A':
        return "Affection"
    elif flame_char == 'M':
        return "Marriage"
    elif flame_char == 'E':
        return "Enemies"
    elif flame_char == 'S':
        return "Siblings"
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
flame_char = flames_game(name1, name2)
result = get_flames_result(flame_char)
print(f"The relationship between {name1} and {name2} is: {result}")
