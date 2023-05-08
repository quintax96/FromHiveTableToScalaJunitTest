from HiveTableToScalaDataframe import HiveTableToScalaDataframe
import PySimpleGUI as sg

def main():
    # Prompt the user to select the input files
    files = sg.popup_get_file(
        'Insert the file containing: hive table name, the hive query result table output and a file containing a list of tuple like [("id","int"),("name","string")]', 
        multiple_files=True
    )

    # Run the HiveTableToScalaDataframe class on the selected files
    HiveTableToScalaDataframe().run(files)

if __name__ == "__main__":
    # Call the main function
    main()