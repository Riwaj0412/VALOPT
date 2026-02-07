def toggle_specs(dashboard):
    """Toggles hardware grid and hides/shows the play button area."""
    if not dashboard.is_revealed:
        dashboard.play_container.pack_forget()
        dashboard.grid_container.pack(fill="x", padx=100, pady=20)
        dashboard.footer_frame.pack_forget()
        dashboard.footer_frame.pack(side="bottom", pady=60)
        dashboard.reveal_btn.configure(text="[ HIDE SPECS ]")
        dashboard.is_revealed = True
    else:
        dashboard.grid_container.pack_forget()
        dashboard.play_container.pack(pady=20)
        dashboard.reveal_btn.configure(text="[ REVEAL SPECS ]")
        dashboard.is_revealed = False
