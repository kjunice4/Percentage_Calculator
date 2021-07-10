# Percentage Calculator
"""
entry = input("Enter Number: ")
rate = input("% Rate: ")
inc_or_dec = input("Enter Increase or Decrease: ")
if inc_or_dec.lower() == 'increase':
    answer = float(entry) + (float(entry) * float(rate) / 100)
    print()
    print("Total: ",answer)
elif inc_or_dec.lower() == 'decrease':
    answer = float(entry) - (float(entry) * float(rate) / 100)
    print()
    print("Total: ",answer)
else:
    print("Invalid Entry")

"""

# Percentage Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Percentage_Calculator"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Percentage Calculator"
            on_release:
                app.root.current = "Percentage_Calculator"
                root.manager.transition.direction = "left" 

""")

#Percentage_Calculator
Builder.load_string("""
<Percentage_Calculator>
    id:Percentage_Calculator
    name:"Percentage_Calculator"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Percentage Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        number.text = ""
                        perc.text = ""
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        number.text = ""
                        perc.text = ""
                        list_of_steps.clear_widgets()       
        
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Number:"
                                                    
            TextInput:
                id: number
                text: number.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:8 - len(number.text)]           
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Percent:"
                                                
            TextInput:
                id: perc
                text: perc.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10              
                input_filter: lambda text, from_undo: text[:8 - len(perc.text)]           
            
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5   
                    
                Button:
                    id: steps
                    text: "Increase"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentage_Calculator.increase(number.text + "&" + perc.text)    
                          
                Button:
                    id: steps
                    text: "Decrease"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentage_Calculator.decrease(number.text + "&" + perc.text)
    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Percentage_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Percentage_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = sm.previous()    
    layouts = []
    def increase(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
           print("INC", entry)
           
           number = entry[:entry.find("&")]
           print("Number",number)
           perc = entry[entry.find("&")+1:]
           print("Perc",perc)
           
           amount = str(float(number) * float(perc) / 100)
           print("amount",amount)
           
           increase = str(float(number) + float(amount))
           print("increase",increase)
           
           self.ids.list_of_steps.add_widget(Label(text= perc + "% of " + number + " = " + amount,font_size = 60, size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= number + " + " + amount + " = " + increase,font_size = 60, size_hint_y= None, height=100))
           self.layouts.append(layout)
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
    def decrease(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
           print("DEC",entry)
           
           number = entry[:entry.find("&")]
           print("Number",number)
           perc = entry[entry.find("&")+1:]
           print("Perc",perc)
           
           amount = str(float(number) * float(perc) / 100)
           print("amount",amount)
           
           decrease = str(float(number) - float(amount))
           print("decrease",decrease)
           
           self.ids.list_of_steps.add_widget(Label(text= perc + "% of " + number + " = " + amount,font_size = 60, size_hint_y= None, height=100))
           self.ids.list_of_steps.add_widget(Label(text= number + " - " + amount + " = " + decrease,font_size = 60, size_hint_y= None, height=100))
           self.layouts.append(layout)
           
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)  
                
class Homepage(Screen):
    pass            

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Percentage_Calculator(name="Percentage_Calculator"))     
sm.current = "Homepage"   


class Percentage_Calculator(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Percentage_Calculator().run()