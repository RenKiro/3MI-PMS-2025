# import sqlite3

# def create_connection():
#     conn = sqlite3.connect('MAIN UI/payroll.db')
#     return conn

# def create_tables():
#     conn = create_connection()
#     curr = conn.cursor()

#     curr.execute("""
#         CREATE TABLE IF NOT EXISTS employees (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 position TEXT NOT NULL,
#                 salary REAL NOT NULL
#             );
#         """)
    
#     curr.execute("""
#         CREATE TABLE IF NOT EXISTS attendance (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 employee_id INTEGER,
#                 date TEXT,
#                 check_in TEXT,
#                 check_out TEXT,
#                 FOREIGN KEY (employee_id) REFERENCES employees (id)
#             );
#         """)
    
#     curr.execute("""
#         CREATE TABLE IF NOT EXISTS payroll (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 employee_id INTEGER,
#                 gross_pay REAL,
#                 deductions REAL,
#                 net_pay REAL,
#                 FOREIGN KEY (employee_id) REFERENCES employees (id)
#             );
#         """)
    
#     print('DATABASE CREATED!')
#     conn.commit()
#     conn.close()


# if __name__ == '__main__':
#     create_tables()



# import sqlite3

# # Create or connect to the database
# conn = sqlite3.connect("MAIN UI/employees.db")
# cursor = conn.cursor()

# # Create table (if not exists)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS employees (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     job_type TEXT,
#     position TEXT,
#     salary REAL,
#     profile BLOB
# )
# """)

# conn.commit()
# conn.close()

# print('Database Successfully Created!')

# import sqlite3

# def insert_employee(name, job_type, position, salary, profile_path):
#     with open(profile_path, "rb") as file:
#         profile_image = file.read()  # Read image as binary data

#     conn = sqlite3.connect("MAIN UI/employees.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO employees (name, job_type, position, salary, profile) VALUES (?, ?, ?, ?, ?)",
#                    (name, job_type, position, salary, profile_image))
#     conn.commit()
#     conn.close()

# profile_path = "C:/Users/mrenz/OneDrive/Documents/Python Repo/Python Space/My Projects/Payroll Management System/MAIN UI/assets/Profile.png"

# insert_employee("Raymond Mariano", "Full-time", "Technician/Installer", 60000, profile_path)
# insert_employee("Tiago Manook", "Full-time", "Technician/Installer", 60000, profile_path)
# insert_employee("Bogart Maravilla", "Full-time", "Assistant", 40000, profile_path)
# insert_employee("Ervin Cruzat", "Full-time", "Forman", 60000, profile_path)





import customtkinter as ctk
import sqlite3
from io import BytesIO
from PIL import Image, ImageTk

