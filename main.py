import customtkinter as ctk
import ux
from splash import SplashScreen
from dashboard import Dashboard
from manual_tweak import ManualTweakScreen
from in_game_settings import InGameSettingsScreen  # Import the new screen


class ValOptApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.title("VALOPT - VALORANT Optimizer")
        self.geometry("1100x700")
        self.configure(fg_color="#0f1923")

        # Prevent window from being resized to maintain UI layout
        self.resizable(False, False)

        # Start with the Splash Screen
        self.show_splash()

    def clear_screen(self):
        """Removes all widgets from the window to prepare for a new screen."""
        for widget in self.winfo_children():
            widget.destroy()

    def show_splash(self):
        self.clear_screen()
        self.splash = SplashScreen(self, on_finish=self.show_dashboard)

    def show_dashboard(self):
        self.clear_screen()
        self.dashboard = Dashboard(
            self, on_manual_tweak=self.show_manual_tweaks)
        self.dashboard.pack(fill="both", expand=True)

    def show_manual_tweaks(self):
        self.clear_screen()
        # Pass self as master_app and the dashboard return function as on_back
        self.manual_tweak = ManualTweakScreen(
            master_app=self,
            on_back=self.show_dashboard
        )
        self.manual_tweak.pack(fill="both", expand=True)

    def show_in_game_settings(self):
        """
        NEW: The function that was missing. 
        Switches the view to the Valorant Settings Editor.
        """
        self.clear_screen()
        self.settings_page = InGameSettingsScreen(
            master_app=self,
            on_back=self.show_manual_tweaks
        )
        self.settings_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    # Ensure UX fonts and themes are loaded
    ux.init_ux()

    app = ValOptApp()
    app.mainloop()
