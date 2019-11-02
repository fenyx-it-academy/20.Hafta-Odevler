from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""
<button>:
    color:.8,.2,12,7
    font_size:40
    size_hint:.3,.1
FloatLayout:
    Button:
        text:"Log In"
        pos_hint:{'x':.2,'top':.4}
    Button:
        text:'Quit'
        pos_hint:{'x':.2,'y':.4}    
"""))