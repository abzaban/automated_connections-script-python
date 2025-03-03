import os
import paramiko
import sys

def processLine(line):
    node = line.strip()
    if "@" in node and "#" in node:
        username, secondNode = node.split("@")
        ip, password = secondNode.split("#")
        sshConn(str(ip), str(username), str(password))
    else:
        print("Invalid connection format")
    return

def sshConn(ip, username, password):
    sshClient = paramiko.SSHClient()
    status = ""
    try:
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshClient.connect(ip, username=username, password=password, timeout=10.0)
        status = "OK"
    except Exception:
        status = "ERROR"
    finally:
        print(f"[{status}]\t\t{username}@{ip}")
        outputFile = open(pathOutputFile, "a")
        outputFile.write(f"[{status}]\t\t{username}@{ip}" + os.linesep)
        outputFile.close()
        sshClient.close()
    return

if len(sys.argv) > 1:
    outputFileName = sys.argv[1]
    try:
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        pathInputFile = os.path.join(scriptDir, "in", "ssh-conn.txt")
        pathOutputFile = os.path.join(scriptDir, "out", f"{outputFileName}.txt")
        with open(pathInputFile, "r") as file:
            lines = file.readlines()
            file.close()
            for line in lines:
                processLine(line)
    except FileNotFoundError:
        print(f"Error: The input file was not found in the directory: {pathInputFile}")
else:
    print("It is required to pass the output file name as a parameter")
