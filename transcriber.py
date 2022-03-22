import csv
import functools
import time

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
    with open(filename, "w", newline='') as f:
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
            break

    if recordIndex == -1:
        data.append(newVersion(version))
        recordIndex = len(data) - 1
    
    data[recordIndex].updateData(param, value, maximum)

    writeData(filename, data)

def deleteRecord(filename, version, safeguard=True):
    data = getData(filename)
    if len(data) == 0:
        print(f"Attempted to delete from the file {filename}, but file does not exist")
        return None

    recordIndex = -1
    for i in range(len(data)):
        if data[i].header[1] == version:
            recordIndex = i
            break
    
    if recordIndex == -1:
        print(f"Attempted to delete the version {version} on file {filename}, but version does not exist")
        return None
    
    confirmation = ''
    if safeguard:
        confirmation = input(f"Deleting version {version} on file {filename}. Enter YES to confirm you want to continue:\n")
    if not safeguard or confirmation == 'YES':
        data.pop(recordIndex)
        writeData(filename, data)

def timerToFunction(outfunc):
    def decorator_output(func):
        def wrapper(*args, **kwargs):
            start = time.process_time()
            result = func(*args, **kwargs)
            end = time.process_time()
            outfunc(end-start)
            return result 
        return wrapper
    return decorator_output

def recordtime(output, version, maximum=10):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bt = time.process_time()
            result = func(*args, **kwargs)
            et = time.process_time()
            elapsed = et - bt
            args_repr = [repr(a) for a in args] 
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            updateData(output, version, signature, elapsed, maximum)
            return result
        return wrapper
    return decorator


