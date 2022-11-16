import PySimpleGUI as sg
import time

# set color theme
sg.theme('Purple')

# dropdown options
table_list = ["Table1", "Table2", "Table3", "Table4", "Table5", "Table6"]
add_remove = ["Add Item", "Remove Item"]

# column layouts
col1 = [[sg.Text("Current Ticket", font=('Arial', 15, 'bold', 'underline'))],
          [sg.Multiline(size=(25, 8), key='-ITEM_ORDERS-')],
          [sg.Button("Total Ticket",tooltip=("Calculate totals, tax and gratuity")), sg.Button("Clear Ticket",tooltip=("Clear entire ticket for current table"))]]
col2 = [[sg.Text("                          Subtotal:"), sg.Multiline(size=(10, 2), key='-SUBTOTAL-')],
          [sg.Text("                                 Tax:"), sg.Multiline(size=(10, 2), key='-TAX-')],
          [sg.Text("                        TOTAL:", font=('Arial', 12, 'bold',)), sg.Multiline(size=(10, 2), key='-TOTAL-')],
          [sg.Text("Suggested Gratuities\n              (10%,15%,20%):"), sg.Multiline(size=(10, 4), key='-GRATUITY-')]]

# constants
TAX_RATE = .0725

# function definitions
def clear_totals():
    """ Clear Total Output Windows"""
    window['-SUBTOTAL-'].update('')
    window['-TAX-'].update('')
    window['-TOTAL-'].update('')
    window['-GRATUITY-'].update('')

def display_order():
    """ Update Window to Current Ticket When User Selects New Table"""
    file = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r")
    file2 = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r")
    window['-ITEM_ORDERS-'].update('')
    for line, line2 in zip(file, file2):
        window['-ITEM_ORDERS-'].print(line, line2)
    file.close()
    file2.close()

def retrieve_price():
    """ Retrieve item price"""
    file = open(f"FoodItems\\{event}.txt", "r")
    price = file.readline()
    file.close()
    return price

def add_item(price):
    """ Add item to the food and tab files"""
    with open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "a") as food:
        food.write(f'{event}\n')
    with open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "a") as tab:
        tab.write(f'{price}\n')

def remove_item():
    """ Remove item from the food and tab files"""
    food = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r+")
    food_lines = food.readlines()
    tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r+")
    tab_lines = tab.readlines()
    food.truncate(0)
    tab.truncate(0)
    food.close()
    tab.close()

    food = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r+")
    tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r+")
    found = 0
    for line1, line2 in zip(food_lines, tab_lines):
        if line1.strip("\n") != event or found == 1:
            food.write(line1)
            tab.write(line2)
        else:
            found = 1
    food.close()
    tab.close()

def calculate_subtotal():
    """ Add item prices to calculate subtotal"""
    tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r+")
    tab_lines = tab.readlines()
    tab.close()

    subtotal = 0
    for line in tab_lines:
        line = line.rstrip()
        subtotal += float(line)
    return subtotal

def call_gratuity_microservice():
    """ Update Gratuity Window With Gratuity Microservice Call"""
    total_file = open("total.txt", "w")
    total_file.truncate(0)  # prevents invalid entry
    total_file.write(f"{total}")
    total_file.close()
    time.sleep(1)

    with open("gratuity.txt", "r") as grat:
        for line in grat:
            window['-GRATUITY-'].print(line.strip("\n"))

def clear_ticket():
    """ Clear the Currently Selected Table's Ticket"""
    food = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r+")
    tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r+")
    food.truncate(0)
    tab.truncate(0)
    food.close()
    tab.close()

