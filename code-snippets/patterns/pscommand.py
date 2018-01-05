"""
The command pattern is handy in situations when,
for some reason, we need to start by preparing what will be
 executed and then to execute it when needed.
 The advantage is that encapsulating actions in such a way enables
 Python developers to add additional functionalities
 related to the executed actions, such as undo/redo,
or keeping a history of actions and the like.
"""

import os

class RenameFileCommand(object):
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)

class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(RenameFileCommand('../passwd', '../password'))
history.execute(RenameFileCommand('../tmp.json', '../temp.json'))
#history.undo()
history.undo()

