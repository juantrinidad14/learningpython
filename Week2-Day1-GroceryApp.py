ShoppingList = []

def instructions():
    print("----------------------------")
    print("type DONE to finish the list ")
    print("type SHOW to view list")
    print("type RETURN to add more list")
    print("----------------------------")

def print_shopping_list():
    print("----------------")
    print("Shopping List: ")
    print("----------------")
    for item in ShoppingList:
        print(">" +item)  

def add_item_to_list(item):
    ShoppingList.append(item) 
    print("-------------------------")
    print("Added {} to shopping list! List now has {} items".format(item, len(ShoppingList))) 

def main():
    instructions()
    while True:
        item = str(input("Enter name of store and items to your list: "))
        if item == "DONE":
            print_shopping_list
            break
        elif item == 'DISPLAY':
            print_shopping_list
        elif item == 'RETURN':
            return_instruc()
        else:
            add_item_to_list(item)
            
main()


























