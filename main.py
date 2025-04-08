import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from YTSearch import *
from YTDownload import *
from YTPlaylistDL import *

class MyApp(App):
    def build(self):
        float_layout = FloatLayout()
        
        # Create a ScrollView to contain the BoxLayout
        scroll_view = ScrollView(size_hint=(1, None), size=(960, 2400), pos_hint={'top': 1})  # Adjust the height as needed
        self.box_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.box_layout.bind(minimum_height=self.box_layout.setter('height'))  # Allow the BoxLayout to grow
        
        # Create Labels
        self.label = Label(text="YTDownloader", font_size=90, size_hint_y=None, height=100)
        self.box_layout.add_widget(self.label)
        
        self.label2 = Label(text="Youtube Downloader", size_hint_y=None, height=100)
        self.box_layout.add_widget(self.label2)
        
        self.label3 = Label(text="", size_hint_y=None, height=20)
        self.box_layout.add_widget(self.label3)

        # Create a TextInput widget
        self.text_input = TextInput(hint_text="Voer zoektermen of playlist url in...", size_hint=(None, None), height=100, width=900, pos_hint={'center_x': 0.5}, padding=(20, 20))
        self.box_layout.add_widget(self.text_input)
        
        self.label4 = Label(text="", size_hint_y=None, height=30)
        self.box_layout.add_widget(self.label4)
        
        # Create a BoxLayout for the buttons with horizontal orientation
        button_layout = BoxLayout(orientation='horizontal', spacing=160, size_hint=(None, None), height=100, width=900, pos_hint={'center_x': 0.5})
        
        # Create a search Button widget
        button = Button(text="Zoek!", size_hint=(None, None), height=100, width=300)
        button.bind(on_press=self.on_DLbutton_press)
        button_layout.add_widget(button)
        
        # Create a playlist download Button widget
        buttonPL = Button(text="Download Playlist", size_hint=(None, None), height=100, width=440)
        buttonPL.bind(on_press=self.on_PLbutton_press)
        button_layout.add_widget(buttonPL)
        
        # Add the button layout to the main BoxLayout
        self.box_layout.add_widget(button_layout)
        
        self.label5 = Label(text="", size_hint_y=None, height=30)
        self.box_layout.add_widget(self.label5)

        self.labelOutput = Label(text="", size_hint_y=None, width=960, text_size=(960, None), valign='top')
        self.labelOutput.bind(texture_size=self.update_label_height)
        self.box_layout.add_widget(self.labelOutput)

        # Add the BoxLayout to the ScrollView
        scroll_view.add_widget(self.box_layout)
        float_layout.add_widget(scroll_view)

        return float_layout
                
                
    def on_DLbutton_press(self, instance):
        # Get the text from the TextInput
        input_text = self.text_input.text

        # Call the YTSearch function to get the lists
        listTitle, listDuration, listURL = YTSearch(input_text)

        # Clear previous buttons if any
        self.clear_previous_buttons()

        # Create a button for each title and add it to the BoxLayout
        for i, title in enumerate(listTitle):
            button = Button(text=f"{title}\n{listDuration[i]}", size_hint_y=None, height=150)
            button.bind(on_press=lambda btn, url=listURL[i]: self.on_button_click(url))  # Bind the button to the click event
            self.box_layout.add_widget(button)

    def clear_previous_buttons(self):
        # Remove all buttons that were previously added
        for child in self.box_layout.children[:]:
            if isinstance(child, Button) and child not in [self.label, self.label2, self.label3, self.label4, self.label5, self.labelOutput]:
                self.box_layout.remove_widget(child)

    def on_button_click(self, url):
        # Handle the button click event, e.g., start downloading the video
        YTDownload(url)

    def update_label_height(self, instance, value):
        instance.height = instance.texture_size[1]
        
    def on_PLbutton_press(self, instance):
        # Get the text from the TextInput
        input_text = self.text_input.text
        YTPlaylistDL(input_text)


if __name__ == "__main__":
    MyApp().run()
