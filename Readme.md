# JAMF ClassToGroup
For converting Classes to Groups in the JAMF MDM. 

Tested and working in Python 2.7, needs to be updated to Python 3.

## Usage
[**groupWipe.py**](src/classToGroup.py): This script is a cleanup utility to delete all *static* groups in JAMF. **In most cases, run this first**, unless you have static groups that need to remain. 
 1. Ensure that you intend to remove ALL static groups from JAMF
 2. Run the script with Python 2.7
 3. Enter your username, password, and JSS/JAMF Pro URL for authentication
 4. Wait for the script to complete, all JAMF static groups should now be removed.

[**classtoGroup.py**](src/classToGroup.py): This is the main script, **in most cases, run this last.** It will convert all classes in JAMF to static groups.
 1. Run the script with Python 2.7
 2. Enter your username, password, and JSS/JAMF Pro URL for authentication
 3. Wait for the script to complete, all JAMF classes should now also be static groups.


## Contributing
Pull requests are welcome, feel free to submit issues as well.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
