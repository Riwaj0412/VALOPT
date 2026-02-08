import customtkinter as ctk
import engine
import ux
import threading


class SplashScreen(ctk.CTkFrame):
    def __init__(self, master, callback):
        super().__init__(master, fg_color="#0f1923")
        self.callback = callback
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        ctk.CTkLabel(self, text="VALOPT // PRO", font=ux.get_font(50),
                     text_color="#ff4655").pack(pady=(250, 20))
        self.status_label = ctk.CTkLabel(
            self,
            text="INITIALIZING SCAN...",
            font=ux.get_font(14),
            text_color="white"
        )
        self.status_label.pack()

        self.progress = ctk.CTkProgressBar(
            self, width=400, progress_color="#ff4655")
        self.progress.set(0)
        self.progress.pack(pady=20)
        self.data = None
        threading.Thread(target=self.fetch_data, daemon=True).start()
        self.animate_progress(0)

    def fetch_data(self):
        self.data = engine.get_system_report()

    def animate_progress(self, val):
        if val <= 1.0:
            self.progress.set(val)
            new_val = val + 0.015
            self.after(20, lambda: self.animate_progress(new_val))
        else:
            self.check_completion()

    def check_completion(self):
        if self.data is not None:
            self.callback(self.data)
        else:
            self.after(100, self.check_completion)
