# Introduction
This program is a MVP (Minimal Viable Product) and is written in Python.

Program aims to implement:
1. one-way synchronization from source folder to replica folder
1. periodical synchronization
1. logging of operations to command line interface
1. logging of operations to a log file

User has to provide source and replica folders. Log file is created when not present.

Program uses only built-in libraries. 

# Next steps
As a MVP, the script covers the assignment with the most probable scenario and should be consulted with the client to discuss further steps.

Those steps can be:
1. handling of wrong (eg. format) input parameters
1. improvement of information saved to the log file 
1. performance optimization
1. control for security

# Usage examples
Examples assume command line interface is opened at the __sync_folder.py__ file location. For other locations, absolute or relative path must be provided for .py file location, source folder, replica folder and log file location.

## Get help for command syntax
```
python sync_folder.py -h
```

## One-time synchronization only
```
python sync_folder.py '.\source' '.\replica' 0 '.\log.txt'
```
