from time import sleep
import smbus # System Management Bus (SMBus), a two-wire interface based on I2C for system component chips

bus = smbus.SMBus(1) 
def readPressureSensor():
    #read data
    PRESSURE_SENSOR_ADDR = 0x28
    data = bus.read_i2c_block_data(PRESSURE_SENSOR_ADDR, 0x00, 4)
    status = (data[0] & 0xC0) >> 6
    pressCounts = data[1] | ((data[0] & 0x3F) << 8)
    tempCounts = ((data[3] & 0xE0) >> 5) | (data[2] << 3)
     
    #pressure conversion
    P_MAX = 2  #[bar]
    P_MIN = 0  #[bar]
    O_MAX = 0.9 * pow(2,14)
    O_MIN = 0.1 * pow(2,14)
    pressure = (pressCounts - O_MIN) * (P_MAX - P_MIN) / (O_MAX - O_MIN) + P_MIN  #[bar]
     
    #temperature conversion
    T_MAX = 150  #[Celsius]
    T_MIN = -50  #[Celsius]
    T_COUNTS = pow(2,11) - 1
    temperature = tempCounts * (T_MAX - T_MIN) / T_COUNTS + T_MIN  #[Celsius]
     
    return pressure, temperature
# exitRequested = False 
# while not exitRequested: 
#     #read pressure sensor 
#     pressure, pressTemp = readPressureSensor()
#     print(f'Pressure: {pressure*10000 :.1f}, pressure temperature: {pressTemp :.1f}C')
#     sleep(0.2)