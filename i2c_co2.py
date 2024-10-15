import smbus
import time

class EZO_CO2:
    def __init__(self, address=0x69):
        self.address = address
        self.bus = smbus.SMBus(1)  # Using python3-smbus, replace smbus2 with smbus 

    def read_data(self):
        try:
            self.bus.write_byte(self.address, ord('r'))  # Send 'r' to request a reading
            time.sleep(1)  # Wait for the sensor to respond
            response = self.bus.read_i2c_block_data(self.address, 0, 7)  # Read 7 bytes
            return ''.join([chr(b) for b in response]).strip()  # Convert to a string and return
        except Exception as e:
            return "Error: {}".format(e)

# Main program to get the reading
if __name__ == "__main__": 
    co2_sensor = EZO_CO2()  # Create an instance of the sensor
    reading = co2_sensor.read_data()  # Read data from the sensor
    print("CO2 Reading: {}".format(reading))  # Display the result
