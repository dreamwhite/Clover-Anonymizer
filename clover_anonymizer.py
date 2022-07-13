#!/usr/bin/python3.10

import os
import plistlib
import sys


def load_plist() -> dict:
    """Loads .plist XML like file and returns the opened buffer

    :return: dict-like object of the loaded plist
    """
    return plistlib.load(open(sys.argv[1], 'rb'))


class PlistStripper:
    def __init__(self):
        self.plist = load_plist()
        self.delete_CPU()
        self.delete_gui_custom_entries()
        self.delete_gui_hide()
        self.delete_rtvariables()
        self.delete_smbios()
        self.delete_system_parameters()
        self.dump()

    def delete_CPU(self) -> None:
        """Deletes custom CPU configuration from config.plist"""

        self.plist['CPU'] = []

    def delete_gui_custom_entries(self) -> None:
        """Deletes custom GUI entries from config.plist"""

        self.plist['GUI']['Custom']['Entries'] = []

    def delete_gui_hide(self) -> None:
        """Deletes hidden GUI entries from config.plist"""

        self.plist['GUI']['Hide'] = []

    def delete_rtvariables(self) -> None:
        """Censors several RTVariables identification fields"""

        self.plist['RtVariables']['MLB'] = 'XX-CHANGE_ME-XX'
        self.plist['RtVariables']['ROM'] = b'\x11"3DUf'

    def delete_smbios(self) -> None:
        """Censors several SMBIOS identification fields"""

        for key in self.plist['SMBIOS'].copy():
            if key != 'ProductName':
                self.plist['SMBIOS'].pop(key)

    def delete_system_parameters(self) -> None:
        """Censors SystemParameters/CustomUUID field"""

        self.plist['SystemParameters']['CustomUUID'] = 'XX-CHANGE_ME-XX'


    def dump(self):
        """Saves to a file the newly censored config.plist"""

        with open('censored_config.plist', 'wb') as f:
            try:
                plistlib.dump(self.plist, f)
                print(f"Successfully exported anonymized config.plist to {os.path.realpath(f.name)}")
            except (Exception,):
                print("An error occurred while trying to save the censored config.plist file!")

if __name__ == '__main__':
    plist_stripper = PlistStripper()
