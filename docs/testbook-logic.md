## Initialization
When starting diagnostics, T4 device calls and asks for location of the external diagnostics device located at '192.168.1.3'. This is called once at first and subsequent attempts do not reinitialize. However, after a certain amount of time, initialization is done again.

## Cable Checks

Communication from Testbook software when requesting blue cable
- first call: 00 00 00 06 00 06 
- second call: 04 00 00 06 00 0a
- third call: 03 00 00 06 00 09
- fourth call: 05 00 00 06 00 0b