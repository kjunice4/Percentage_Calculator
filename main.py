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
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-math,LLC © : Percentage Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
                
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
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
                text: "Menu"
            
            Button:
                text: "Percentage Calculator"   
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Percentage_Calculator"
                    root.manager.transition.direction = "left"
            
            Button:
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 1 , 1
                height: 200
                text: "Percentage Converter"
                on_release:
                    app.root.current = "Percentages_converter"
                    root.manager.transition.direction = "left"         
            
            Button:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-math,LLC ©"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')
            
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-math,LLC ©"
                    
            Image:
                source: 'KSquared_QR_code.png'
                size_hint_y: None
                height: 1000
                width: 1000
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
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
                font_size: 60
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-math?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Percentage Calculator v0.1"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
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
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
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
                                                    
            TextInput:
                id: number
                text: number.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                hint_text: "Number:"
                input_filter: lambda text, from_undo: text[:8 - len(number.text)]           
            
            TextInput:
                id: perc
                text: perc.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10         
                hint_text: "Percent:"
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

Builder.load_string("""
<Percentages_converter>
    id: Percentages_converter
    name:"Percentages_converter"
    
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
                text: "Percentages Converter"   
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        input.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: input
                    text: input.text
                    hint_text: "Percentage:"
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:4 - len(input.text)] 
                    
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: 75
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Fraction"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentages_converter.convert_perc_to_frac(input.text)
                        
                Button:
                    id: steps
                    text: "Decimal"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Percentages_converter.convert_perc_to_dec(input.text)
                    
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
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True

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

class Percentages_converter(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Percentages_converter, self).__init__(**kwargs)
    
    layouts = []
    def convert_perc_to_frac(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            # 2, 4, 5, 10, 25, 50
            if len(entry) > 2:
                numerator = entry[-2:]
                whole = entry[:-2]
                print("whole",whole)
                print("numerator",numerator)
                denomenator = 100
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 50
                        denomenator = int(denomenator) / 50
                        print("numerator 50 ",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % 50 != 0 or denomenator % 50 != 0:
                            break
                
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break

                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if str(numerator) == "00":
                    numerator = "1" + str(numerator)
                    
                if str(numerator)[0] == "0":
                    numerator = str(numerator)[1]    
                    
                if int(numerator) != int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(entry) + "% to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(str(denomenator)) + "  ", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                    self.layouts.append(layout)     
                
                if int(numerator) == int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= entry + "% to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(entry).replace(".0","") , font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "-----", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                    self.layouts.append(layout)   
                
            if len(entry) <= 2:
                numerator = entry
                print("numerator",numerator)
                denomenator = 100
                if int(numerator) % 50 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 50
                        denomenator = int(denomenator) / 50
                        print("numerator 50 ",numerator)
                        print("denomenator 50 ",denomenator)
                        if numerator % 50 != 0 or denomenator % 50 != 0:
                            break
                    
                if int(numerator) % 25 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 25
                        denomenator = int(denomenator) / 25
                        print("numerator 25 ",numerator)
                        print("denomenator 25 ",denomenator)
                        if numerator % 25 != 0 or denomenator % 25 != 0:
                            break
                
                if int(numerator) % 10 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 10
                        denomenator = int(denomenator) / 10
                        print("numerator 10 ",numerator)
                        print("denomenator 10 ",denomenator)
                        if numerator % 10 != 0 or denomenator % 10 != 0:
                            break
                
                if int(numerator) % 5 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 5
                        denomenator = int(denomenator) / 5
                        print("numerator 5 ",numerator)
                        print("denomenator 5 ",denomenator)
                        if numerator % 5 != 0 or denomenator % 5 != 0:
                            break
                            
                if int(numerator) % 2 == 0:
                    while int(numerator) > 1:
                        numerator = int(numerator) / 2
                        denomenator = int(denomenator) / 2
                        print("numerator 2 ",numerator)
                        print("denomenator 2 ",denomenator)
                        if numerator % 2 != 0 or denomenator % 2 != 0:
                            break
                        
                if str(numerator)[0] == "0":
                    numerator = str(numerator)[1]
                    
                if int(numerator) != int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(entry) + "% to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "----", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                    self.layouts.append(layout)     
                    
                if int(numerator) == int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= entry + "% to Fraction = ", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(entry).replace(".0","") , font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "-----", font_size = 75, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = 75, size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_perc_to_dec(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            dec = entry + "/100"
            evaled = str(eval(dec))
            print("evaled",evaled)
            self.ids.list_of_steps.add_widget(Label(text= entry + "% to Decimal = ", font_size = 75, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= evaled, font_size = 75, size_hint_y= None, height=100))
            self.layouts.append(layout)
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = 75, size_hint_y= None, height=100))   
            self.layouts.append(layout)

class Homepage(Screen):
    pass            

class Menu(Screen):
    pass            

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(updates(name="updates"))    
sm.add_widget(Percentage_Calculator(name="Percentage_Calculator"))   
sm.add_widget(Percentages_converter(name="Percentages_converter"))   
sm.current = "Homepage"   


class Percentage_Calculator(App):
    def __init__(self, **kwargs):
        super(Percentage_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
        
    def build(app):
        return sm

if __name__ == '__main__':
    Percentage_Calculator().run()
