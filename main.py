
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_height = "270.0px"
        container0.css_left = "30.0px"
        container0.css_position = "absolute"
        container0.css_top = "45.0px"
        container0.css_width = "405.0px"
        container0.variable_name = "container0"
        container1 = Container()
        container1.attr_class = "Container"
        container1.attr_editor_newclass = False
        container1.css_height = "250px"
        container1.css_left = "510.0px"
        container1.css_position = "absolute"
        container1.css_top = "300.0px"
        container1.css_width = "250px"
        container1.variable_name = "container1"
        container0.append(container1,'container1')
        container2 = Container()
        container2.attr_class = "Container"
        container2.attr_editor_newclass = False
        container2.css_height = "270.0px"
        container2.css_left = "510.0px"
        container2.css_position = "absolute"
        container2.css_top = "-15.0px"
        container2.css_visibility = "visible"
        container2.css_width = "270.0px"
        container2.variable_name = "container2"
        container0.append(container2,'container2')
        button0 = Button()
        button0.attr_class = "Button"
        button0.attr_editor_newclass = False
        button0.css_height = "30px"
        button0.css_left = "90.0px"
        button0.css_position = "absolute"
        button0.css_top = "180.0px"
        button0.css_width = "100px"
        button0.text = "Login"
        button0.variable_name = "button0"
        container0.append(button0,'button0')
        global label0
        label0 = Label()
        label0.attr_class = "Label"
        label0.attr_editor_newclass = False
        label0.css_height = "15.0px"
        label0.css_left = "90.0px"
        label0.css_position = "absolute"
        label0.css_top = "105.0px"
        label0.css_width = "30.0px"
        label0.text = "User:"
        label0.variable_name = "label0"
        container0.append(label0,'label0')
        global label1
        label1 = Label()
        label1.attr_class = "Label"
        label1.attr_editor_newclass = False
        label1.css_height = "15.0px"
        label1.css_left = "60.0px"
        label1.css_position = "absolute"
        label1.css_top = "135.0px"
        label1.css_width = "75.0px"
        label1.text = "Password:"
        label1.variable_name = "label1"
        container0.append(label1,'label1')
        global textinput0
        textinput0 = TextInput()
        textinput0.attr_class = "TextInput"
        textinput0.attr_editor_newclass = False
        textinput0.attr_maxlength = "200"
        textinput0.css_font_size = "15px"
        textinput0.css_font_style = "normal"
        textinput0.css_height = "20px"
        textinput0.css_left = "135px"
        textinput0.css_position = "absolute"
        textinput0.css_top = "105.0px"
        textinput0.css_width = "150px"
        textinput0.css_writing_mode = "none"
        textinput0.text = ""
        textinput0.variable_name = "textinput0"
        container0.append(textinput0,'textinput0')
        global textinput1
        textinput1 = TextInput()
        textinput1.attr_class = "TextInput"
        textinput1.attr_editor_newclass = False
        textinput1.attr_maxlength = "200"
        textinput1.css_font_size = "15px"
        textinput1.css_height = "20px"
        textinput1.css_left = "135.0px"
        textinput1.css_position = "absolute"
        textinput1.css_top = "135.0px"
        textinput1.css_width = "150.0px"
        textinput1.text = ""
        textinput1.variable_name = "textinput1"
        container0.append(textinput1,'textinput1')
        global label2
        label2 = Label()
        label2.attr_class = "Label"
        label2.attr_editor_newclass = False
        label2.css_font_size = "40px"
        label2.css_height = "45.0px"
        label2.css_left = "150.0px"
        label2.css_position = "absolute"
        label2.css_top = "30.0px"
        label2.css_width = "105.0px"
        label2.text = "Login"
        label2.variable_name = "label2"
        container0.append(label2,'label2')
        global button1
        button1 = Button()
        button1.attr_class = "Button"
        button1.attr_editor_newclass = False
        button1.css_height = "30px"
        button1.css_left = "225.0px"
        button1.css_position = "absolute"
        button1.css_top = "180.0px"
        button1.css_width = "100px"
        button1.text = "Sign Up"
        button1.variable_name = "button1"
        container0.append(button1,'button1')
        button0.onclick.do(self.onclick_button0)
        

        self.container0 = container0
        return self.container0
    
    def onclick_button0(self, emitter):
        Users = textinput0.text
        PassWord = textinput1.text
        print(Users,PassWord)

    def onclick_button1(self, emitter):
        pass



#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
