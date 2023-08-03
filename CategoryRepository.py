from connection import dbConnection
from uuid import uuid4

class CategoryRepository:
     def __init__(self):
          self.dbConnection = dbConnection()
          self.cursor = self.dbConnection.cursor()

     def getAll(self):
          query = "SELECT * FROM categories"
          self.cursor.execute(query)
          categories = self.cursor.fetchall()
          allCategories = []
          for (id, name) in categories:
               allCategories.append({
                    "id": id,
                    "name": name
               })

          return allCategories
     
     def delete(self, id):
          query = "DELETE FROM categories where category_id = %s"
          self.cursor.execute(query, (id, ))
          self.dbConnection.commit()

     def create(self, categoryName):
          query = """INSERT INTO categories 
                    (category_id, category_name) values(%s, %s)"""
          
          self.cursor.execute(query, (str(uuid4()), categoryName))

          self.dbConnection.commit()




obj = CategoryRepository()
# # print(obj.getAll())

# obj.delete("cas343jcbaj454cbja")

# obj.create("Snaks")