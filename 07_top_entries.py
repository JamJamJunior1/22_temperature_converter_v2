# Get data from user and store it in a list, showing te most recent entries first

# Set up empty list
all_calculations = []

# Get five items of Data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("list big empty")

else:

    # Show that everything got to the list
    print()
    print("The Complete Edition")
    print(all_calculations)

    # print items starting at the end of the list
    if len(all_calculations) >= 3:
        print("Most Recent")
        for item in range(0, 3):
            print(all_calculations[len(all_calculations) - item - 1])

    else:
        print("Newest to Oldest")
        for item in all_calculations:
            print(all_calculations(len(all_calculations) - all_calculations.index()))
