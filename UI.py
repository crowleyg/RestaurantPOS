import PySimpleGUI as sg
import time

sg.theme('Purple')

table_list = ["Table1", "Table2", "Table3", "Table4", "Table5", "Table6"]

add_remove = ["Add Item", "Remove Item"]

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
          [sg.Text("Current Ticket", font=('Arial', 15, 'bold', 'underline'))],
          [sg.Multiline(size=(25, 8), key='-ITEM_ORDERS-')],
          [sg.Button("Total Ticket",tooltip=("Calculate totals, tax and gratuity")), sg.Button("Clear Ticket",tooltip=("Clear entire ticket for current table"))],
          [sg.Text("")],
          [sg.Text("                          Subtotal:"), sg.Multiline(size=(10, 1), key='-SUBTOTAL-')],
          [sg.Text("                                 Tax:"), sg.Multiline(size=(10, 1), key='-TAX-')],
          [sg.Text("                        TOTAL:", font=('Arial', 12, 'bold',)), sg.Multiline(size=(10, 1), key='-TOTAL-')],
          [sg.Text("Suggested Gratuity (15%):"), sg.Multiline(size=(10,1), key='-GRATUITY-')]]

window = sg.Window('Restaurant POS System', layout, size=(600, 800), use_custom_titlebar=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "What's New?":
        choice, _ = sg.Window("What's New?", [[sg.Text("You no longer need to clear tickets one item at a time!")],
                                              [sg.Text("Press the 'Clear Ticket' button to clear the entire ticket for a table.")],
                                              [sg.Push(), sg.Ok(s=10)]], disable_close=True).read(close=True)

    if event == "How To Use":
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
        file = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r")
        file2 = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r")
        window['-ITEM_ORDERS-'].update('')
        for line, line2 in zip(file, file2):
            window['-ITEM_ORDERS-'].print(line, line2)

        #close the files
        file.close()
        file2.close()

        #sg.Popup(event, values['-TABLE-'], values['-ADD_REMOVE-'])

    if (event == "ClassicBurger" or event == "Cheeseburger" or event == "ChickenSandwich" or event == "FrenchDip"
        or event == "Fries" or event == "OnionRings" or event == "SweetPotatoFries" or event == "FriedZucchini"
        or event == "Coke" or event == "Sprite" or event == "Lemonade" or event == "Tea"):

        file = open(f"FoodItems\\{event}.txt", "r")
        line = file.readline()
        file.close()

        # Adding items to ticket
        if values['-ADD_REMOVE-'] == "Add Item":

            # add the item to the food and tab files
            with open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "a") as food:
                food.write(f'{event}\n')
            with open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "a") as tab:
                tab.write(f'{line}\n')


            # update the current ticket window
            window['-ITEM_ORDERS-'].update('')
            food = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r")
            tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r")
            for line1, line2 in zip(food, tab):
                window['-ITEM_ORDERS-'].print(line1, line2)
            food.close()
            tab.close()

        #removing items from ticket
        if values['-ADD_REMOVE-'] == "Remove Item":
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

            # update the current ticket window
            window['-ITEM_ORDERS-'].update('')
            food = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r")
            tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r")
            for line1, line2 in zip(food, tab):
                window['-ITEM_ORDERS-'].print(line1, line2)
            food.close()
            tab.close()

            #for count, line1, line2 in enumerate(zip(food, tab)):
                #if line1 == event:



    if event == "Clear Ticket":
        # verify user wants to clear
        choice, _ = sg.Window('Continue?',[[sg.Text("Are you sure you want to clear the ticket?")],[sg.Yes(s=10), sg.No(s=10)]], disable_close=True).read(close=True)
        if choice == "Yes":

            # clear the files
            food = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r+")
            tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r+")
            food.truncate(0)
            tab.truncate(0)
            food.close()
            tab.close()

            #update the current ticket window
            window['-ITEM_ORDERS-'].update('')
            food = open(f"CurrentTickets\\{values['-TABLE-']}_Food.txt", "r")
            tab = open(f"CurrentTickets\\{values['-TABLE-']}_Tab.txt", "r")
            for line1, line2 in zip(food, tab):
                window['-ITEM_ORDERS-'].print(line1, line2)
            food.close()
            tab.close()

            # display confirmation
            sg.popup('Ticket Cleared')

#for tax and total use window[key].update(line)

window.close()