from gi.repository import Gtk, Gdk
import RPi.GPIO as GPIO
import puzzle1, gi, threading
GPIO.setwarnings(False)

class MyWindow(Gtk.Window):
    def __init__(self):
        
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path("/home/pi/Desktop/puzzle 2/propiedades.css")
        styleContext = Gtk.StyleContext()
        styleContext.add_provider(cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        screen = Gdk.Screen.get_default()
        styleContext.add_provider_for_screen(screen, cssProvider,Gtk.STYLE_PROVIDER_PRIORITY_USER)
        
        super().__init__(title="Let's read your card")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(10)
        
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.box.set_name("box1")
        self.add(self.box)
        self.evbox = Gtk.EventBox()
        
        self.label = Gtk.Label('Please, login with your university card')
        self.label.set_use_markup(True)
        self.label.set_size_request(500,100)
        
        self.evbox.add(self.label)

        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clicked)
        
        self.box.pack_start(self.evbox, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)
        
        thread = threading.Thread(target=self.read_uid)
        thread.setDaemon(True)
        thread.start()
        
    def clicked(self, widget):
        self.box.set_name("box")
        self.label.set_label("Please, login with your university card")
        thread = threading.Thread(target=self.read_uid)
        thread.start()
        
    def read_uid(self):
        uid = puzzle1.Rfid_rc522().read_uid()
        self.box.set_name("box2")
        self.label.set_label('UID: '+uid)
        
if __name__ == "__main__":
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
