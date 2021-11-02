from kivy.uix.floatlayout import FloatLayout
from widgets import *


class FlashlightScreen(FloatLayout):
    
    def __init__(self, *, on_power, on_sos, on_pattern):
        super().__init__()
        power_button = PowerButton(on_state=on_power)
        self.add_widget(power_button)
        self.add_widget(ToggleModeSwitchLabel())
        self.add_widget(
            ToggleModeSwitch(on_state=power_button.switch_toggle_mode))
        self.add_widget(SOSSwitchLabel())
        self.add_widget(SOSSwitch(on_state=on_sos))