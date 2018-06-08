class FileManager:

    def __init__(self):
        self.fileHandle = None

    def openFile(self, filename, mode="r"):
        self.fileHandle = open(filename, mode)

    def readFile(self):
        print(self.fileHandle.readLines())

    def writeToFile(self, message):
        self.fileHandle.write(message)

    def closeFileHandler(self):
        self.fileHandle.close()


f = FileManager()

f.openFile("test.txt")
f.readFile()
f.writeToFile("Guten højteløjte")
f.closeFileHandler()