from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''

<Button>:
    color: 1,1,1,1
    front_size: 20
    size_hint: .3,.08
    
FloatLayout:
    Button:
        text:'Log in'
        pos_hint: { 'x':.1, 'y':.54}
        
    Button:
        text:'Quit'
        pos_hint: { 'x':.1, 'y':.45}
        
        
'''))