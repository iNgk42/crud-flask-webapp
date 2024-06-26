# Logique metier de l'application
from database import task_store
from datetime import date

class Task:
    def __init__(self, task_id, task_title, task_description, task_due_date, task_registration_date):
        self.id = task_id
        self.title = task_title
        self.description = task_description
        self.due_date = task_due_date
        self.registration_date = task_registration_date

    #get all tasks attributes
    def getAllTaskAttributes(self):
        task_attributes = [self.id, self.title, self.description, self.due_date, self.registration_date]
        return task_attributes

    #register new task to the system or db
    def register(self):
        if task_store == []:
            self.id = 0
        else:
            self.id = task_store[-1].id + 1

        self.registration_date = date.today().strftime("%d/%m/%y")
        task_store.append(self)

    #delete existing task to the system or db
    def remove(self):
        task_store.remove(self)

    #Mark existing task as done
    def acknowledge(self):
        pass

