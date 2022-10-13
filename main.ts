input.onButtonPressed(Button.A, function () {
    řádek()
})
input.onButtonPressed(Button.B, function () {
    prodleva += ZMĚNA
    music.playTone(prodleva, music.beat(BeatFraction.Double))
    if (prodleva == 500 || prodleva == 100) {
        ZMĚNA = ZMĚNA * -1
    }
    if (prodleva == 500) {
        led.plot(4, 4)
    } else {
        led.unplot(4, 4)
        if (prodleva > 300) {
            led.plot(3, 4)
        } else {
            led.unplot(3, 4)
            if (prodleva > 200) {
                led.plot(2, 4)
            } else {
                led.unplot(2, 4)
                if (prodleva > 100) {
                    led.plot(1, 4)
                } else {
                    led.unplot(1, 4)
                }
            }
        }
    }
})
function řádek () {
    for (let pořadí = 0; pořadí <= 4; pořadí++) {
        led.unplot(pořadí, 0)
    }
    basic.pause(100)
    for (let pořadí2 = 0; pořadí2 <= 4; pořadí2++) {
        led.plotBrightness(pořadí2, 0, jas)
        basic.pause(prodleva)
    }
}
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    jas += ZMENA_JAS
    if (jas == 250 || jas == 50) {
        ZMENA_JAS = ZMENA_JAS * -1
    }
    control.raiseEvent(
    EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_BUTTON_EVT_CLICK
    )
})
let ZMENA_JAS = 0
let jas = 0
let ZMĚNA = 0
let prodleva = 0
basic.showIcon(IconNames.StickFigure)
prodleva = 100
ZMĚNA = 100
jas = 50
ZMENA_JAS = 50
basic.pause(2000)
basic.clearScreen()
led.plot(0, 4)
