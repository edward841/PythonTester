import csv
"""
with open("testingFiles.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Version", 1, "Humble Beginnings"])
    writer.writerow(["Test#", "Test Parameters", "Run1", "Run2"])
"""
class VersionData:
            
    def __init__(self, header):
        self.header = header
        self.text = []
        self.data = []

    def addText(self, line):
        self.text.append(line)

    def addData(self, line):
        self.data.append(line)


def getData(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        version = None

        for line in reader:
            if line[0] == "Version":
                if version != None:
                    data.append(version)
                version = VersionData(line)
            else if not isdigit(line[0]):
                version.addText(line)
            else:
                version.addData(line)
    return data

def writeData(filename, data):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        for version in data:
            writer.writerow(version.header)
            for line in version.text:
                writer.writerow(line)
            for line in version.data:
                writer.writerow(line)

def newVersion():
    version = VersionData(["Version", 1])
    version.addText(["Test"])
    return version

def updateTimes(filename, version, param, time):
    data = getData(filename)
    if len(data) == 0:
       data.append(newVersion())
    
    writeData(filename, data)

if __name__ == '__main__':
    getData("testingFiles.csv")