# window layout
layout = [[sg.Push(), sg.Button("What's New?",tooltip=("Displays new features")), sg.Button("How To Use",tooltip=("Displays instructions"))],
          [sg.Text("Table Number", font=('Arial', 15, 'bold', 'underline'))],
          [sg.DropDown(table_list, size=(10, 8), default_value=table_list[0], key="-TABLE-",tooltip=("Select Table Number")), sg.Button("Select Table",tooltip=("Change current table"))],
          [sg.HorizontalSeparator()],
          [sg.Text("Menu", font=('Arial', 15, 'bold', 'underline'))],
          [sg.DropDown(add_remove, size=(15, 8), default_value=add_remove[0], key="-ADD_REMOVE-", tooltip=("Change mode"))],
          [sg.Text("Sandwiches")],
          [sg.Button("ClassicBurger", tooltip=("Served medium rare.\nContains Lettuce, Tomato, All-Beef Patty on artisan bun.\n Price: $12.00 ")), sg.Button("Cheeseburger",tooltip=("Served medium rare.\nContains Lettuce, Tomato, Cheese, All-Beef Patty on artisan bun.\n Price: $14.00 ")), sg.Button("ChickenSandwich",tooltip=("Deep Fried Chicken.\nContains Lettuce, Tomato, Cheese on artisan bun.\n Price: $10.00 ")), sg.Button("FrenchDip", tooltip=("Flank Steak.\nContains Swiss Cheese, Onions, Horseradish on artisan bread.\n Price: $13.00 "))],
          [sg.Text("Sides")],
          [sg.Button("Fries", tooltip=("Basket of fries\n Price: $2.00 ")), sg.Button("OnionRings",tooltip=("Stack of Onion Rings\n Price: $5.00 ")), sg.Button("SweetPotatoFries",tooltip=("Basket of sweet potato fries\n Price: $3.00 ")), sg.Button("FriedZucchini",tooltip=("Whole zucchini battered and fried\n Price: $4.00 "))],
          [sg.Text("Drinks")],
          [sg.Button("Coke",tooltip=("16oz Coke\n Price: $3.00 ")), sg.Button("Sprite",tooltip=("16oz Sprite\n Price: $3.00 ")), sg.Button("Lemonade",tooltip=("16oz Lemonade\n Price: $3.00 ")), sg.Button("Tea",tooltip=("16oz Tea\n Price: $3.00 "))],
          [sg.HorizontalSeparator()],
          [sg.Column(col1, element_justification='left'),sg.Column(col2, element_justification='left')]]

# create PySimpleGUI window
window = sg.Window('Restaurant POS System', layout, size=(600, 600), use_custom_titlebar=True)

# event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "What's New?":

        # display text to 'What's New?' Window
        choice, _ = sg.Window("What's New?", [[sg.Text("You no longer need to clear ticket items one at a time!")],
                                              [sg.Text("To save time, press the 'Clear Ticket' button to clear the entire ticket for a table.")],
                                              [sg.Text("*NOTE: 'Clear Ticket' removes ALL items on ticket. To remove one item, try 'Remove Item' instead.")],
                                              [sg.Push(), sg.Ok(s=10)]], disable_close=True).read(close=True)

    if event == "How To Use":

        # display text to 'How To Use' Window
        choice, _ = sg.Window("How To Use", [[sg.Text("* Change Table Number to table currently being served.")],
                                             [sg.Text("* Click 'Select Table' to populate current ticket.")],
                                             [sg.HorizontalSeparator()],
                                             [sg.Text("* In 'Menu' section, change dropdown between 'Add Item'")],
                                             [sg.Text("  and 'Remove Item' based off which operation user needs.")],
                                             [sg.Text("* Hit button for food item to add/remove from ticket.")],
                                             [sg.HorizontalSeparator()],
                                             [sg.Text("* In 'Current Ticket' section, click 'Total Ticket' to")],
                                             [sg.Text("  calculate Totals, Tax and Gratuity for current table.")],
                                             [sg.Text("* Click the 'Clear Ticket' button to empty the current table ticket.")],
                                             [sg.Push(), sg.Ok(s=10)]], disable_close=True).read(close=True)

    if event == "Select Table":

        display_order()
        clear_totals()

    if (event == "ClassicBurger" or event == "Cheeseburger" or event == "ChickenSandwich" or event == "FrenchDip"
        or event == "Fries" or event == "OnionRings" or event == "SweetPotatoFries" or event == "FriedZucchini"
        or event == "Coke" or event == "Sprite" or event == "Lemonade" or event == "Tea"):

        price = retrieve_price()

        if values['-ADD_REMOVE-'] == "Add Item":
            add_item(price)
            display_order()

        # removing items from ticket
        if values['-ADD_REMOVE-'] == "Remove Item":
            remove_item()
            display_order()

    if event == "Total Ticket":

        # calculate totals
        subtotal = calculate_subtotal()
        tax = round(subtotal * TAX_RATE, 2)
        total = subtotal + tax

        # update total windows
        clear_totals()
        window['-SUBTOTAL-'].print(subtotal)
        window['-TAX-'].print(tax)
        window['-TOTAL-'].print(total)
        call_gratuity_microservice()

    if event == "Clear Ticket":

        # verify user wants to clear current ticket
        choice, _ = sg.Window('Continue?',[[sg.Text("Are you sure you want to clear the ticket?")],[sg.Yes(s=10), sg.No(s=10)]], disable_close=True).read(close=True)
        if choice == "Yes":
            clear_ticket()
            display_order()
            clear_totals()

            # display confirmation
            sg.popup('Ticket Cleared')

window.close()