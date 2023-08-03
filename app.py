from PyQt5.QtWidgets import *
from CategoryRepository import CategoryRepository

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.windowSettings()

    def windowSettings(self):
        self.setFixedSize(500, 700)
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(20, 20, 200, 300)
        self.listWidget.itemClicked.connect(self.listWidgetItem)
        self.setCategories()

        
    def setCategories(self):
        categories = CategoryRepository()

        for item in categories.getAll():
            newItem = QListWidgetItem()
            newItem.setText(item["name"])
            newItem.categoryData = item
            self.listWidget.addItem(newItem)

    def listWidgetItem(self):
        print(self.listWidget.currentItem().categoryData)





    




app = QApplication([])
window = Window()
window.show()
app.exec()