import os, sys

name = 'restart'
enabled = False
operator = True

def cmd(self, c, e, line, message_source, target):
    self.connection.disconnect('Restarting from command')
    os.execl(sys.executable, sys.executable, * sys.argv)