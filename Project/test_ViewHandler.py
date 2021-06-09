import unittest
import PyQt5.QtWidgets as qtw
from Project.View.Miscellaneous import SplashScreen
from Project.View.ViewCards import ViewHandler
from Project.Model.BackEnd import BackEnd as be
import threading
from Project.View.ViewCards import ViewHandler
from Project.main import backEnd as be


class TestViewHandler(unittest.TestCase):
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

    def test_switchViews(self):
        # check if starts at table view
        self.assertEqual(self.mw.mainWidget.layout().getCurrentIndex(), 0)

        # Change to statistics view
        self.mw.switchViews("statistics")
        self.assertEqual(self.mw.mainWidget.layout().getCurrentIndex(), 1)

        # change back to table view
        self.mw.switchViews("table")
        self.assertEqual(self.mw.mainWidget.layout().getCurrentIndex(), 0)


if __name__ == '__main__':
    unittest.main()
