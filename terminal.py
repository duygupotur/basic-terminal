import gi
from gi.repository import Gtk, Vte
from gi.repository import GLib
gi.require_version("Gtk", "3.0")
import os

HOME = "HOME"
SHELLS = [ "/bin/bash" ]

terminal     = Vte.Terminal()
terminal.spawn_sync(
    Vte.PtyFlags.DEFAULT,
    os.environ[HOME],
    SHELLS,
    [],
    GLib.SpawnFlags.DO_NOT_REAP_CHILD,
    None,
    None,
    )

win = Gtk.Window()
win.connect('delete-event', Gtk.main_quit)
win.add(terminal)
win.show_all()

Gtk.main()