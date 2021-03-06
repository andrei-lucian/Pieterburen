from Project.Controller.Actions import NavigateTableAction

def navigateTableButton(mainWindow, qtw):
    mainWindow.NavigateTableButton = qtw.QAction('Table', mainWindow, checkable=False)
    mainWindow.NavigateTableButton.setShortcut('Shift+Tab')
    mainWindow.NavigateTableButton.setEnabled(False)
    mainWindow.NavigateTableButton.triggered.connect(lambda : NavigateTableAction.uponActionPerformed(mainWindow, qtw))