# AsyncRebootMeraki #
-----------------
Small utility that asyncronously reboots multiple meraki dashboard devices.

The minimum that is needed are serial numbers - they must be in a dictironary nested in a list e.g.

'''
serial_numbers = [{'serial': 'XXX-XXX-XXX'}, {'serial': 'XXX-XXX-XXX'}]
'''


## Install and Use

In rebootremeraki.py, set your API key and either change the serial numbers or add code to read SNs from text or CSV and build a list in the following format:

'''
serial_numbers = [{'serial': 'XXX-XXX-XXX'}, {'serial': 'XXX-XXX-XXX'}]
'''

**Note that the code *will* prompt before rebooting devices.**


Python Virtual Environment is the preferred install method but to install to your default python (tested with 3.9 or newer):

**1. Clone this repository locally**
```
git clone https://github.com/zabrewer/AsyncRebootMeraki.git
```
**2. Install from setup.py**

```
pip install .
```

### Installing to a Python Virtual Environment

Note: For Mac OSX, replace "python" with "python3" and for both platforms, make sure the output of python -v (or python3 -v) is 3.6 or greater.

**1. Clone this repository locally**
```
git clone https://github.com/zabrewer/meraki-apiv0-audit.git
```
**2. Create the virtual environment**
```
python3 -m venv AsyncRebootMeraki
```

**3. Change to the meraki-apiv0-audit directory**
```
cd AsyncRebootMeraki
```

**4. Activate the virtual environment**

For Windows
```
Scripts\activate.bat
```

For Mac
```
source bin/activate
```

**5. Satisfy dependencies by installing external packages**
```
pip install .
```

**6. Launch meraki-apiv0-audit while in virtual environment**
```
rebootmeraki.py
```