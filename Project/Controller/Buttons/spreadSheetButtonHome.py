from Project.Controller.Actions import CSVFileUploadAction


def spreadSheetButtonHome(homeView, qtw, qtg, mainWindow):
    spreadsheetButton = qtw.QPushButton(homeView)

    spreadsheetButton.setStyleSheet("QPushButton{"
                                    "background-color:#020117; "
                                    "border:2px white; "
                                    "color:white; "
                                    "border-radius: 25px;"
                                    "border-style: outset"

                                    "} "
                                    "QPushButton::pressed{"
                                    "border: 4px solid gray; "
                                    "color: gray"
                                    "}")

    spreadsheetButton.setFont(qtg.QFont('Comic Sans', 20))
    spreadsheetButton.setText("Upload\n Spreadsheet")
    spreadsheetButton.setFixedHeight(160)
    spreadsheetButton.clicked.connect(lambda: CSVFileUploadAction.uponActionPerformed(mainWindow, qtw))
    #spreadsheetButton.clicked.connect(lambda: mainWindow.switchViews("table"))
    return spreadsheetButton
