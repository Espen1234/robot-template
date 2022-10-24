function back () {
    pins.servoSetPulse(AnalogPin.P8, 1300)
    pins.servoSetPulse(AnalogPin.P13, 1700)
    control.waitMicros(20000)
}
input.onButtonPressed(Button.A, function () {
    forward()
})
function doSomething () {
	
}
input.onButtonPressed(Button.B, function () {
    back()
})
function forward () {
    pins.servoSetPulse(AnalogPin.P8, 1700)
    pins.servoSetPulse(AnalogPin.P13, 1300)
    control.waitMicros(20000)
}
function call_right () {
    pins.digitalWritePin(DigitalPin.P0, 0)
}
function sensor () {
    pins.digitalWritePin(DigitalPin.P1, 0)
    control.waitMicros(2)
    pins.digitalWritePin(DigitalPin.P1, 1)
    control.waitMicros(4)
    pins.digitalWritePin(DigitalPin.P1, 0)
    distance = pins.pulseIn(DigitalPin.P2, PulseValue.High) / 58
}
let count = 0
let distance = 0
basic.showIcon(IconNames.Heart)
distance = 0
basic.forever(function () {
    count = 0
    for (let index = 0; index < 4; index++) {
        sensor()
        if (distance < 7) {
            count += 1
            sensor()
        }
    }
    if (count == 4) {
        call_right()
        basic.pause(2000)
        forward()
    } else {
        forward()
    }
})
