# Restaurant Point of Sale System

This Python script implements a Restaurant Point of Sale (POS) system using the PySimpleGUI library. The system enables users to manage orders and calculate totals, taxes, and gratuities for tables in a restaurant setting.

## Requirements

Before running the program, ensure that you have the following dependencies installed:

- Python 3.6 or above
- PySimpleGUI (`PySimpleGUI`)

To install the dependencies, run the following command:

`pip install -r requirements.txt`

Make sure you have pip installed and the requirements.txt file is in the same directory as the script.

## Features

- **Table Selection**: Users can select a table from a dropdown list to manage its orders.

- **Menu Interaction**: The menu is divided into sections such as "Sandwiches," "Sides," and "Drinks." Users can choose to either "Add Item" or "Remove Item" from the selected table's ticket. The available items are listed as buttons, and clicking on an item button will perform the selected action (add/remove) for that item.

- **Current Ticket Display**: The current ticket for the selected table is displayed in a multi-line text box. It shows the items that have been added to the ticket.

- **Total Calculation**: Users can click the "Total Ticket" button to calculate the subtotal, tax, and total cost of the items on the ticket. The calculated values are displayed in designated areas.

- **Gratuity Calculation**: After calculating the total, the system calls a gratuity microservice and displays suggested gratuity amounts (10%, 15%, 20%) based on the total.

- **Clear Ticket**: The "Clear Ticket" button allows users to clear all items from the selected table's ticket. A confirmation dialog is shown before clearing the ticket.

- **What's New? and How To Use**: Users can click the "What's New?" and "How To Use" buttons to get information about new features and usage instructions, respectively.

## Code Explanation

The code is organized into various sections:

- **Color Theme and Dropdown Options**: The script sets the color theme and defines dropdown options for table selection and add/remove actions.

- **Column Layouts**: The layout of the GUI is defined using two columns. The left column displays the current ticket and action buttons, while the right column displays subtotal, tax, total, and gratuity information.

- **Constants and Function Definitions**: Various constants and functions are defined, such as functions to clear totals, display orders, retrieve item prices, add/remove items, calculate subtotal, call the gratuity microservice, and clear the ticket.

- **Window Layout**: The main GUI layout is defined using a combination of text, dropdowns, buttons, and columns.

- **Window Creation and Event Loop**: The PySimpleGUI window is created using the defined layout. The script enters an event loop where it waits for user interactions. Depending on the event (button click or window closure), corresponding actions are executed.

## Instructions
1. Clone the repository.
2. Install the required dependencies using the command mentioned in the "Requirements" section above.
3. Run the script.
4. Use the dropdown to select a table.
5. Click the "Select Table" button to display the current ticket for the selected table.
6. Use the "Add Item" or "Remove Item" dropdown to select the action.
7. Click on the buttons representing menu items to add or remove items from the ticket.
8. Click the "Total Ticket" button to calculate and display the subtotal, tax, and total.
9. The gratuity suggestions will be displayed based on the calculated total.
10. To clear the entire ticket for the selected table, click the "Clear Ticket" button and confirm the action.

## Notes

- The script uses external files to store information about current orders and prices. Make sure the file paths are correctly set up for your system.

- This is a basic implementation and can be extended to include additional features and error handling as needed.

- The script's GUI is created using PySimpleGUI, which simplifies the process of building graphical interfaces in Python.
