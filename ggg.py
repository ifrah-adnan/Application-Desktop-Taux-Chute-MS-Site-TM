import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Créer un widget de tableau avec 5 lignes et 3 colonnes
        self.tableWidget = QTableWidget(5, 3)

        # Créer un dictionnaire pour garder une trace des lignes cliquées
        self.clicked_rows = {}

        # Remplir le widget de tableau avec des boutons dans chaque ligne
        for row in range(self.tableWidget.rowCount()):
            button = QPushButton(f"Cliquer {row}", self.tableWidget)
            button.clicked.connect(lambda checked, r=row: self.on_button_clicked(r))
            self.tableWidget.setCellWidget(row, 0, button)

        # Ajouter le widget de tableau à la fenêtre principale
        self.setCentralWidget(self.tableWidget)

    def on_button_clicked(self, row):
        if row in self.clicked_rows:
            # La ligne a déjà été cliquée, effectuer une action appropriée
            print(f"Ligne {row} déjà cliquée!")
        else:
            # Marquer la ligne comme cliquée
            self.clicked_rows[row] = True

            # Modifier la valeur d'une colonne dans le widget de tableau
            item = QTableWidgetItem("Nouvelle valeur")
            self.tableWidget.setItem(row, 1, item)

            # Enregistrer la modification dans une base de données (à implémenter)

            # Rafraîchir l'affichage du widget de tableau
            self.tableWidget.viewport().update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
