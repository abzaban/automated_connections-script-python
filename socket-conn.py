import os
import socket
import sys

def processLine(line):
    node = line.strip()
    if ":" in node:
        ip, port = node.split(":")
        if port.isnumeric():
            socketConn(str(ip), int(port))
        else:
            print(f"Invalid port for the IP: {ip}, port: {port}")
    else:
        print("Invalid connection format")
    return

def socketConn(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = ""
    try:
        s.settimeout(10)
        s.connect((ip, port))
        status = "OK"
    except Exception:
        status = "ERROR"
    finally:
        print(f"[{status}]\t\t{ip}:{port}")
        outputFile = open(pathOutputFile, "a")
        outputFile.write(f"[{status}]\t\t{ip}:{port}" + os.linesep)
        outputFile.close()
        s.close()
    return

if len(sys.argv) > 1:
    outputFileName = sys.argv[1]
    try:
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        pathInputFile = os.path.join(scriptDir, "in", "socket-conn.txt")
        pathOutputFile = os.path.join(scriptDir, "out", f"{outputFileName}.txt")
        with open(pathInputFile, "r") as inputFile:
            lines = inputFile.readlines()
            inputFile.close()
            for line in lines:
                processLine(line)
    except FileNotFoundError:
        print(f"Error: The input file was not found in the directory: {pathInputFile}")
else:
    print("It is required to pass the output file name as a parameter")
