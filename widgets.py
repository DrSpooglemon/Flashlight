from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.lang.builder import Builder

Builder.load_string('''
<ToggleModeSwitchLabel>
    text:
        'Toggle mode'
    size_hint:
        .2, .05
    pos_hint:
        {'right': .95, 'top': .95}

<ToggleModeSwitch>
    size_hint:
        .2, .05 
    pos_hint:
        {'right': .95, 'top': .9}
        
<SOSSwitchLabel>
    text:
        'SOS'
    size_hint:
        .2, .05
    pos_hint:
        {'x': .05, 'top': .95} 
        
<SOSSwitch>
    size_hint:
        .2, .05 
    pos_hint:
        {'x': .05, 'top': .9}

<PowerButton>
    size_hint:
        .35, .2
    pos_hint:
        {'center_x': .5, 'center_y': .5}                   
''')


class ToggleModeSwitchLabel(Label):
    pass


class ToggleModeSwitch(Switch):
    
    def __init__(self, on_state):
        super().__init__(active=True)
        self.bind(active=on_state)
        
        
class SOSSwitchLabel(Label):
    pass


class SOSSwitch(Switch):
    
    def __init__(self, on_state):
        super().__init__(active=False)
        self.bind(active=on_state)
    
    
class PowerButton(Button):
    
    power = BooleanProperty(False)
    toggled = BooleanProperty(False)
    toggle_mode = BooleanProperty(True)
    
    def __init__(self, on_state):
        super().__init__(text='OFF')
        self.bind(power=on_state)
        self.bind(power=self.on_power)
        self.bind(toggled=self.on_toggle)
        
    def _do_press(self):
        self.power = True
        self.state = 'down'
        
    def _do_release(self, *_):
        if self.toggle_mode:
            self.toggled = not self.toggled
        else:
            self.power = False
        self.state = 'normal'
        
    def on_toggle(self, _, toggled):
        self.power = toggled
        
    def on_power(self, _, power):
        if power:
            self.text = 'ON'
        else:
            self.text = 'OFF'
        
    def switch_toggle_mode(self, _, state):
        self.toggle_mode = state
        self.toggled = False
        self.power = False
        
        
        
        
        