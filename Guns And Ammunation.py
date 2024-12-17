cart = []
pistols = [("Glock", 100), ("Desert Eagle", 500), ("Smith and Vessen", 400), ("Suppressed gun", 200)]
assault_rifles = [("Ak-47", 100), ("M-16", 500), ("Ak-56", 400), ("Graza", 200)]
thrown = [("Hand Grenade", 100), ("Smoke Grenade", 500), ("Flash Bang", 400), ("Molotov Cocktail", 200)]
fighter_jets = [("Mig-21", 100), ("Mig-25", 500), ("Su-27", 400), ("Su-30", 200), ("Mirage", 400), ("F-16", 200), ("F-35", 400), ("F-22 Raptor", 200), ("B2", 200), ("Dassault Rafale", 200)]
miscellaneous = [("Tank", 200), ("RPG", 300), ("Dynamite", 200)]

def separator():
    print("==========================================\n")

def category_menu():
    print("1) Pistols")
    print("2) Assault Rifles")
    print("3) Thrown")
    print("4) Fighter Jets")
    print("5) Miscellaneous")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input!!!")
        separator()
        return
    
    separator()
    
    if choice == 1:
        add_weapon(pistols)
    elif choice == 2:
        add_weapon(assault_rifles)
    elif choice == 3:
        add_weapon(thrown)
    elif choice == 4:
        add_weapon(fighter_jets)
    elif choice == 5:
        add_weapon(miscellaneous)
    else:
        print("Invalid Input!!!")
        separator()
        return
    

def add_weapon(weapon_list):
    for i in range(len(weapon_list)):
        print(f"{i+1} {weapon_list[i][0]}    {weapon_list[i][1]}")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input!!!")
        separator()
        return
    
    if choice < 1 or choice > len(weapon_list):
        print("Invalid Input!!!")
        separator()
        return
    
    cart.append(weapon_list[choice-1])
    print(f"{weapon_list[choice-1][0]} added to cart successfully!")
    separator()

def display():
    
    if len(cart) == 0:
        print("Cart is empty!!!")
        separator()
        return
    
    for i in range(len(cart)):
        print(f"{i+1}) {cart[i][0]}   @{cart[i][1]}")
    
    separator()

def clear_cart():
    if len(cart) == 0:
        print("Cart is already empty!!!")
        separator()
        return
    
    cart.clear()
    print("Cart cleared successfully")
    separator()

def remove_weapon():
    if len(cart) == 0:
        print("Cart is already empty!!!")
        separator()
        return
    for i in range(len(cart)):
        print(f"{i+1}) {cart[i][0]}   {cart[i][1]}")
    print()
    try:
        remove_index = int(input("Enter the item you want to remove: "))
    except ValueError:
        print("Invalid Input")
        separator()
        return
    
    if remove_index < 1 or remove_index > len(cart):
        print("Invalid Input")
        separator()
        return
    
    cart.pop(remove_index-1)
    print(f"Item removed successfully")

def print_invoice():
    
    if (len(cart)) == 0:
        print("Cart is empty!!!")
        separator()
        return
    
    
    total_cost = 0
    for i in range(len(cart)):
        total_cost += cart[i][1]
    
    for i in range(len(cart)):
        print(f"{i+1}) {cart[i][0]}   @{cart[i][1]}")
    
    print("=========================================")
    print(f"Total Payable A1mount: {total_cost}")
    print("Your order has been successfully placed")
    print("Happy Purchasing!!! :)")
    print("=========================================")
    print()
    cart.clear()

while True:
    print("1) Add weapons to cart")
    print("2) Display cart")
    print("3) Remove weapon from cart")
    print("4) Clear cart")
    print("5) Print Invoice & Checkout")
    print("6) Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Input!!!")
        separator()
        continue
    
    if choice < 1 or choice > 6:
        print("Invalid Input!!!")
        separator()
        continue
    
    separator()
    if choice == 1:
        category_menu()
    
    elif choice == 2:
        display()
    
    elif choice == 3:
        remove_weapon()
    
    elif choice == 4:
        clear_cart()
    
    elif choice == 5:
        print_invoice()
    
    elif choice == 6:
        exit(0)
    
    else:
        print("Invalid Input!!!")
        separator()
        continue
