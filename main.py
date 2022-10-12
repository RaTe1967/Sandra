def on_button_pressed_a():
    for pořadí in range(5):
        led.unplot(pořadí, 0)
    basic.pause(100)
    for pořadí2 in range(5):
        led.plot(pořadí2, 0)
        basic.pause(prodleva)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global prodleva, ZMĚNA
    prodleva += ZMĚNA
    if prodleva == 500 or prodleva == 100:
        ZMĚNA = ZMĚNA * -1
input.on_button_pressed(Button.B, on_button_pressed_b)

ZMĚNA = 0
prodleva = 0
basic.show_icon(IconNames.STICK_FIGURE)
prodleva = 100
ZMĚNA = 100
basic.pause(2000)
basic.clear_screen()
led.plot(0, 4)