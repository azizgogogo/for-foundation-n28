from PyQt5.QtWidgets import *
from CategoryRepository import CategoryRepository

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.categoryRepo = CategoryRepository()
        self.windowSettings()

    def windowSettings(self):
        self.setFixedSize(500, 700)
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(20, 20, 200, 300)
        self.listWidget.itemClicked.connect(self.listWidgetItem)
        self.setCategories()


        self.createLineEdit = QLineEdit(self)
        self.createButton = QPushButton("Save", self)

        self.createLineEdit.move(220, 20)
        self.createButton.move(350, 20)

        self.createButton.clicked.connect(self.createCategory)


        
    def setCategories(self):
        self.listWidget.clear()
        

        for item in self.categoryRepo.getAll():
            newItem = QListWidgetItem()
            newItem.setText(item["name"])
            newItem.categoryData = item
            self.listWidget.addItem(newItem)

    def listWidgetItem(self):
        categoryId = self.listWidget.currentItem().categoryData["id"]
        self.deleteCategory(categoryId)


    
    def createCategory(self):
        self.categoryRepo.create(self.createLineEdit.text())
        self.createLineEdit.clear()
        self.setCategories()

    def deleteCategory(self, id = ""):
        
        msgBox = QMessageBox.question(self, "Title", "Delete ?",
                                       QMessageBox.Yes | QMessageBox.No)

        if msgBox == QMessageBox.Yes:
            self.categoryRepo.delete(id)

        self.setCategories()




app = QApplication([])
window = Window()
window.show()
app.exec()