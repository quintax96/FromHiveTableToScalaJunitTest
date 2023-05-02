from HiveTableToScalaDataframe import HiveTableToScalaDataframe
import PySimpleGUI as sg

def main():

    files : list[str] = sg.popup_get_file('Insert the file containing: hive table name, the hive query result table output and a file containing a list of tuple like [("id","int"),("name","string")]', multiple_files=True)

    HiveTableToScalaDataframe().run(files)

if __name__ == "__main__":
    main()