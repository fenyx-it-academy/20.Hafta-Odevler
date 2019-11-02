from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string("""
<button>:
    
    font_size:40
    size_hint:.3,.1
FloatLayout:
    Label:
        text: "user"
        size_hint:.3,.1
        pos_hint:{'x':.2,'y':.5}
    Label:
        text: "password"
        size_hint:.3,.1
        pos_hint:{'x':.2,'y':.4}
             
    TextInput:
        color:18,7
        size_hint:.3,.1
        pos_hint:{'x':.4,'y':.5} 
        
    TextInput:
        color:12,7
        size_hint:.3,.1
        pos_hint:{'x':.4,'y':.4}
          
    Button:
        text:"Log In"
        color:.0,.2,12,7
        pos_hint:{'x':.4,'y':.3}
    
"""))