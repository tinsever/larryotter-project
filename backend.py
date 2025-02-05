from flask import Flask
import serial
import time

app = Flask(__name__)

# Seriellen Port für die Kommunikation mit dem Arduino definieren
ser = serial.Serial('COM3', 9600, timeout=1)  # COM3 anpassen, je nach Port des Arduino

def wink(times):
    # Den Arduino über die serielle Schnittstelle anweisen, das Winken auszuführen
    ser.write(f"wink {times}\n".encode())

@app.route('/start', methods=['GET'])
def start():
    # Die Funktion "wink" aufrufen, um den Servo 5 Mal winken zu lassen
    wink(5)
    return "Das Winken wurde gestartet!", 200

if __name__ == '__main__':
    app.run(host='localhost', port=8123)
