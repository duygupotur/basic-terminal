import gi
from gi.repository import Gtk, Vte
from gi.repository import GLib
gi.require_version("Gtk", "3.0")
import os

HOME = "HOME"
SHELLS = [ "/bin/bash" ]

class Terminal01(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Terminalim")
        self.set_border_width(10)

        self.terminal     = Vte.Terminal()
        self.terminal.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ[HOME],
            SHELLS,
            [],
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )

        self.command = "echo \"Komut Örneği.\"\n\n"

        self.buttons = list()
        for prog_language in ["Komut Gönder", "Yol Bul", "None"]:
            button = Gtk.Button(prog_language)
            self.buttons.append(button)
            if prog_language=="Komut Gönder":
                button.connect("clicked", self.InputToTerm)
            elif prog_language=="Yol Bul":
                button.connect("clicked", self.gettoPath)
            else:
                button.connect("clicked", self.gettoPath)

        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        self.label = Gtk.Label()
        self.label.set_text("Boş yer")
        self.label.set_justify(Gtk.Justification.LEFT)

        self.grid.attach(self.label, 0, 0, 3, 10)
        self.grid.attach_next_to(
            self.terminal, self.label, Gtk.PositionType.RIGHT, 7, 10
        )
        self.grid.attach_next_to(
            self.buttons[0], self.label, Gtk.PositionType.BOTTOM, 1, 1
        )
        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(
                button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1
            )
        self.show_all()

    def InputToTerm(self, clicker):
        length = len(self.command)
        ### gtk
        ### TypeError: Vte.Terminal.feed_child() takes exactly 2 arguments (3 given)
        # self.terminal.feed_child_binary(self.command.encode("utf-8"))
        ## xfce
        self.terminal.feed_child_binary(self.command, length)

    def gettoPath(self, clicker):
        test=self.terminal.get_window_title()
        test=test.split(":")
        self.label.set_text(test[1])


win = Terminal01()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
