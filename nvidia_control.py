import tkinter.messagebox as msg


def launch():
    """Shows the manual instructions when clicked."""
    msg.showinfo(
        "Manual Step Required",
        "Windows is preventing the app from opening the panel directly.\n\n"
        "Please right-click your desktop and select 'NVIDIA Control Panel' manually."
    )
