# Testbook Interface Emulator
A python based project to add easy-to-use usb-to-obdii-port diagnostics to the legacy Land Rover Testbook/RDS diagnostics software. Currently, no system publicly exists to provide this functionality. 

## Background
 Coming from the BMW ecosystem, I was surprised at the lack of open source or easily accessible dealer diagnostics that the Land Rover community had. With BMWs, there's thousands of different posts regarding how to set up INPA, DIS, ISTA, etc.

## Status
- Testbook RDS 7 virtual machine created with mult
- Multiple Testbook data discs acquired covering Land Rovers and Rovers
- Received a Wireshark dump from a project contributor (name withheld before permission) showing Testbook initialization, commununication with 5AS Ecu, and several programs with the 5AS ecu.
- **successfuly emulated a Rover 5AS security ecu** 