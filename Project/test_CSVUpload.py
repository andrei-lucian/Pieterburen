import unittest
import pandas as pd
import Project.Model.BackEnd.BackEnd as be
from Project.Controller.Actions.OpenAction import CSVUpload
from Project.View.ViewCards import ViewHandler
import PyQt5.QtWidgets as qtw
from Project.Controller.Actions import FileUploadAction

class TestCSVUpload(unittest.TestCase):
    def setUp(self):
        self.app = qtw.QApplication([])
        screenResolution = self.app.desktop().screenGeometry()
        windowHeightToScreen, windowWidthToScreen = 0.7, 0.6
        width, height = int(screenResolution.width() * windowWidthToScreen), int(
             screenResolution.height() * windowHeightToScreen)
        self.backend = be.BackEnd()
        self.mw = ViewHandler.MainWindow(width, height, self.backend, 0)
        self.tableView = self.mw.getTableView()
        self.backend.addTableView(self.tableView)

    # This tests both the parseCSVFiles, openAction and CSVUpload methods at once;
    # CSVUpload is needed to get .csv file to test parseCSVFiles with
    def test_CSVUpload(self):
        self.backend.clear()
        self.assertTrue(self.backend.data.empty)

        # Upload valid .csv file
        CSVUpload(self.mw, qtw)
        index = 0

        actual = self.backend.data.loc[index, ["Left Lung Whistle"]].values[0]
        result = "Yes"
        result2 = "No"
        result3 = "Unknown"
        result4 = ""
        self.assertTrue(actual in [result, result2, result3, result4])

        actual = self.backend.data.loc[index, ["Right Lung Whistle"]].values[0]
        result = "Yes"
        result2 = "No"
        result3 = "Unknown"
        result4 = ""
        self.assertTrue(actual in [result, result2, result3, result4])

        actual = self.backend.data.loc[index, ["Left Lung Rhonchus"]].values[0]
        result = "Okay"
        result2 = "Mild"
        result3 = "Moderate"
        result4 = "Severe"
        result5 = "Unknown"
        result6 = ""
        self.assertTrue(actual in [result, result2, result3, result4, result5, result6])

        actual = self.backend.data.loc[index, ["Right Lung Rhonchus"]].values[0]
        result = "Okay"
        result2 = "Mild"
        result3 = "Moderate"
        result4 = "Severe"
        result5 = "Unknown"
        result6 = ""
        self.assertTrue(actual in [result, result2, result3, result4, result5, result6])


if __name__ == '__main__':
    unittest.main()
