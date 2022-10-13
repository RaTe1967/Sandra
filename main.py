def on_button_pressed_a():
    řádek()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global prodleva, ZMĚNA
    prodleva += ZMĚNA
    music.play_tone(prodleva, music.beat(BeatFraction.DOUBLE))
    if prodleva == 500 or prodleva == 100:
        ZMĚNA = ZMĚNA * -1
    if prodleva == 500:
        led.plot(4, 4)
    else:
        led.unplot(4, 4)
        if prodleva > 300:
            led.plot(3, 4)
        else:
            led.unplot(3, 4)
            if prodleva > 200:
                led.plot(2, 4)
            else:
                led.unplot(2, 4)
                if prodleva > 100:
                    led.plot(1, 4)
                else:
                    led.unplot(1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def řádek():
    for pořadí in range(5):
        led.unplot(pořadí, 0)
    basic.pause(100)
    for pořadí2 in range(5):
        led.plot_brightness(pořadí2, 0, jas)
        basic.pause(prodleva)

def on_logo_pressed():
    global jas, ZMENA_JAS
    jas += ZMENA_JAS
    if jas == 250 or jas == 50:
        ZMENA_JAS = ZMENA_JAS * -1
    control.raise_event(EventBusSource.MICROBIT_ID_BUTTON_A,
        EventBusValue.MICROBIT_BUTTON_EVT_CLICK)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

ZMENA_JAS = 0
jas = 0
ZMĚNA = 0
prodleva = 0
basic.show_icon(IconNames.STICK_FIGURE)
prodleva = 100
ZMĚNA = 100
jas = 50
ZMENA_JAS = 50
basic.pause(2000)
basic.clear_screen()
led.plot(0, 4)