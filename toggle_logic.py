def toggle_specs(dash):
    if not dash.is_revealed:
        dash.opt_btn.pack_forget()
        dash.btn_frame.pack_forget()
        dash.btn_frame.pack(after=dash.title_label, pady=20)

        dash.grid_container.pack(expand=True, fill="both", padx=60)

        # Pull data stored in the main app
        data = dash.app.stored_data
        for key, node in dash.node_widgets.items():
            node.update_value(data.get(key, "N/A"))

        dash.reveal_btn.configure(
            text="[ HIDE SPECS ]", fg_color="#00ff7f", text_color="black")
        dash.is_revealed = True
    else:
        dash.grid_container.pack_forget()
        dash.btn_frame.pack_forget()
        dash.btn_frame.pack(expand=True)
        dash.opt_btn.pack(side="left", padx=20)

        dash.reveal_btn.configure(
            text="[ REVEAL SPECS ]", fg_color="#333333", text_color="white")
        dash.is_revealed = False
