import csv

class VersionData:
    def __init__(self, header):
        self.header = header
        self.text = []
        self.data = []

    def addText(self, line):
        self.text.append(line)

    def addData(self, line):
        self.data.append(line)

    def updateData(self, param, value, maximum=None):
        dataIndex = -1
        for i in range(len(self.data)):
            if self.data[i][1] == param:
                dataIndex = i
                break
        if dataIndex == -1:
            dataIndex = len(self.data)
            self.data.append([str(dataIndex+1), param])
        
        if maximum == None or len(self.data[dataIndex])-2 < maximum:
            self.data[dataIndex].append(value)
        
            if len(self.data[dataIndex])-2 > int(self.text[0][1]):
                self.text[0][1] = str(int(self.text[0][1]) + 1)
                self.text[-1].append(f"R{self.text[0][1]}")

def getData(filename):
    data = []
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            version = None

            for line in reader:
                if line[0] == "Version":
                    if version != None:
                        data.append(version)
                    version = VersionData(line)
                elif not line[0].isdigit():
                    version.addText(line)
                else:
                    version.addData(line)
            data.append(version)
    except FileNotFoundError:
        pass

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

def newVersion(label):
    version = VersionData(["Version", label])
    version.addText(["Run count", "0"])
    version.addText(["Test", "Input"])
    return version

def updateData(filename, version, param, value, maximum=None):
    data = getData(filename)
    recordIndex = -1
    for i in range(len(data)):
        if data[i].header[1] == version:
            recordIndex = i
    
    if recordIndex == -1:
        data.append(newVersion(version))
        recordIndex = len(data) - 1
    
    data[recordIndex].updateData(param, value, maximum)

    writeData(filename, data)

if __name__ == "__main__":
    updateData("testingRecord.csv", "potatoes", "10", 0.12312)
