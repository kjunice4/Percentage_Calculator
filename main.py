# Percentage Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import numpy as np

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

#Compound_Interest
Builder.load_string("""
<Compound_Interest>
    id:Compound_Interest
    name:"Compound_Interest"

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
                text: "Compound Interest"
                
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "A = P(1 + r/n)^(n*t)"
            
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
                        loan.text = ""
                        interest.text = ""
                        time.text = ""
                        list_of_steps.clear_widgets()       
                                                    
            TextInput:
                id: loan
                text: loan.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                hint_text: "P = Principal:"
            
            TextInput:
                id: interest
                text: interest.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10         
                hint_text: "r = Interest rate:"
                
            TextInput:
                id: n
                text: n.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10         
                hint_text: "n = Times per year:"
                
            TextInput:
                id: time
                text: time.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10         
                hint_text: "t = Years:"
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5   
                    
                Button:
                    id: steps
                    text: "Calculate"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Compound_Interest.increase(loan.text + "&" + interest.text + "$" + time.text + "!" + n.text)    
                          
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

#Loan_Calculator
Builder.load_string("""
<Loan_Calculator>
    id:Loan_Calculator
    name:"Loan_Calculator"

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
                text: "Loan Calculator"
            
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
                        loan.text = ""
                        interest.text = ""
                        time.text = ""
                        list_of_steps.clear_widgets()       
                                                    
            TextInput:
                id: loan
                text: loan.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                hint_text: "Loan Amount:"
            
            TextInput:
                id: interest
                text: interest.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10         
                hint_text: "Yearly Interest rate:"
                
            TextInput:
                id: time
                text: time.text
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10         
                hint_text: "Years:"
                
            Button:
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Loan_Calculator.calculate(loan.text + "&" + interest.text + "$" + time.text)
    
                       
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
            sm.current = "Menu"
            
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
                
            
class Compound_Interest(Screen):
    """
            Button:
                text: "Compound Interest"   
                font_size: 75
                background_color: 0, 1 , 0 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Compound_Interest"
                    root.manager.transition.direction = "left" 
    """
    
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Compound_Interest, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "Menu"
            
    layouts = []
    def increase(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
           print()
           print("Compounding:", entry)
           
           amp = entry.find("&")
           dollar_sign = entry.find("$")
           exclamation = entry.find("!")
           
           loan = float(entry[:amp])
           print("loan =",loan)
           
           interest = float(entry[amp+1:dollar_sign])/100
           print("interest =",interest)
           
           time = entry[dollar_sign+1:exclamation]
           print("time =",time)
           
           times_per_year = entry[exclamation+1:]
           print("times_per_year =",times_per_year)
           
           self.ids.list_of_steps.add_widget(Label(text= "Compound Interest",font_size = 50, size_hint_y= None, height=100))
           
           i = 0
           while i < float(time):
               loan = float(loan)*(1+(float(interest)/float(times_per_year)))**float(float(times_per_year)*float(time))
               print("final_amount",loan)
               self.ids.list_of_steps.add_widget(Label(text= "Year " + str(i+1) + " : " + "${:,.2f}".format(float(loan)),font_size = 50, size_hint_y= None, height=100))
               i = i + 1
           
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)  
    """           
    def decrease(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
           print()
           print("DECREASING", entry)
           
           amp = entry.find("&")
           dollar_sign = entry.find("$")
           
           loan = float(entry[:amp])
           print("loan =",loan)
           
           interest = float(entry[amp+1:dollar_sign])/100
           print("interest =",interest)
           
           time = entry[dollar_sign+1:]
           print("time =",time)
           
           self.ids.list_of_steps.add_widget(Label(text= "Decreasing Compound Interest",font_size = 50, size_hint_y= None, height=100))
           
           i = 0
           while i < int(time):
               loan = str(float(loan) - float(float(loan) * float(interest)))
               print("loan of years" + str(i) + " =",loan)
               self.ids.list_of_steps.add_widget(Label(text= "Year " + str(i+1) + " = $" + "{:,.2f}".format(float(loan)),font_size = 60, size_hint_y= None, height=100))
               i = i + 1
           
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)  
        """
class Loan_Calculator(Screen):
    
    """
    Button:
        text: "Loan Calculator"   
        font_size: 75
        background_color: 1, 1 , 0 , 1
        size_hint_y: None
        height: 200
        padding: 10, 10
        on_release:
            app.root.current = "Loan_Calculator"
            root.manager.transition.direction = "left" 
    """
    
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Loan_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "Menu"
            
    layouts = []
    def calculate(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
           print()
           print("calculate", entry)
           
           amp = entry.find("&")
           dollar_sign = entry.find("$")
           
           loan = float(entry[:amp])
           print("loan =",loan)
           
           interest = float(entry[amp+1:dollar_sign])/100
           print("interest =",interest)
           
           time = entry[dollar_sign+1:]
           print("Years =",time)
           
           times_per_year = float(time) * 12
           print('times_per_year',times_per_year)
           
           #Loop Total Interest
           initial_interest_payment = str(float(loan)*float(interest)/12)
           print("initial_interest_payment",initial_interest_payment)
           
           #Principal = Interest / (rate of Interest * time period)
           principal = (float(interest) * 100) / ()
           print("principal",principal)
           
           
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
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
sm.add_widget(Compound_Interest(name="Compound_Interest"))
sm.add_widget(Loan_Calculator(name="Loan_Calculator"))
sm.current = "Homepage"   


class Percentage_Calculator(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Percentage_Calculator().run()
