def right():
    pins.servo_set_pulse(AnalogPin.P8, 1700)
    pins.servo_set_pulse(AnalogPin.P13, 1700)
    control.wait_micros(20000)
    stop()
def sonarNEW():
    global distance
    distance = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    basic.show_number(distance)
def back():
    pins.servo_set_pulse(AnalogPin.P8, 1700)
    pins.servo_set_pulse(AnalogPin.P13, 1300)
    control.wait_micros(20000)
def sonar1():
    global distance
    pins.digital_write_pin(DigitalPin.P1, 0)
    control.wait_micros(3)
    pins.digital_write_pin(DigitalPin.P1, 1)
    control.wait_micros(20)
    pins.digital_write_pin(DigitalPin.P1, 0)
    distance = pins.pulse_in(DigitalPin.P2, PulseValue.HIGH) / 58
    basic.show_number(distance)
def left():
    pins.servo_set_pulse(AnalogPin.P8, 1300)
    pins.servo_set_pulse(AnalogPin.P13, 1300)
    control.wait_micros(20000)
def stop():
    pins.servo_set_pulse(AnalogPin.P8, 0)
    pins.servo_set_pulse(AnalogPin.P13, 0)
    control.wait_micros(20000)

def on_button_pressed_a():
    while True:
        sonar1()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    while True:
        sonarNEW()
input.on_button_pressed(Button.B, on_button_pressed_b)

def forward():
    pins.servo_set_pulse(AnalogPin.P8, 1300)
    pins.servo_set_pulse(AnalogPin.P13, 1700)
    control.wait_micros(20000)
distance = 0
basic.show_icon(IconNames.SCISSORS)
stop()