import webbrowser

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from filesharer import FileShare

Builder.load_file('frontend_webcam.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        self.filepath = 'images/' + time.strftime('%Y%m%d-%H%M%S') + '.png'
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_error_msg = "Create a link first loserrr ;)"
    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileShare(file_path)
        self.link = fileshare.url()
        self.ids.link.text = self.link

    def copy_link(self):
        try:
            Clipboard.copy(self.link)
        except:
            self.ids.link.text = self.link_error_msg

    def open_link(self):
        try:
            webbrowser.open(self.link)
        except:
            self.ids.link.text = self.link_error_msg



class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()