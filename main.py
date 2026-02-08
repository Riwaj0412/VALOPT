import customtkinter as ctk
from splash import SplashScreen
from detected import DetectedScreen
from dashboard import DashboardHUD
from optimize_screen import OptimizeScreen
from manual_tweak import ManualTweakScreen
import ux
<<<<<<< HEAD
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
=======
>>>>>>> 6bee7d2e0e5050d7d93d54d73ece281eb74c38d8


class ValOptApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("VALOPT")
        ux.center_window(self, 1000, 950)
        self.resizable(False, False)
        self.show_splash()

    def show_splash(self):
        SplashScreen(self, self.show_detected)

    def show_detected(self, data=None):
        for child in self.winfo_children():
            child.destroy()
        DetectedScreen(self, self.show_dashboard)

    def show_dashboard(self):
        for child in self.winfo_children():
            child.destroy()
        DashboardHUD(self)

    def show_optimize(self):
        for child in self.winfo_children():
            child.destroy()
        OptimizeScreen(self, self.show_dashboard)


if __name__ == "__main__":
    app = ValOptApp()
    app.mainloop()
