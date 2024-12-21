def add_item(menu, item):
    if item not in menu:
        menu.append(item)
        print(f'{item} added to the menu.')
    else:
        print(f'{item} is already in the menu.')

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        print(f'{item} removed from the menu.')
    else:
        print(f'{item} is not in the menu.')

def check_item(menu, item):
    if item in menu:
        return f'{item} is available'
    else:
        return f'{item} is not available'

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item_name = "Tacos"
remove_item_name = "Salad"
check_item_name = "Pizza"
add_item(initial_menu, add_item_name)
remove_item(initial_menu, remove_item_name)
availability = check_item(initial_menu, check_item_name)
print(f'Updated menu: {initial_menu}')
print(f'Availability: {availability}')
