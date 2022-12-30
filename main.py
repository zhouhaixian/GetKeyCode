import PySimpleGUI
from pynput import keyboard

layout = [
    [PySimpleGUI.Text('按下任意键查看键码')],
    [PySimpleGUI.Input(enable_events=True, key='Input', readonly=True)]
]

window = PySimpleGUI.Window('GetKeyCode', layout, finalize=True)
input_el = window['Input']
input_el.bind('<FocusIn>', '<FocusIn>')
input_el.bind('<FocusOut>', '<FocusOut>')


def on_press(key):
    try:
        input_el.update(key.vk)
    except AttributeError:
        input_el.update(key.value.vk)


listener = keyboard.Listener(on_press=on_press)


if __name__ == '__main__':
    while True:
        event, values = window.read()

        match event:
            case PySimpleGUI.WINDOW_CLOSED:
                break
            case 'Input<FocusIn>':
                listener.start()
            case 'Input<FocusOut>':
                listener.stop()
                listener = keyboard.Listener(on_press=on_press)

    window.close()
