from turtle import onclick
import PySimpleGUI as sg
width = 26

def create_main_layout():

    layout = [
        #Top "Welcome" Text
        [
            sg.Text("Welcome to New Brunswick's Fire Prediction & Protection System", font=("Helvetica", 29),),
        ],
        #Division
        [
            sg.Text("_"*150)
        ],
        
        
        #Stage One
        [
            sg.Text("Stage One: Metric Heat Map", font=("Helvetica", 22),),
        ],
        [
            sg.Text(" ")
        ],
        #Buttons to generate and save the data
        [
            sg.Button("View Metric Heatmap", key="-GENERATE_METRIC_MAP-", size=(26, 1), font=("Helvetica", 16), disabled=False, disabled_button_color='grey'),
            sg.Button("Save Metric Heatmap as PNG", key="-SAVE_METRIC_MAP-", size=(30, 1), font=("Helvetica", 16), disabled=True, disabled_button_color='grey'),
        ],
        #Division
        [
            sg.Text("_"*150)
        ],
        
        
        #Stage Two
        [
            sg.Text("Stage Two: At-Risk Area Heatmap", font=("Helvetica", 22),),
        ],
        [
            sg.Text(" ")
        ],
        #Buttons to generate and save the data
        [
            sg.Button("View At-Risk Area Heatmap", key="-GENERATE_RISK_MAP-", size=(26, 1), font=("Helvetica", 16), disabled=False, disabled_button_color='grey'),
            sg.Button("Save At-Risk Heatmap as PNG", key="-SAVE_RISK_MAP-", size=(30, 1), font=("Helvetica", 16), disabled=True, disabled_button_color='grey'),
        ],
        #Division
        [
            sg.Text("_"*150)
        ],
        
        
        #Stage Three
        [
            sg.Text("Stage Three: Fire Station Bubble Map", font=("Helvetica", 22),),
        ],
        [
            sg.Text(" ")
        ],
        #Text to tell the user to select their desired city for viewing for Stage 3
        [
            sg.Text("Select Key Loaction to View: ", font=("Helvetica", 16))
        ],
        #Buttons to generate and save the data
        [
            sg.Combo(['Saint John','Moncton','Fredericton', 'Miramichi','Bathurst','Mactaquac','Mount Carleton','Parlee Beach', 'Kouchibouguac', 'Fundy', 'Gagetown'],font=("Helvetica", 16), size=(30, 1), default_value='Saint John',key='-KEY_COMBO-'),
            sg.Button("View Fire Station Area Bubble Map", key="-GENERATE_STATION_MAP-", size=(26, 1), font=("Helvetica", 16), disabled=True, disabled_button_color='grey'),
            sg.Button("Save Fire Station Bubble Map as PNG", key="-SAVE_STATION_MAP-", size=(30, 1), font=("Helvetica", 16), disabled=True, disabled_button_color='grey'),
        ],
        #Division
        [
            sg.Text("_"*150)
        ],
        
        #If the user wishes to save the maps, this is where they specify the location
        [
            sg.Text("Path to Save Generated Map:", size=(width, 1), font=("Helvetica", 20)),
            sg.Input(key="-SAVE_PATH-", size=(30, 1), font=("Helvetica", 20), enable_events='true', readonly='true', disabled_readonly_background_color='white', disabled_readonly_text_color='black'),
            sg.FolderBrowse(key="-SAVE_BROWSE-", size=(15, 1), font=("Helvetica", 16), enable_events='true') #Browse by file type doesn't work on mac as there is a pysimplegui tkinter bug with it
        ],
    ]

    return layout


def create_result_layout(image, dist_between,morat,next_opp,seconds,date):

    layout = [
    ]
    
    return layout