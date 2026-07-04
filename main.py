import serial
import vgamepad as vg
import time

def map_range(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def main():
    try:
        gamepad = vg.VX360Gamepad()
        print("Virtual Xbox 360 Controller active.")
    except Exception as e:
        print(f"Failed to start vgamepad. Error: {e}")
        import traceback
        traceback.print_exc()
        return
    
    try:
        ser = serial.Serial('COM5', 115200)
        print("Connected to Arduino on COM5.")
    except Exception as e:
        print(f"Could not connect to Arduino. Error: {e}")
        return
    
    print("Listening for data...")

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode().strip()

                try:
                    x, y, btn = map(int, line.split(","))

                    x_xbox = map_range(y, 0, 1023, 32767, -32768)
                    y_xbox = map_range(x, 0, 1023, 32767, -32768)

                    # print('x: ' + str(x_xbox) + ' y: ' + str(y_xbox) + ' btn: ' + str(btn))

                    gamepad.left_joystick(x_value=x_xbox, y_value=y_xbox)
                    # gamepad.right_joystick(x_value=x_xbox, y_value=y_xbox)

                    if btn == 0:
                        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                    else:
                        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                    
                    gamepad.update()
                except ValueError:
                    pass
            else:
                time.sleep(0.008) # sleep briefly if no data (saves cpu)

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    main()
