import ttkbootstrap as tb
from ttkbootstrap.constants import *
import customtkinter as ctk
from CTkTable import *

from tools import resize_image


class PayrollApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')
        self.title('Wintercool San Pascual - Payroll')
        self.geometry('1350x700+7+10')
        self.resizable=(False, False)
        self.overrideredirect(True)

        self.profile_win = None

        self.initiate_main_interface()


    def initiate_frames(self):
        style = tb.Style()
        style.configure("FrameBG.TFrame", background="blue")

        self.header_frame = ctk.CTkFrame(self, fg_color='#6A5ACD', corner_radius=0)
        self.main_frame = ctk.CTkFrame(self, fg_color='#F5F5F5')
        self.nav_frame = ctk.CTkFrame(self.main_frame, width=200, fg_color='#E5E5E5', corner_radius=0)

        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color='#ECECEC',
            border_color='#D9D9D9',
            corner_radius=15
        )
        self.content_frame.pack_propagate(False)

        self.header_frame.pack(fill='x', side='top')
        self.main_frame.pack(fill=BOTH, expand=True)
        self.nav_frame.pack(side=LEFT, fill=Y)
        self.content_frame.pack(padx=10, pady=10, side=RIGHT, fill=BOTH, expand=True)


    def initiate_main_interface(self):
        self.initiate_frames()

        self.admin_name = "Admin Name"

        branch_logo = resize_image('assets/images/wintercool_logo.jpg', (125, 100))
        profile_icon = resize_image("assets/icons/Circle Profile (dark).png", (55, 55))

        self.logo_brand = tb.Label(self.header_frame, image=branch_logo, background='#6A5ACD')
        self.logo_brand.image = branch_logo

        self.company_name_label = tb.Label(self.header_frame,
            text='3MI', 
            font=('Segoe UI', 30, 'bold italic'),
            background='#6A5ACD',
            foreground='black'
            )
        
        self.branch_label = tb.Label(self.header_frame,
            text='Payroll Management System',
            font=('Segoe UI', 24),
            background='#6A5ACD',
            foreground='black'
            )

        profile_button = ctk.CTkButton(
            self.header_frame,
            image=profile_icon,
            text="Admin",
            fg_color="transparent",
            hover_color="#8477FF",
            corner_radius=100,
            width=20,
            height=20,
            border_width=0,
            cursor='hand2',
            font=('Roboto', 17),
            command=self.open_profile_window
        )

        self.logo_brand.grid(row=0, column=0, padx=(10, 20), pady=(15, 25))
        self.company_name_label.grid(row=0, column=1, padx=(0, 10), pady=(0, 10))
        self.branch_label.grid(row=0, column=2, pady=(0, 10))
        profile_button.grid(row=0, column=3, padx=(530, 10), pady=(45, 0), sticky='n')

        self.update_view('Dashboard')
        self.initiate_nav_selections()
        

    def initiate_nav_selections(self):
        style = tb.Style()
        style.configure("CustomLink.TButton", background="#F5F5F5", foreground="black", font=('Roboto', 13), padding=10, borderwidth=0, anchor='center')

        style.map("CustomLink.TButton", background=[('active', '#EFEFEF'), ('!disabled', '#E5E5E5')], foreground=[('active', '#6A5ACD'), ('!disabled', 'black')])
        
        # nav_label = tb.Label(self.nav_frame, text='Navigation', font=('Raleway', 16, 'bold'), background='#DDDDDD', width=15, anchor='center')
        nav_label = tb.Label(self.nav_frame, text='Navigation', font=('Poppins', 16, 'bold'), background='#CCCCCC', width=15, anchor='center')
        nav_label.pack_propagate(False)
        nav_label.pack(pady=(75, 5), ipady=6)

        choices = ["Dashboard", "Employee", "Attendance", "Payroll", "Reports", "Advanced"]

        for choice in choices:
            self.btn = tb.Button(self.nav_frame, text=choice, bootstyle='dark primary-link', style='CustomLink.TButton', command=lambda c=choice: self.update_view(c), cursor='hand2')
            self.btn.pack(fill=X, padx=(30, 30), pady=5)

        # self.update_view('Dashboard')
 

    def update_view(self, selected_view):    
        for widget in self.content_frame.winfo_children():
            widget.forget()

        # self.update_idletasks()

        if selected_view == 'Dashboard':
            self.show_main_dashboard()

        elif selected_view == "Employee":
            self.show_employee_section()

        elif selected_view == 'Attendance':
            self.show_main_dashboard()

        elif selected_view == 'Payroll':
            self.show_main_dashboard()

        elif selected_view == 'Reports':
            self.show_main_dashboard()

        elif selected_view == 'Advanced':
            self.show_main_dashboard()

        else:
            pass

    
    def open_profile_window(self):
        if self.profile_win and self.profile_win.winfo_exists():
            return

        self.profile_win = ctk.CTkToplevel(self)
        self.profile_win.title("Admin Profile")
        self.profile_win.geometry("280x170+1050+42")
        self.profile_win.resizable(False, False)
        self.profile_win.overrideredirect(True)
        self.profile_win.attributes("-topmost", True)
        self.profile_win.wm_attributes('-alpha', 0.97)
        self.profile_win.configure(fg_color='#8477FF')
        admin_icon = resize_image("assets/icons/Circle Profile (dark).png", (80, 80))

        profile_label = ctk.CTkLabel(self.profile_win, text='', image=admin_icon, fg_color="#8477FF")
        profile_label.image = admin_icon
        profile_label.pack(pady=(8, 0))

        # Display admin name
        name_label = ctk.CTkLabel(self.profile_win, text=self.admin_name, font=("Arial", 16, "bold"), text_color='#333333')
        name_label.pack()

        def open_profile():
            self.destroy()
        
        profile_button = ctk.CTkButton(
            self.profile_win,
            text="Profile",
            command=open_profile,
            width=100,
            font=('Poppins', 13, 'bold'),
            text_color='white',
            fg_color='#2AB5F4',
            hover_color='#5ACDFA'
        )
        profile_button.pack(
            pady=(0, 10),
            side='left',
            expand=True,
            anchor='e',
            padx=(0, 10)
        )

        def logout():
            self.profile_win.destroy()
        
        logout_button = ctk.CTkButton(
            self.profile_win,
            text="Logout", 
            command=logout,
            width=100,
            font=('Poppins', 13, 'bold'),
            text_color='white',
            fg_color="red",
            hover_color='#FF4D4D'
        )
        logout_button.pack(
            pady=(0, 10),
            side='right',
            expand=True,
            anchor='w',
            padx=(10, 0)
        )

        self.bind("<Button-1>", self.click_outside)

    
    def click_outside(self, event):
        if self.profile_win and self.profile_win.winfo_exists():
            if not (self.profile_win.winfo_rootx() <= event.x_root <= self.profile_win.winfo_rootx() + self.profile_win.winfo_width() and 
                    self.profile_win.winfo_rooty() <= event.y_root <= self.profile_win.winfo_rooty() + self.profile_win.winfo_height()):
                self.profile_win.destroy()
                self.unbind("<Button-1>")


    def add_employee(self):
        pass


    def clear_fields(self):
        pass
        # self.entry_name.delete(0, tk.END)
        # self.entry_position.delete(0, tk.END)
        # self.entry_salary.delete(0, tk.END)
        # self.entry_mobile_no.delete(0, tk.END)
        # self.entry_email.delete(0, tk.END)
        # self.entry_birthdate.delete(0, tk.END)
        # self.entry_nationality.delete(0, tk.END)


    def create_card(self, master, title, value, color):
        card_frame = ctk.CTkFrame(master, width=230, height=130, corner_radius=10, fg_color=color)
        card_frame.pack_propagate(False)
        card_frame.pack(side='left', padx=10, pady=(0, 10))

        title_label = ctk.CTkLabel(
            card_frame,
            text=title,
            font=('Poppins', 17, 'bold'),
            # text_color='black'
        )
        title_label.pack(pady=(10, 0))

        value_label = ctk.CTkLabel(
            card_frame,
            text=value,
            font=('Segoe UI', 24, 'bold'),
            text_color='#FFFFFF'
        )
        value_label.pack(pady=(0, 10))

        info_icon = resize_image("assets/icons/Info (dark).png", (16, 16))

        more_info = ctk.CTkButton(
            card_frame,
            text="More Info",
            image=info_icon,
            compound="left",
            font=("Poppins", 13, 'bold'),
            corner_radius=10,
            text_color='#F8F8FF',
            fg_color=color,
            hover_color=color,
            height=40,
            width=140,
            cursor='hand2',
        )
        more_info.pack(padx=(36, 0), pady=(5, 10), anchor='w')

        return card_frame


    def setup_employee_section(self):
        def button_action():
            print("Button clicked!")

        section_title = ctk.CTkLabel(self.content_frame, text='Employee List', font=('Poppins', 25, 'bold'), fg_color='#ECECEC', text_color='#423784')
        section_title.pack(pady=(20, 5), anchor='w', padx=(35, 0))

        value = [['Profile','Name','Job Type','Position','Salary', 'Actions'],
                 [1,2,3,4,5, 'EDIT -- DELETE'],
                 [1,2,3,4,5, 'EDIT -- DELETE'],
                 [1,2,3,4,5, 'EDIT -- DELETE'],
                 [1,2,3,4,5, 'EDIT -- DELETE']] * 3

        vrow = len(value)

        scrollf = ctk.CTkScrollableFrame(self.content_frame, fg_color='lightgray', width=1000, height=400)
        scrollf.pack(pady=20)
        table = CTkTable(scrollf, row=vrow, column=6, values=value, corner_radius=32, header_color='gray', cursor='hand2', pady=5, padx=0, height=50, font=('Roboto', 16))
        table.edit_row(0, font=('Roboto', 17, 'bold'))
        table.pack(expand=True, fill="both", padx=20, pady=20)

        for cell in value:
            print(cell)
        # button = ctk.CTkButton(table, text="Edit", command=button_action, width=50, height=20)
        # button.place(relx=0.5, rely=0.5, anchor="center")  # Adjust placement


    def setup_dashboard_section(self):
        dashboard_title = ctk.CTkLabel(self.content_frame, text='Dashboard Overview', font=('Poppins', 25, 'bold'), fg_color='#ECECEC', text_color='#423784')
        dashboard_title.pack(pady=(20, 40), anchor='w', padx=(35, 0))

        cards_frame = ctk.CTkFrame(self.content_frame, fg_color='#ECECEC')
        cards_frame.pack()

        payroll_card = self.create_card(cards_frame, 'Total Payroll Cost', 'P50,000', '#2AB5F4')
        employees_card = self.create_card(cards_frame, 'Active Employees', '6', '#2EB463')
        absent_card = self.create_card(cards_frame, 'Absent Employees', '2', '#D64545')
        next_payroll_card = self.create_card(cards_frame, 'Next Payroll', 'Jan 15, 2025', '#E8A100')

        self.below_cards_frame = ctk.CTkFrame(self.content_frame, fg_color='#ECECEC', corner_radius=0, width=830, height=200)
        self.below_cards_frame.pack_propagate(False)
        self.below_cards_frame.pack(pady=(0, 20))

        # NOTIFICATIONS
        notifications_frame = ctk.CTkFrame(self.below_cards_frame, width=400, height=150, corner_radius=10, fg_color='#F0B733')
        notifications_frame.pack_propagate(False)
        notifications_frame.pack(side='right')

        notifications_label = ctk.CTkLabel(notifications_frame, text='⚠️ Notifications', font=('Arial', 18, 'bold'), text_color='black')
        notifications_label.pack(pady=(10, 5))

        notifications_text = ctk.CTkLabel(notifications_frame, text='📌 Next Payroll on Jan 15, 2025', font=('Roboto', 17), text_color='black')
        notifications_text.pack(pady=10)

        # ATTENDANCE

        attendace_frame = ctk.CTkFrame(self.below_cards_frame, width=400, height=150, corner_radius=10, fg_color='#897DCC')
        attendace_frame.pack_propagate(False)
        attendace_frame.pack(side='left')

        attendace_label = ctk.CTkLabel(attendace_frame, text='📆 Attendance Logs', font=('Arial', 18, 'bold'))
        attendace_label.pack(pady=(10, 5))

        # Footholder Here

        show_overlay_button = ctk.CTkButton(self.content_frame, text='Enable Overlays', command=self.enable_overlays, width=500)
        show_overlay_button.pack(pady=(0, 10))

    def enable_overlays(self):
        self.below_cards_frame.configure(border_width=1, border_color='black')

    def show_main_dashboard(self):
        self.setup_dashboard_section()
        # graph_frame.pack_forget()  # Hide graph placeholder

    def show_employee_section(self):
        # graph_frame.pack_forget()  # Hide graph placeholder
        self.setup_employee_section()

    def show_attendance_section(self):
        pass

    def show_payroll_section(self):
        pass
        
    def show_reports_section(self):
        pass

    def show_advanced_section(self):
        pass

    def on_label_click(self):
        print('Dashboard clicked!')

    def logout(self):
        self.quit()

    def run(self):
        self.mainloop()



if __name__ == '__main__':
    app = PayrollApp()
    app.mainloop()
