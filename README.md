# automated_connections-script-python
Scripts to automate connections with ssh and socket.

# Prepare connections
In the in folder are the input files used by both scripts, you must fill out the file using the corresponding format for each connection you want to automate. For SSH connections the format is username@ip#password and for Socket connections the format is ip:port.

# Run project
Open a CLI in root folder of project and then run:

```sh
pip3 install paramiko
python3 ./socket-conn.py outputFileName
python3 ./ssh-conn.py outputFileName
```
