from kivy.app import App
from screens import FlashlightScreen
from controllers import PatternController
from kivy.utils import platform
if platform == 'android':
    from plyer import flash
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA])
else:
    flash = None


class FlashlightApp(App):
    
    try:
        flash_states = (flash.off, flash.on)
    except:
        flash_states = ('OFF', 'ON')
    
    def build(self):
        self.pattern_controller = PatternController(self, flash)
        return FlashlightScreen(on_power=self.on_power,
                                on_sos=self.on_sos,
                                on_pattern=self.on_pattern)
    
    def on_power(self, _, state):
        try:
            self.flash_states[state]()
        except:
            print(self.flash_states[state])
        
    def on_sos(self, _, state):
        if state:
            self.pattern_controller('sos', loop=True)
        else:
            self.pattern_controller.stop()
        
    def on_pattern(self, *args):
        pass
        
    def on_stop(self):
        flash.release()

if __name__ == '__main__':
    FlashlightApp().run()