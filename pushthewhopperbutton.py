#!/usr/bin/env python

import os
import platform
import yaml

def checkInstallation(path):
    # Makes sure files are where we expect them to be
    if platform.system() == 'Windows':
        assert os.path.exists(os.path.join(path, "SuperVHS.exe"))
        print("We found it!!!")


if __name__ == "__main__":
    try:
        with open("config.yaml",'r') as f:
            config = yaml.safe_load(f)
            VHSPATH = config.vhspath
            checkInstallation(VHSPATH)

    except Exception as e:
        VHSPATH = input("Enter path to SuperVHS installation: ")
        checkInstallation(VHSPATH)
        with open("config.yaml",'w') as f:
            f.write(yaml.dump({"vhspath":VHSPATH}))

