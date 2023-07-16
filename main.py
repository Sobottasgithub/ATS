import json
import pathfinding
import os, sys
from PyQt5 import QtWidgets, uic

# load graph and aliases data
with open(os.path.join(os.path.dirname(sys.argv[0]), "data/graph.json")) as json_file:
    graph = json.load(json_file)
with open(os.path.join(os.path.dirname(sys.argv[0]), "data/aliases.json")) as json_file:
    aliases = json.load(json_file)

# "simulated SERVER"
bus_stops_at = []
route = []


class Main_Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        global color_json_read

        uic.loadUi(os.path.join(os.path.dirname(
            sys.argv[0]), "UserInterface.ui"), self)
        self.setWindowTitle("ATS")

        for i in aliases:
            if ".comment" not in i:
                self.start.addItem(i)
                self.ziel.addItem(i)

        self.book_button.clicked.connect(self.create_path)
        self.trip_waypoints.setWordWrap(True);

    def create_path(self):
        global bus_stops_at
        global route

        start = str(self.start.currentText())
        ziel = str(self.ziel.currentText())

        if start != ziel:
            bus_stops_at.append(start)
            bus_stops_at.append(ziel)

            p = pathfinding.search(graph, aliases[start], aliases[ziel])

            if route == []:
                for i in range(len(p['path'])):
                    route.append(p['path'][i])
                self.trip_waypoints.setText("new bus with your route: "+ str(route))
            else:   
                if any(start in s for s in route):
                    for i in range(len(p['path'])):
                        if p['path'][i] not in route:
                            route.append(p['path'][i])
                        else:
                            pass

                    self.trip_waypoints.setText("Existing bus with your route "+ str(route))

                else:
                    self.trip_waypoints.setText("new bus with your route "+ str(p['path']))

# mainapp run
#simulation: user 1
application_run = QtWidgets.QApplication(sys.argv)
Main_application = Main_Ui()
Main_application.show()
application_run.exec_()

#simulation: user 2
application_run1 = QtWidgets.QApplication(sys.argv)
Main_application1 = Main_Ui()
Main_application1.show()
application_run1.exec_()