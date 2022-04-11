A python based project to add easy-to-use usb-to-obdii-port diagnostics to the legacy Land Rover Testbook/RDS diagnostics software. Currently, no system publicly exists to provide this functionality. 

Background: Coming from the BMW ecosystem, I was surprised at the lack of open source or easily accessible dealer diagnostics that the Land Rover community had. With BMWs, there's thousands of different posts regarding how to set up INPA, DIS, ISTA, etc. 


Progress so far:

Testbook RDS 7 virtual machine created.
Testbook P38 RR, LR D1 & 2, Freelander data disc acquired, covers up to 2003 LR Disco2 (but not the 'drg0024v' data disc, which is the last version to be published and would make creating a packaged VM much easier to use.)

Initialization
When starting diagnostics, T4 device calls and asks for location of the external diagnostics device located at '192.168.1.3'. This is called once at first and subsequent attempts do not reinitialize. However, after a certain amount of time, initialization is done again.

##unsure##
After initialization
4 packets of data are sent out at set intervals with time inbetween. This could possibly be related to the "Principles of the test": 

    "To ensure correct data transfer, it is necessary to complete four tests:
    • The transmitting and receiving of data via K "line" as it leaves TestBook
    • The transmitting of data via L "line" as it leaves TestBook
    • The transmitting and receiving of data via K "line" as it leaves the extension cable (DTC0007A) connected to TestBook
    • The transmitting of data via L "line" as it leaves the extension cable (DTC0007A) connected to TestBook"

                      first call: x00  x00  x00  x06  x00  x06 
                      second call: x04  x00  x00  x06  x00  x0a
                      third call: x03  x00  x00  x06  x00  x09
                      fourth call: x05  x00  x00  x06  x00  x0b