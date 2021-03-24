from Project.Controller.Actions import NavigateTableAction

def navigateTableButton(mainWindow, qtw):
    mainWindow.NavigateTableButton = qtw.QAction('Navigate to table view', mainWindow, checkable=False)
    mainWindow.NavigateTableButton.triggered.connect(lambda : NavigateTableAction.uponActionPerformed(mainWindow, qtw))