class Task:
    def __init__(self, id, name, _class, info, dd, dl, importance):
        self.id = id
        self.name = name
        self._class = _class
        self.info = info
        self.dateDue = dd
        self.daysLeft = dl
        self.importance = importance

    def toString(self):
        print('\n\t\t ===== Overview of task: ' + self.name + ' =====\n')
        print('Task' + str(self.id) + ': \t ' + self._class + ' \t ' + self.info)

    def getId(self):
        return self.id




class DummyTask(Task):
    def __init__(self):
        Task.__init__(self, -1, 'noName', 'noClass', 'noInfo', 'noDateDue', 1, 5)
        