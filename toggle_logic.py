def toggle_specs(dash):
    if not dash.is_revealed:
        # Hide the Optimize button specifically
        dash.opt_btn.pack_forget()

        # Move the frame to the top
        dash.btn_frame.pack_forget()
        dash.btn_frame.pack(after=dash.title_label, pady=20)

        # Show Grid
        dash.grid_container.pack(expand=True, fill="both", padx=60)

        # Fill Data
        data = dash.app.stored_data
        for key, node in dash.node_widgets.items():
            node.update_value(data.get(key, "N/A"))

        dash.reveal_btn.configure(
            text="[ HIDE SPECS ]", fg_color="#00ff7f", text_color="black")
        dash.is_revealed = True
    else:
        # Hide Grid
        dash.grid_container.pack_forget()

        # Reset Button Frame to center
        dash.btn_frame.pack_forget()
        dash.btn_frame.pack(expand=True)

        # Bring back the Optimize button next to Reveal
        dash.opt_btn.pack(side="left", padx=20)

        dash.reveal_btn.configure(
            text="[ REVEAL SPECS ]", fg_color="#333333", text_color="white")
        dash.is_revealed = False
