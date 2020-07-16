# STM32 I2C 5V Tolerent

## I2C STM32 Open Drain Pullup Issue #5102

Description
Type: Bug
Related issue: I2C 5V tolerant I/O could be damaged
Priority: Major
Bug
Target
STM32 (Multitech mDot)

Toolchain:
mBed

Expected behavior
I2C bus are usually 5V tolerant on all STM32 processor. If an external device on the I2C bus requires 5V operation, we usually acheive it by using 5V external pull-ups on the bus. Since signaling uses open-drain output on I2C for both signal SCL and SDA any 5V tolerant MCU will work on a 5V I2C bus

Actual behavior
Currently the I2C initialization setup the SDA/SCL pin in pin_mode(sda/scl, OpenDrainPullup) which cause the internal pull-up to be activated by default on OpenDrain output.
Having pull-up activated on a 5V externally pull bus, cause the pin to clamp on the STM32 die diode and could damage the IC (There is a note in STM32 datasheet specifying this issue).
It is understood by all the community that I2C bus should always be externally pulled by physical resistor. I2C initialization should then be ALWAYS OpenDrainNoPull by default.

If a feature of a I2C open drain pull-up by the MCU is required, then a new method should be added in the I2C class to add the mode option for OpenDrainNoPull (default) and OpenDrainPullup.

Steps to reproduce
Use external pull-up of 4K7 to 5V on each SCL/SDA pin. Initialize the I2C instance.
Voltage on both pins should be between 3.7-3.9V instead of 5V.
Toggle SCL/SDA pin back in DigitalIn with no Pullup, signal will go back to 5V.