# Function to fetch employees from the database
def fetch_employees():
    conn = sqlite3.connect("MAIN UI/employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, job_type, position, salary, profile FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return employees

# # Function to update displayed employees based on search
# def update_list(search_text=""):
#     search_text = search_text.lower()

#     for widget in scrollable_frame.winfo_children():
#         if widget != header_frame: 
#             widget.destroy()

#     filtered_employees = [emp for emp in all_employees if search_text in emp[0].lower()]

#     # Display filtered employees
#     for emp in filtered_employees:
#         name, job_type, position, salary, profile_blob = emp

#         # Convert profile image from BLOB
#         image = Image.open(BytesIO(profile_blob))
#         image = image.resize((40, 40))
#         profile_pic = ImageTk.PhotoImage(image)

#         # Employee Row (Themed Frame)
#         emp_frame = ctk.CTkFrame(scrollable_frame, fg_color="#4B0082", corner_radius=10)  # Purple background
#         emp_frame.pack(fill="x", padx=10, pady=5)

#         # Ensure the grid layout is aligned
#         for i in range(6):  
#             emp_frame.grid_columnconfigure(i, weight=1)

#         # Profile Picture (Properly Centered)
#         img_label = ctk.CTkLabel(emp_frame, image=profile_pic, text="")
#         img_label.image = profile_pic
#         img_label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

#         # Employee Details (Properly Centered)
#         details = [name, job_type, position, f"₱{salary:,.2f}"]
#         for i, text in enumerate(details, 1):
#             lbl = ctk.CTkLabel(emp_frame, text=text, text_color="white", font=("Arial", 13))
#             lbl.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

#         # Action Buttons (Ensure Center Alignment)
#         button_frame = ctk.CTkFrame(emp_frame, fg_color="transparent")
#         button_frame.grid(row=0, column=5, padx=10, pady=5, sticky="ew")

#         attendance_btn = ctk.CTkButton(button_frame, text="Attendance", fg_color="#0073e6", width=80)
#         attendance_btn.pack(side="left", padx=5, pady=5)

#         edit_btn = ctk.CTkButton(button_frame, text="Edit", fg_color="#0073e6", width=50)
#         edit_btn.pack(side="left", padx=5, pady=5)


# def update_list(search_text=""):
#     search_text = search_text.lower()

#     for widget in scrollable_frame.winfo_children():
#         if widget != header_frame: 
#             widget.destroy()

#     filtered_employees = [emp for emp in all_employees if search_text in emp[0].lower()]

#     # Create a new container frame inside the scrollable frame for proper alignment
#     container_frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
#     container_frame.pack(fill="x")

#     for index, emp in enumerate(filtered_employees):
#         name, job_type, position, salary, profile_blob = emp

#         # Convert profile image from BLOB
#         image = Image.open(BytesIO(profile_blob))
#         image = image.resize((40, 40))
#         profile_pic = ImageTk.PhotoImage(image)

#         # Employee Row (Grid instead of Pack)
#         emp_frame = ctk.CTkFrame(container_frame, fg_color="#4B0082", corner_radius=10)  # Purple background
#         emp_frame.grid(row=index, column=0, sticky="ew", padx=10, pady=5)

#         # Ensure the grid layout aligns with the header
#         for i in range(6):  
#             emp_frame.grid_columnconfigure(i, weight=1)

#         # Profile Picture
#         img_label = ctk.CTkLabel(emp_frame, image=profile_pic, text="")
#         img_label.image = profile_pic
#         img_label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

#         # Employee Details (Properly aligned)
#         labels = [
#             (name, 1),
#             (job_type, 2),
#             (position, 3),
#             (f"₱{salary:,.2f}", 4),
#         ]
        
#         for text, col in labels:
#             lbl = ctk.CTkLabel(emp_frame, text=text, text_color="white", font=("Arial", 13))
#             lbl.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

#         # Action Buttons (Properly Aligned)
#         button_frame = ctk.CTkFrame(emp_frame, fg_color="transparent")
#         button_frame.grid(row=0, column=5, padx=10, pady=5, sticky="ew")
        
#         attendance_btn = ctk.CTkButton(button_frame, text="Attendance", fg_color="#0073e6", width=80)
#         attendance_btn.pack(side="left", padx=5, pady=5)
        
#         edit_btn = ctk.CTkButton(button_frame, text="Edit", fg_color="#0073e6", width=50)
#         edit_btn.pack(side="left", padx=5, pady=5)




def update_list(search_text=""):
    search_text = search_text.lower()

    for widget in scrollable_frame.winfo_children():
        if widget != header_frame: 
            widget.destroy()

    filtered_employees = [emp for emp in all_employees if search_text in emp[0].lower()]

    # Create a new container frame inside the scrollable frame for proper alignment
    container_frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
    container_frame.pack(fill="x")

    for index, emp in enumerate(filtered_employees):
        name, job_type, position, salary, profile_blob = emp

        # Convert profile image from BLOB
        image = Image.open(BytesIO(profile_blob))
        image = image.resize((40, 40))
        profile_pic = ImageTk.PhotoImage(image)

        # Employee Row (Ensure Full Width)
        emp_frame = ctk.CTkFrame(container_frame, fg_color="#4B0082", corner_radius=10)
        emp_frame.grid(row=index, column=0, sticky="ew", padx=10, pady=5)

        # Ensure columns stretch properly
        for i in range(6):  
            emp_frame.grid_columnconfigure(i, weight=1)

        # Profile Picture
        img_label = ctk.CTkLabel(emp_frame, image=profile_pic, text="")
        img_label.image = profile_pic
        img_label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        # Employee Details
        labels = [
            (name, 1),
            (job_type, 2),
            (position, 3),
            (f"₱{salary:,.2f}", 4),
        ]
        
        for text, col in labels:
            lbl = ctk.CTkLabel(emp_frame, text=text, text_color="white", font=("Arial", 13))
            lbl.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

        # Action Buttons (Properly Spaced)
        button_frame = ctk.CTkFrame(emp_frame, fg_color="transparent")
        button_frame.grid(row=0, column=5, padx=10, pady=5, sticky="ew")
        
        attendance_btn = ctk.CTkButton(button_frame, text="Attendance", fg_color="#0073e6", width=90)
        attendance_btn.grid(row=0, column=0, padx=5, pady=5)
        
        edit_btn = ctk.CTkButton(button_frame, text="Edit", fg_color="#0073e6", width=60)
        edit_btn.grid(row=0, column=1, padx=5, pady=5)



# Setup GUI
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry("900x600")
app.title("Employee Management")

system_header = ctk.CTkFrame(app, fg_color="transparent")
system_header.pack(fill="x", pady=(10, 0))


# Header Label (Matching Theme)
header = ctk.CTkLabel(system_header, text="Employee Management", font=("Arial", 24, "bold"), text_color="black")
header.pack()

# Search Bar (Centered, Themed)
search_entry = ctk.CTkEntry(app, placeholder_text="Search employee...", width=500, fg_color="white", text_color="black")
search_entry.pack(pady=10)
search_entry.bind("<KeyRelease>", lambda e: update_list(search_entry.get()))

# Scrollable Frame (Themed Background)
scrollable_frame = ctk.CTkScrollableFrame(app, width=880, height=500, fg_color="#D8D8D8")  # Light gray
scrollable_frame.pack(pady=10, fill="both", expand=True)

# Table Header (Created Once)
header_frame = ctk.CTkFrame(scrollable_frame, fg_color="#D8D8D8", corner_radius=0)  # Light gray header
header_frame.pack(fill="x", padx=5, pady=2)

headers = ["Profile", "Name", "Job Type", "Position", "Salary", "Actions"]
for i in range(6):  
    header_frame.grid_columnconfigure(i, weight=1)  

for i, header in enumerate(headers):
    label = ctk.CTkLabel(header_frame, text=header, font=("Arial", 14, "bold"), text_color="black")
    label.grid(row=0, column=i, padx=5, pady=5, sticky="ew")

# col_widths = [100, 120, 150, 180, 120, 150]  # Adjust column widths for proper alignment

# for i, (header, width) in enumerate(zip(headers, col_widths)):
#     label = ctk.CTkLabel(header_frame, text=header, font=("Arial", 14, "bold"), text_color="black")
#     label.grid(row=0, column=i, padx=5, pady=5, sticky="w")
#     header_frame.grid_columnconfigure(i, weight=1, minsize=width)  # Ensure proper alignment

# Load employees initially
all_employees = fetch_employees()
update_list()

app.mainloop()
