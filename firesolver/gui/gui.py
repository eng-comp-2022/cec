from turtle import onclick
import PySimpleGUI as sg
width = 26

def create_main_layout():

    #This contains the three buttons to view and save the map, as well as save the txt. This is seperate to allow for right-justification
    map_column = [
        [
            sg.Button("View Generated Firestation Locations", key="-GENERATE_MAP-", size=(15, 1), font=("Helvetica", 16), disabled=False, disabled_button_color='grey'),
            sg.Button("Save Generated Locations Firestation as PNG", key="-SAVE_MAP-", size=(15, 1), font=("Helvetica", 16), disabled=False, disabled_button_color='grey'),
            sg.Button("View At-Risk Locations", key="-GENERATE_RISK-", size=(15, 1), font=("Helvetica", 16), disabled=False, disabled_button_color='grey'),
            sg.Button("Save At-Risk Locations Firestation as PNG", key="-SAVE_RISK-", size=(15, 1), font=("Helvetica", 16), disabled=False, disabled_button_color='grey'),
            sg.Button("Save Generated Locations as TXT", key="-SAVE_TXT-", size=(15, 1), font=("Helvetica", 16), disabled=False, disabled_button_color='grey'),
        ],
    ]

    layout = [
        #Top "Welcome" Text
        [
            sg.Text("Welcome to the Fire Tower Positioning System", font=("Helvetica", 40),),
        ],
        #Division
        [
            sg.Text("_"*150)
        ],
        #User Input Portion
        [
            sg.Text("To help us optimize your fire tower positioning, please provide us with some information:", font=("Helvetica", 16),),
        ],
        [
            sg.Text(" ")
        ],
        [
            sg.Text("Budget:", size=(width, 1), font=("Helvetica", 20)),
            sg.Input(key="-BUDGET-", size=(10, 1), font=("Helvetica", 20))
        ],
        [
            sg.Text("Path to Tower Data:", size=(width, 1), font=("Helvetica", 20)),
            sg.Input(key="-FOLDER_PATH-", size=(30, 1), font=("Helvetica", 20), enable_events='true', readonly='true', disabled_readonly_background_color='white', disabled_readonly_text_color='black'),
            sg.FileBrowse(key="-FOLDER_BROWSE-", file_types=(("Text Files", "*.txt")), size=(15, 1), font=("Helvetica", 16), enable_events='true') #Browse by file type doesn't work on mac as there is a pysimplegui tkinter bug with it
        ],
        #Division
        [
            sg.Text("_"*150)
        ],
        #User Data Mirror
        [
            sg.Text("Below is the data that will be used for generation: ", font=("Helvetica", 16),),
        ],
        [
            sg.Text(" ")
        ],
        [
            sg.Text("Budget: ", size=(10, 1), font=("Helvetica", 20)),
            sg.Text("", size=(10, 1), font=("Helvetica", 20), key="-BUDGET_MIRROR-"),
        ],
        [
            sg.Text("File Path: ", size=(10, 1), font=("Helvetica", 20)),
            sg.Text("", font=("Helvetica", 16), key="-PATH_MIRROR-"),
        ],
        [
            sg.Text("File Data: ", size=(10, 1), font=("Helvetica", 20)),
        ],
        [
            sg.Multiline("", size=(40, 10), font=("Helvetica", 16), key="-DATA_MIRROR-"),
        ],
        #Division
        [
            sg.Text("_"*150)
        ],
        [
            sg.Text(" ")
        ],
        [
            sg.Text("Path to Save Generated Map:", size=(width, 1), font=("Helvetica", 20)),
            sg.Input(key="-SAVE_PATH-", size=(30, 1), font=("Helvetica", 20), enable_events='true', readonly='true', disabled_readonly_background_color='white', disabled_readonly_text_color='black'),
            sg.FolderBrowse(key="-SAVE_BROWSE-", size=(15, 1), font=("Helvetica", 16), enable_events='true') #Browse by file type doesn't work on mac as there is a pysimplegui tkinter bug with it
        ],
        [
            sg.Text(" ")
        ],
        [
            sg.Column(map_column, element_justification='right', expand_x=True)
        ],
    ]

    return layout


def create_result_layout(image, dist_between,morat,next_opp,seconds,date):

    layout = [
    ]
    
    return layout