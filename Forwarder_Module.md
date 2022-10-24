# Custom Build Forwarder
##### (Python/Stream-Lit/SSH)

## _Forwarder Module on StreamLit_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Pre-Requisites :
- streamlit
- shutil
- glob
- pyautogui
- ✨Magic ✨

## Features

Forward any sort of logs from any log-source to the Stip with just providing the address of log present in log-source
## Files

Following are the files included inthis software up till now :
- [Main StreamLit App](https://github.com/Junny2/Log-Forwarder/blob/main/StreamLit.py) - This file is the main file and is used to launch the GUI and the application.
- [T2auto](https://github.com/Junny2/Log-Forwarder/blob/main/T2auto.py) - This file is to hit/run the Task2Renaming file.
- [SJA_Log](https://github.com/Junny2/Log-Forwarder/blob/main/SJA_Log.py) - This is the configuration file.
- [Task2_Renaming](https://github.com/Junny2/Log-Forwarder/blob/main/Task2_Renaming.py) - This file make directories and rename the logs as per user defined format.
- [Postgresql](https://github.com/Junny2/Log-Forwarder/blob/main/postgresql.py) - This is the main technique file.

And of course it is NCCS open source project with a [public repository](http://172.16.16.45/employees/ueba/-/tree/main)
 on GitLab.

## Installation

Install the dependencies and devDependencies and start the server.

#### _Open cmd in the folder containing the files and hit the following command_
```sh
streamlit run StreamLit.py
```


