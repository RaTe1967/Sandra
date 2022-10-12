input.onButtonPressed(Button.A, function () {
    for (let pořadí = 0; pořadí <= 4; pořadí++) {
        led.unplot(pořadí, 0)
    }
    basic.pause(100)
    for (let pořadí = 0; pořadí <= 4; pořadí++) {
        led.plot(pořadí, 0)
        basic.pause(prodleva)
    }
})
input.onButtonPressed(Button.B, function () {
    prodleva += ZMĚNA
    if (prodleva == 500 || prodleva == 100) {
        ZMĚNA = ZMĚNA * -1
    }
})
let ZMĚNA = 0
let prodleva = 0
basic.showIcon(IconNames.StickFigure)
prodleva = 100
ZMĚNA = 100
basic.pause(2000)
basic.clearScreen()
led.plot(0, 4)
