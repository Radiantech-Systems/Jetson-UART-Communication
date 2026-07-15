import serial

ser = serial.Serial('/dev/ttyTHS1', 115200, timeout=1)

print("Listening...")

while True:
    if ser.in_waiting:
        data = ser.readline().decode('utf-8', errors='ignore').strip()

        if data:
            print("STM32:", data)

            ser.write(b"Hello from Jetson\r\n")
            print("Sent: Hello from Jetson")
