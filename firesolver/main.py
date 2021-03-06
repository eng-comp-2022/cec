import PySimpleGUI as sg
from gui.gui import create_main_layout
from maps import bubbleMap
from maps import chloroplethMap


if __name__ == "__main__":

    # Define the window's contents and theme
    layout = create_main_layout()

    # Create the window
    window = sg.Window("Fire Tower Positioning System", layout)
    
    #Create flag to notify is a save path has been selected
    savePathPresent = False;
    
    #Create a flag to notify if stage two has been completed
    didStage2 = False;

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read(timeout=250)

        # See if window was closed
        if event == sg.WINDOW_CLOSED:
            break
        
        #Check to see if there is a save path, enable saving it so
        if values['-SAVE_PATH-'] != "":
            window['-SAVE_METRIC_MAP-'].update(disabled=False)
            window['-SAVE_RISK_MAP-'].update(disabled=False)
            savePathPresent = True

        ## STAGE ONE ##
        # If user wants to generate the stage one map, generate the map without saving it
        if event == "-GENERATE_METRIC_MAP-":
            chloroplethMap.generateMetricMap(False, "")

        # If user wants to save the stage one map, save the map without having it pop up
        if event == "-SAVE_METRIC_MAP-":
            chloroplethMap.generateMetricMap(True, values["-SAVE_PATH-"])
            
            
        ## STAGE TWO ##
        # If user wants to generate the stage two map, generate the map without saving it. Also, enable stage 3
        if event == "-GENERATE_RISK_MAP-":
            chloroplethMap.generateRiskMap(False, "")
            window['-GENERATE_STATION_MAP-'].update(disabled=False)
            didStage2 = True

        # If user wants to save the stage two map, save the map without having it pop up. Also, enable stage 3
        if event == "-SAVE_RISK_MAP-":
            chloroplethMap.generateRiskMap(True, values["-SAVE_PATH-"])
            window['-GENERATE_STATION_MAP-'].update(disabled=False)
            didStage2 = True

        #Enable Stage 3 if requirements are met
        if savePathPresent and didStage2:
                window['-SAVE_STATION_MAP-'].update(disabled=False)


        ## STAGE THREE ##
        # If user wants to generate the stage two map, generate the map without saving it
        if event == "-GENERATE_STATION_MAP-":
            bubbleMap.generateStationMap(False, "", values["-KEY_COMBO-"])

        # If user wants to save the stage three map, save the map without having it pop up
        if event == "-SAVE_STATION_MAP-":
            bubbleMap.generateStationMap(True, values["-SAVE_PATH-"], values["-KEY_COMBO-"])

    # Finish up by removing from the screen
    window.close()
