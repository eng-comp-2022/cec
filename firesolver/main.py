import PySimpleGUI as sg
from gui.gui import create_main_layout
from maps import bubbleMap
from maps import chloroplethMap


if __name__ == "__main__":

    # Define the window's contents and theme
    layout = create_main_layout()

    # Create the window
    window = sg.Window("Fire Tower Positioning System", layout)

    # Flags to check if the user input is valid
    validBudget = False
    validData = False

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read(timeout=250)

        # See if window was closed
        if event == sg.WINDOW_CLOSED:
            break

        # Update the budget to mirror the user's input
        if values["-BUDGET-"] == "":
            window["-BUDGET_MIRROR-"].update("Unlimited")
        else:
            # Ensure it is a valid number, respond accordingly
            try:
                float(values["-BUDGET-"])
                window["-BUDGET_MIRROR-"].update("$" + values["-BUDGET-"])
                validBudget = True
            except ValueError:
                window["-BUDGET_MIRROR-"].update("Invalid Input")
                validBudget = False

        # If the user input a file, read it and update the window accordingly
        if event == "-FOLDER_PATH-":

            # Update path
            window["-PATH_MIRROR-"].update(values["-FOLDER_PATH-"])
            # Clear previous data
            window["-DATA_MIRROR-"].update("")

            # Check that file is of correct data type. Must be done due to pysimplegui glitch
            if values["-FOLDER_PATH-"][-4:] != ".txt":

                # File is not of the correct type, notify user and disable button
                window["-DATA_MIRROR-"].update(
                    'File is not of the correct type. Please use a file with the extension ".txt"'
                )
                validData = False

            else:

                # Open and read the new file
                file = open(values["-FOLDER_PATH-"], "r")
                lines = file.readlines()

                # Create an empty string that will be appended to the data
                data = ""

                # Create a counter starting at 1 do use modulus
                i = 1

                # Iterate through the file lines and categorize according to position
                for line in lines:
                    if i % 3 == 1:
                        data += "Type: " + line.strip() + "\n"
                    elif i % 3 == 2:
                        data += "\tCost: " + line.strip() + "\n"
                    else:
                        data += "\tRadius: " + line.strip() + "\n\n"

                    i = i + 1  # Increment counter

                # Update the window to show the data
                window["-DATA_MIRROR-"].update(data)
                validData = True

        # Enable or disable the 'Generate' button accordingly
        if validBudget and validData:
            window["-GENERATE_MAP-"].update(disabled=False)
        else:
            window["-GENERATE_MAP-"].update(disabled=True)

        # Enable or disable the 'Save' button accordingly
        if validBudget and validData and values["-SAVE_PATH-"] != "":
            window["-SAVE_MAP-"].update(disabled=False)
            window["-SAVE_TXT-"].update(disabled=False)
        else:
            window["-SAVE_MAP-"].update(disabled=True)
            window["-SAVE_TXT-"].update(disabled=True)

        # Generate the map without saving it
        if event == "-GENERATE_MAP-":
            bubbleMap.generateFireStationMap(False, "")

        # Generate the map and save it without showing it
        if event == "-SAVE_MAP-":
            bubbleMap.generateFireStationMap(True, values["-SAVE_PATH-"])
            
        # Generate the map without saving it
        if event == "-GENERATE_RISK-":
            chloroplethMap.generateRiskMap(False, "")

        # Generate the map and save it without showing it
        if event == "-SAVE_RISK-":
            chloroplethMap.generateRiskMap(True, values["-SAVE_PATH-"])

        # Save the generated data to a .txt file
        if event == "-SAVE_TXT-":
            bubbleMap.generateText(values["-SAVE_PATH-"])

    # Finish up by removing from the screen
    window.close()
