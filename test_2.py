import customtkinter as ctk

# Sample data for search
data_list = ["Apple", "Banana", "Cherry", "Dragonfruit", "Grapes", "Mango", "Orange", "Peach", "Pear", "Strawberry"]

# Function to update list based on search
def update_list(search_text):
    search_text = search_text.lower()
    filtered_items = [item for item in data_list if search_text in item.lower()]
    
    # Clear previous items
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Display filtered items
    for item in filtered_items:
        lbl = ctk.CTkLabel(frame, text=item, fg_color="transparent", anchor="w", padx=10)
        lbl.pack(fill="x", pady=2)

# GUI setup
ctk.set_appearance_mode("dark")  # Options: "System" (default), "Dark", "Light"
app = ctk.CTk()
app.geometry("400x500")
app.title("Search Bar Example")

# Search bar
search_entry = ctk.CTkEntry(app, placeholder_text="Search...", width=300)
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", lambda e: update_list(search_entry.get()))

# Frame to show search results
frame = ctk.CTkFrame(app, width=300, height=300)
frame.pack(pady=10, fill="both", expand=True)

# Initialize list
update_list("")

app.mainloop()
