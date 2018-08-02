class League:

    current = ""

    def __init__(self, current):
       self.current = current

    def setCurrent(self, new):
        self.current = new
    
    def getCurrent(self):
        return self.current