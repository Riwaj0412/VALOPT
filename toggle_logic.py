def toggle_specs(app_instance):
    if not app_instance.is_revealed:
        # Hide Optimize and move frame to top
        app_instance.opt_btn.pack_forget()
        app_instance.btn_frame.pack_forget()
        app_instance.btn_frame.pack(after=app_instance.title_label, pady=20)

        # Show Grid
        app_instance.grid_container.pack(expand=True, fill="both", padx=60)
        for key, node in app_instance.node_widgets.items():
            node.update_value(app_instance.stored_data.get(key, "N/A"))

        app_instance.reveal_btn.configure(
            text="[ HIDE SPECS ]", fg_color="#00ff7f", text_color="black")
        app_instance.is_revealed = True
    else:
        # Return to Hero view
        app_instance.grid_container.pack_forget()
        app_instance.btn_frame.pack_forget()
        app_instance.btn_frame.pack(expand=True)
        app_instance.opt_btn.pack(side="left", padx=20)

        app_instance.reveal_btn.configure(
            text="[ REVEAL SPECS ]", fg_color="#333333", text_color="white")
        app_instance.is_revealed = False
