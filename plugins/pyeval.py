import re, math, random
from sandbox import Sandbox, SandboxConfig

name = 'pyeval'
enabled = True
operator = False

def cmd(self, c, e, line, message_source, target):
    def pass_func(x):
        return x
    try:
        self.send(c, target, str(self.sandbox.call(pass_func, eval(line[1], {"math": math, "re": re, "random": random}))).replace("\n", ""))
    except Exception as ex:
        self.send(c, target, "Error: " + str(ex))

def init(self):
    self.sandbox = Sandbox(SandboxConfig('unicodedata', 'random', 'regex', 'math'))