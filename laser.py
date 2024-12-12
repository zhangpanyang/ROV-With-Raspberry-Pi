from serial import Serial
from time import sleep
#prepare laser distance sensor
serial = Serial('/dev/serial0', 115200, timeout=0.01) #set Baud rate to 115200
serial.write([0x5A,0x05,0x05,0x06,0x6A])  #set unit to mm
serial.write([0x5A,0x06,0x03,0x64,0x00,0x39])  #set frame rate to 100 Hz
serial.write([0x5A,0x09,0x3B,0x00,0x00,0x00,0x00,0x00,0x62])  #set IO mode to standard
sleep(0.1)
serial.reset_input_buffer()
 
def readLaserSensor():
    #skip old serial data
    FRAME_SIZE = 9
    while (serial.inWaiting() > FRAME_SIZE):
        serial.read()
 
    #read data
    data = serial.read(FRAME_SIZE)
     
    #parse data
    distance = float('nan')
    strength = float('nan')
    temperature = float('nan')
    if len(data) == FRAME_SIZE and data[0] == 0x59 and data[1] == 0x59:
        checksum = 0
        for i in range(0, FRAME_SIZE - 1):
            checksum = checksum + data[i]
        checksum = checksum & 0xFF
        if checksum == data[FRAME_SIZE - 1]:
            distance = data[2] | data[3] << 8  #[mm]
            strength = data[4] | data[5] << 8  #[0-65536]
            temperature = data[6] | data[7] << 8
             
            distance = distance/1000   # change length unit to [m]
            temperature = temperature/8 - 256  #[C]
     
    return distance, strength, temperature

# exitRequested = False 
# while not exitRequested: 
#     #read laser sensor 
#     laserDistance, laserStrength, laserTemp = readLaserSensor()
#     print(f'Distance: {laserDistance:.3f}m, strength: {laserStrength:.3f}, laser temperature: {laserTemp:.3f}C')
#     sleep(0.5)