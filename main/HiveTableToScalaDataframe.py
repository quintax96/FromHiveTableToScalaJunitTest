import PySimpleGUI as sg

class HiveTableToScalaDataframe:
    def run(self, files):
        # initialize an empty string to store the output Scala code
        scala_code = ""
        # split the input files by semicolon
        files = files.split(";")

        # loop over each file
        for file in files:
            with open(file, "r") as inputFile:
                # read all the lines from the file
                lines = inputFile.readlines()
                # extract the table name and list of types
                tableName = lines[0]
                lines.pop(0)
                listaTipi = eval(lines[0])
                lines.pop(0)
                # remove unnecessary lines
                lastLine = len(lines) - 1
                lines.pop(lastLine)
                lines.pop(2)
                lines.pop(0)

            # start building the Scala code
            scala_code = scala_code + "\n\nval " + tableName.strip("\n") + " = List(\n" 

            # extract the field names from the first line
            campi = lines[0].strip().rstrip('\n,').replace('|', '', 1).split('|')
            campi.pop(len(campi) -1) # remove last item because it is a ',' character

            # remove the first line from the list of lines
            lines.pop(0) 

            c = 0

            # loop over each row of data
            for i in lines:
                scala_code = scala_code + "("

                # extract the values for the current row
                valori = lines[c].split('|')
                valori.pop(len(valori) - 1)
                valori.pop(0)

                s = ""
                y = 0

                # build up a string of values for the current row
                for j in valori:
                    # if the value is a string, surround it with double quotes
                    if listaTipi[y][1] == "string" and len(listaTipi) == len(campi):
                        s = s + '"' + j.strip() + '",\t'
                    else:
                        s = s + j.strip() + ",\t"
                    y = y + 1

                # add the row values to the Scala code
                scala_code = scala_code + s.rstrip(",\t")
                scala_code = scala_code + "),\n"
                c = c + 1    

            # remove the trailing comma and newline from the Scala code
            scala_code = scala_code.rstrip('\n,') 
            scala_code = scala_code + "\n).toDF("

            c = 0

            # add the field names to the Scala code
            for i in campi:
                if c < len(campi) - 1:
                    scala_code = scala_code + '"' + campi[c].strip() + '",'
                else:
                    scala_code = scala_code + '"' + campi[c].strip() + '")'
                c = c + 1

        # create a PySimpleGUI window to prompt the user to save the output Scala code
        layout = [[sg.Input(expand_x=True, key='-FILE-'), sg.Button('SaveAs'), sg.Button('Save')]]
        window = sg.Window("save the dataframe in a specified path", layout, finalize=True)
        sg.theme('darkBlue4')

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break

            elif event == 'SaveAs':
                # prompt the user to select a file to save the Scala code to
                filename = values['-FILE-']
                filename = sg.popup_get_file("Save As", default_extension='.txt', default_path=filename, save_as=True, file_types=(("All TXT Files", "*.txt"),), no_window=True)
                if filename:
                    window['-FILE-'].update(filename)

            elif event == 'Save':
                # save the Scala code to the specified file
                filename = values['-FILE-']
                if filename:
                    try:
                        with open(filename, 'wt') as f:
                            f.write(scala_code)
                        sg.popup(f"File {repr(filename)} Saved !!!")
                        continue
                    except PermissionError:
                        pass
                sg.popup(f"Cannot open file {repr(filename)} !!!")

        # close the PySimpleGUI window
        window.close()