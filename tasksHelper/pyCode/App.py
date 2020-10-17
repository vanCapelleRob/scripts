import json
import os
from Task import *

class App:
    def __init__(self, jf, bjf):
        self.tasks = [] # list of Task
        self.JSONFile = jf
        self.backupJSONFile = bjf
        
        self.fillTasks()
        self.lastId = self.getLastID()

        
            

    def writeToJson(self):
        self.orderTasks()
        jsonTasks = {}
        jsonTasks['tasks'] = []
        for t in self.tasks:
            jsonTasks['tasks'].append({
                'id': t.id, 
                'name': t.name, 
                'class': t._class, 
                'info': t.info, 
                'date-due': t.dateDue, 
                'days-left': t.daysLeft, 
                'importance': t.importance
            })

        with open(self.JSONFile, 'w') as jsonOut:
            json.dump(jsonTasks, jsonOut)
    
    def makeBackup(self):
        pass

    def getLastID(self):
        biggestID = -1

        if len(self.tasks) == 0: return biggestID

        for task in self.tasks:
            if task.id > biggestID:
                biggestID = task.id
        return biggestID

    def fillTasks(self):
        jsonFile = self.JSONFile
        with open(jsonFile, 'r') as jsonIn:
            data = json.load(jsonIn)
            for t in data['tasks']:
                task = Task(t['id'], t['name'], t['class'], t['info'], t['date-due'], t['days-left'], t['importance'])
                self.tasks.append(task)

    def checkInput(self, input):
        if input != '':
            return True
        else:
            return False

    def addTask(self):
        temp = DummyTask()

        myId = self.lastId+1
        temp.id = myId
        name = input('Name: ')
        if self.checkInput(name): temp.name = name
        _class = input('Class: ')
        if self.checkInput(_class): temp._class =_class
        info = input('Info: ')
        if self.checkInput(info): temp.info = info
        dateDue = input('Date due (dd/mm/yyyy): ')
        if self.checkInput(dateDue): temp.dateDue = dateDue
        daysLeft = input('Days left: ')
        if self.checkInput(daysLeft): temp.daysLeft = daysLeft
        importance = input('Importance (1-10): ')
        if self.checkInput(importance): temp.importance = int(importance)

        self.lastId = myId

        os.system('clear')
        self.tasks.append(temp)
        self.writeToJson()

    def getTask(self, taskId):
        for task in self.tasks:
            if task.id == int(taskId):
                return task

    def editTask(self):
        taskId = input('===== Give task number you want to edit: ')
        os.system('clear')
        print('Dit is de huidige taak: ')
        self.printTask(taskId)

        oldTask = self.getTask(taskId)
        
        # name = oldTask.name
        # _class = oldTask._class
        # info = oldTask.info
        # dateDue = oldTask.dateDue
        # daysLeft = oldTask.daysLeft
        # importance = oldTask.importance

        print('\n Geef de nieuwe waardes in: (laat leeg voor niet te veranderen)')
        name = input('Name: ')
        if self.checkInput(name): oldTask.name = name
        _class = input('Class: ')
        if self.checkInput(_class): oldTask._class =_class
        info = input('Info: ')
        if self.checkInput(info): oldTask.info = info
        dateDue = input('Date due (dd/mm/yyyy): ')
        if self.checkInput(dateDue): oldTask.dateDue = dateDue
        daysLeft = input('Days left: ')
        if self.checkInput(daysLeft): oldTask.daysLeft = daysLeft
        importance = input('Importance (1-10): ')
        if self.checkInput(importance): oldTask.importance = int(importance)


        self.tasks[oldTask.id] = oldTask
        self.writeToJson()
        os.system('clear')

    def deleteTask(self):
        taskId = input('===== Give task number you want to delete: ')
        os.system('clear')
        
        taskToDelte = self.getTask(taskId)
        self.tasks.remove(taskToDelte) #delete task
        for task in self.tasks: # fix id's
            if task.id > taskToDelte.id:
                task.id = task.id - 1

        self.lastId = self.lastId -1
        self.writeToJson()

    def orderTasks(self):
        sortedTasks = []
        
        for i in range(len(self.tasks)):
            tempBiggest = None
            importance = -1
            for task in self.tasks:
                if task.importance >= importance:
                    importance = task.importance
                    tempBiggest = task
            self.tasks.remove(tempBiggest)
            sortedTasks.append(tempBiggest)
            sortedTasks[i].id = i

        self.tasks = sortedTasks

    def printTasks(self):
        # self.tasks.remove(self.dummyTask)
        # self.orderTasks()
        for task in self.tasks:
            if task.id != -1:       
                if len(task.name) >= 16:
                    print('Task' + str(task.id) + ':\t ' + task.name + '\t ' + task._class + '\t' + str(task.importance) + '\t' + task.dateDue)
                else:
                    print('Task' + str(task.id) + ':\t ' + task.name + '\t\t ' + task._class + '\t' + str(task.importance) + '\t' + task.dateDue)
        # self.tasks.append(self.dummyTask)

    def printTask(self, *args):
        taskId = 0
        if len(args) == 0:
            taskId = input('===== Give task number: ')
            os.system('clear')
        elif len(args) == 1 and isinstance(args[0], str):
            taskId = args[0]
        task = self.getTask(taskId)
        task.toString()

    
