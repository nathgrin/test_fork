class file_class():
    fname = ""

    def __init__(self, fname):
        self.fname = fname

    def clearfile(self):
        open(self.fname, 'w').close()

    def write_appline(self, writeline):
        with open(self.fname, 'a') as thefile:
            thefile.write(writeline)

