import PySimpleGUI as sg

class HiveTableToScalaDataframe:

    def run(self, files):

        str = ""
        files = files.split(";")

        for file in files:

            with open(file, "r") as inputFile:
                lines = inputFile.readlines()
                tableName = lines[0]
                lines.pop(0)
                listaTipi = eval(lines[0])
                lines.pop(0)
                lastLine = len(lines) - 1
                lines.pop(lastLine)
                lines.pop(2)
                lines.pop(0)

            str = str + "\n\nval " + tableName.strip("\n") + " = List(\n" 

            #generating the fields list[String]
            campi = lines[0].strip().rstrip('\n,').replace('|', '', 1).split('|')
            campi.pop(len(campi) -1) #remove last item beacasue it is a ',' char

            #remove fileds from the list[String]
            lines.pop(0) 

            c = 0

            for i in lines:
                str = str + "("

                valori = lines[c].split('|')
                valori.pop(len(valori) - 1)
                valori.pop(0)

                s = ""
                y = 0

                for j in valori:

                    if listaTipi[y][1] == "string" and len(listaTipi) == len(campi):
                        s = s + '"' + j.strip() + '",\t'
                    else:
                        s = s + j.strip() + ",\t"
                    y = y + 1

                str = str + s.rstrip(",\t")
                str = str + "),\n"
                c = c + 1    

            str = str.rstrip('\n,') 
            str = str + "\n).toDF("

            c = 0

            for i in campi:
                if c < len(campi) - 1:
                    str = str + '"' + campi[c].strip() + '",'
                else:
                    str = str + '"' + campi[c].strip() + '")'
                c = c + 1

        layout = [[sg.Input(expand_x=True, key='-FILE-'), sg.Button('SaveAs'), sg.Button('Save')]]
        window = sg.Window("save the dataframe in a specified path", layout, finalize=True)
        sg.theme('darkBlue4')

        while True:

            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break

            elif event == 'SaveAs':
                filename = values['-FILE-']
                filename = sg.popup_get_file("Save As", default_extension='.txt', default_path=filename, save_as=True, file_types=(("All TXT Files", "*.txt"),), no_window=True)
                if filename:
                    window['-FILE-'].update(filename)

            elif event == 'Save':
                filename = values['-FILE-']
                if filename:
                    try:
                        with open(filename, 'wt') as f:
                            f.write(str)
                        sg.popup(f"File {repr(filename)} Saved !!!")
                        continue
                    except PermissionError:
                        pass
                sg.popup(f"Cannot open file {repr(filename)} !!!")

        window.close()