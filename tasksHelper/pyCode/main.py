def main(jsonFile, backupJsonFile):
    # TODO: clean up toString van tasks en app. 
    _input = ''
    
    app = App(jsonFile, backupJsonFile)

    # start main loop
    while _input != 'q':
        #print all tasks: 
        print('\n\t\t ===== All current tasks: =====\n')
        app.printTasks()

        print('\n\n===== Add (a) Edit (e) Delete (d) Show (s) Quit (q) =====')
        _input = input('===== Input: ')
            
        if _input == 'a':
            app.addTask()
        if _input == 's':
            app.printTask()
        if _input == 'e':
            app.editTask()
        if _input == 'd':
            app.deleteTask()

if __name__ == '__main__':
    import os
    # from Task import *
    from App import *

    # set json file with all tasks
    jsonFile = '/home/webadmin/scripts/tasksHelper/tasks.json'
    backupJsonFile = '/home/webadmin/scripts/taskHelper/.backups/backup.json'

    main(jsonFile, backupJsonFile)