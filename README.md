![macOS](https://img.shields.io/badge/Supported_Clover_build:-≥_r5123-white.svg)

# Clover Anonymizer – remove sensitive data from your config.plist

## About
Python Script for removing sensitive data from Clover's `config.plist`. Useful if you plan to share your Config/EFI online. Also resets some settings to default values which should not be carried over to a different system. Check the feature list for more details.

Based on my [OC-Anonymizer](https://github.com/dreamwhite/OC-Anonymizer) work

## Features

Changes the following Settings/Parameters in the **config.plist**:

- Strips most of **SMBIOS** related data such as:
	- `SMBIOS/ProductName` untouched
	- `RtVariables`:
		- anonymized `MLB` and `ROM`
	- Anonymized `SystemParameters/CustomUUID`
- **Other Settings**:
	- Deletes custom values from `CPU` section
	- Deletes custom entries from `GUI/Custom/Entries`
	- Deletes hidden entries from `GUI/Hide`

## Instructions
- Install [**Python**](https://www.python.org/) if you haven't already
- Click on "Code" > "Download ZIP" and upack it.
- Copy/move the **Clover-Anonymizer-master** folder to your Desktop
- Start Terminal
- Enter:</br>
`cd desktop/Clover-Anonymizer-master`
- Next, enter </br>`python3 clover_anonymizer.py PATH_TO_CONFIG.plist` (you can also drag and drop the config into the terminal)
- Hit `ENTER`

This will create a `censored_config.plist`in the `clover_anonymizer` folder without sensitive data and changed settings as described. 

## Credits and Resources

- [Acidanthera](https://github.com/acidanthera) for [OpenCorePkg](https://github.com/acidanthera)
- [5T33Z0](https://github.com/5T33Z0) for the idea
