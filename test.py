import tkinter as tk
from tkinter import ttk, messagebox
import time

# ----------------------------
# LIGHTED TITLE / GLOW EFFECT
# ----------------------------
def create_glowing_title(root, text):
    # Shadow layers for soft glow
    shadow_colors = ["#a0c4ff", "#b0d0ff", "#c0e0ff"]  # soft glow colors
    for i, color in enumerate(shadow_colors):
        tk.Label(root, text=text,
                 font=("Segoe UI", 28, "bold"),
                 fg=color,
                 bg="#c9d6ff").place(relx=0.5, y=60+i*2, anchor="center")
    
    # Main bright text
    tk.Label(root, text=text,
             font=("Segoe UI", 28, "bold"),
             fg="black",
             bg="#c9d6ff").place(relx=0.5, y=60, anchor="center")

# ============================
# MAIN MENU WINDOW
# ============================
def main_menu():
    clear_window()
    root.configure(bg="#c9d6ff")
    
    # Full-width header
    header_frame = tk.Frame(root, bg="#c9d6ff", height=120)
    header_frame.pack(fill="x", padx=40, pady=(20, 0))
    
    # Title that spans width
    tk.Label(header_frame, text="Health & Wellness Assistant", 
             font=("Segoe UI", 36, "bold"),
             fg="#2c3e50",
             bg="#c9d6ff").pack()
    
    tk.Label(header_frame, text="Your Complete Health Management Solution",
             font=("Segoe UI", 14),
             fg="#5a7cff",
             bg="#c9d6ff").pack(pady=(5, 0))
    
    # Decorative line under title
    tk.Frame(root, height=2, bg="#6fa8dc", bd=0).pack(fill="x", padx=80, pady=(10, 0))
    
    # Main content area - takes most of the screen
    content_frame = tk.Frame(root, bg="#d8e3ff")  # Slightly darker for contrast
    content_frame.pack(fill="both", expand=True, padx=40, pady=30)
    
    # Features section title
    tk.Label(content_frame, text="Health Management Tools",
             font=("Segoe UI", 24, "bold"),
             bg="#d8e3ff",
             fg="#2c3e50").pack(pady=(20, 30))
    
    # Container for feature cards - wider grid
    cards_container = tk.Frame(content_frame, bg="#d8e3ff")
    cards_container.pack(fill="both", expand=True)
    
    # Feature cards in a single row to fill width
    features = [
        ("📊", "BMI & Calorie\nCalculator", 
         "Calculate BMI and daily\ncalorie requirements", 
         BMI_page, "#6fa8dc"),
        ("⏰", "Medication\nReminder", 
         "Set and manage\nmedication reminders", 
         medication_page, "#6fa8dc"),
        ("📝", "Daily Wellness\nLog", 
         "Track your daily wellness\nand mood", 
         wellness_page, "#6fa8dc"),
        ("👣", "Step Counter\nLog", 
         "Log and monitor\ndaily steps", 
         step_counter_page, "#6fa8dc"),
    ]
    
    # Create cards in a row
    for i, (icon, title, description, command, color) in enumerate(features):
        card_frame = tk.Frame(cards_container, bg="#d8e3ff")
        card_frame.pack(side="left", fill="both", expand=True, padx=15)
        
        # Card with shadow effect
        card = tk.Frame(card_frame, bg="white", width=200, height=250)
        card.pack_propagate(False)
        card.pack()
        
        # Card styling
        card.config(highlightbackground="#b8c9ff", highlightthickness=2)
        
        # Card content
        tk.Label(card, text=icon, font=("Segoe UI", 42),
                bg="white", fg=color).pack(pady=(30, 10))
        
        tk.Label(card, text=title, font=("Segoe UI", 16, "bold"),
                bg="white", fg="#2c3e50", wraplength=180).pack(pady=5)
        
        tk.Label(card, text=description, font=("Segoe UI", 11),
                bg="white", fg="#666666", wraplength=180).pack(pady=10, padx=10)
        
        # Card button
        card_btn = tk.Button(card, text="Open Feature →",
                           font=("Segoe UI", 11, "bold"),
                           bg=color,
                           fg="white",
                           relief="flat",
                           padx=20,
                           pady=8,
                           command=command)
        card_btn.pack(pady=20)
        
        # Hover effects for entire card
        def on_enter_card(e, c=card, b=card_btn, col=color):
            c.config(bg="#f8faff")
            c.config(highlightbackground=color)
            b.config(bg="#5a96d9")
            b.config(cursor="hand2")
            c.config(cursor="hand2")
        
        def on_leave_card(e, c=card, b=card_btn, col=color):
            c.config(bg="white")
            c.config(highlightbackground="#b8c9ff")
            b.config(bg=col)
        
        card.bind("<Enter>", on_enter_card)
        card.bind("<Leave>", on_leave_card)
        card_btn.bind("<Enter>", on_enter_card)
        card_btn.bind("<Leave>", on_leave_card)
        card.bind("<Button-1>", lambda e, cmd=command: cmd())
    
    # Bottom section with exit button
    bottom_frame = tk.Frame(root, bg="#c9d6ff", height=100)
    bottom_frame.pack(side="bottom", fill="x", padx=40, pady=(0, 20))
    
    # Decorative line above exit button
    tk.Frame(bottom_frame, height=2, bg="#6fa8dc", bd=0).pack(fill="x", pady=(0, 20))
    
    # Centered exit button
    btn_frame = tk.Frame(bottom_frame, bg="#c9d6ff")
    btn_frame.pack()
    
    exit_btn = tk.Button(btn_frame, text="🚪 Exit Application",
                        font=("Segoe UI", 14, "bold"),
                        bg="#e74c3c",
                        fg="white",
                        width=25,
                        height=2,
                        relief="flat",
                        bd=0,
                        command=root.destroy)
    exit_btn.pack()
    
    # Hover effect for exit button
    def on_enter_exit(e):
        exit_btn.config(bg="#c0392b")
        exit_btn.config(cursor="hand2")
    
    def on_leave_exit(e):
        exit_btn.config(bg="#e74c3c")
    
    exit_btn.bind("<Enter>", on_enter_exit)
    exit_btn.bind("<Leave>", on_leave_exit)
    
    # Health tip at the bottom
    health_tips = [
        "💡 Tip: Drink 8 glasses of water daily for optimal health",
        "💡 Tip: Aim for 7-9 hours of sleep each night",
        "💡 Tip: Regular exercise boosts both physical and mental health",
        "💡 Tip: Balanced nutrition is key to maintaining good health"
    ]
    
    tip_label = tk.Label(bottom_frame, 
                        text=health_tips[0],
                        font=("Segoe UI", 11, "italic"),
                        bg="#c9d6ff",
                        fg="#5a7cff")
    tip_label.pack(pady=(15, 0))
    
    # Rotate tips
    def rotate_tip():
        current = tip_label.cget("text")
        index = health_tips.index(current) if current in health_tips else 0
        next_index = (index + 1) % len(health_tips)
        tip_label.config(text=health_tips[next_index])
        root.after(5000, rotate_tip)
    
    root.after(5000, rotate_tip)

# =====================================================
# PAGE CLEAR FUNCTION
# =====================================================
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# =====================================================
# ADVANCED DASHBOARD BMI PAGE (GAUGE + MODERN UI)
# =====================================================
def BMI_page():
    clear_window()
    root.configure(bg="#f2f2f2")

    # -------- MAIN CARD -------- #
    card = tk.Frame(root, bg="white", padx=40, pady=40)
    card.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(card, text="BMI Dashboard", font=("Segoe UI", 26, "bold"), bg="white")
    title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # -------- INPUT FIELDS -------- #
    tk.Label(card, text="Weight (kg):", font=("Segoe UI", 16), bg="white").grid(row=1, column=0, sticky="e", padx=15, pady=10)
    weight_entry = tk.Entry(card, font=("Segoe UI", 16), width=12, bd=2, relief="groove")
    weight_entry.grid(row=1, column=1, pady=10)

    tk.Label(card, text="Height (cm or m):", font=("Segoe UI", 16), bg="white").grid(row=2, column=0, sticky="e", padx=15, pady=10)
    height_entry = tk.Entry(card, font=("Segoe UI", 16), width=12, bd=2, relief="groove")
    height_entry.grid(row=2, column=1, pady=10)

    # -------- ACTIVITY LEVEL -------- #
    tk.Label(card, text="Activity Level:", font=("Segoe UI", 16), bg="white").grid(row=3, column=0, sticky="e", padx=15, pady=10)
    activity_var = tk.StringVar()
    activity_combo = ttk.Combobox(card, textvariable=activity_var, font=("Segoe UI", 14), width=14,
                                  values=[
                                      "Sedentary (little exercise)",
                                      "Lightly Active (1-3 days/wk)",
                                      "Moderately Active (3-5 days/wk)",
                                      "Very Active (6-7 days/wk)",
                                      "Extra Active (intense daily)"
                                  ])
    activity_combo.grid(row=3, column=1, pady=10)
    activity_combo.current(0)

    # -------- GOAL SELECTION -------- #
    tk.Label(card, text="Goal:", font=("Segoe UI", 16), bg="white").grid(row=4, column=0, sticky="e", padx=15, pady=10)
    goal_var = tk.StringVar()
    goal_combo = ttk.Combobox(card, textvariable=goal_var, font=("Segoe UI", 14), width=14,
                              values=["Maintain Weight", "Lose Weight", "Gain Weight"])
    goal_combo.grid(row=4, column=1, pady=10)
    goal_combo.current(0)

    # -------- GAUGE CANVAS -------- #
    gauge_canvas = tk.Canvas(card, width=300, height=180, bg="white", highlightthickness=0)
    gauge_canvas.grid(row=5, column=0, columnspan=2, pady=20)

    # -------- RESULT LABEL -------- #
    result_label = tk.Label(card, text="", font=("Segoe UI", 18), bg="white")
    result_label.grid(row=6, column=0, columnspan=2, pady=10)

    # -------- CALORIE COLOR BAR -------- #
    bar_canvas = tk.Canvas(card, width=300, height=25, bg="white", highlightthickness=0)
    bar_canvas.grid(row=7, column=0, columnspan=2, pady=10)

    bar_canvas.create_rectangle(0, 0, 75, 25, fill="#4da6ff")     # Underweight
    bar_canvas.create_rectangle(75, 0, 150, 25, fill="#66cc66")   # Normal
    bar_canvas.create_rectangle(150, 0, 225, 25, fill="#ffcc00")  # Overweight
    bar_canvas.create_rectangle(225, 0, 300, 25, fill="#ff6666")  # Obese

    bar_pointer = bar_canvas.create_line(0, 0, 0, 25, width=4, fill="black")

    # -------- CALCULATE FUNCTION -------- #
    def calculate():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())

            if height > 3:
                height /= 100

            bmi = weight / (height ** 2)

            # Category + pointer x-position
            if bmi < 18.5:
                cat = "Underweight"; x = 37
            elif bmi < 24.9:
                cat = "Normal"; x = 112
            elif bmi < 29.9:
                cat = "Overweight"; x = 187
            else:
                cat = "Obese"; x = 262

            # -------- ACTIVITY MULTIPLIER -------- #
            level = activity_var.get()
            if "Sedentary" in level: mult = 1.2
            elif "Lightly" in level: mult = 1.375
            elif "Moderately" in level: mult = 1.55
            elif "Very" in level: mult = 1.725
            else: mult = 1.9

            # -------- MAINTENANCE CALORIES -------- #
            maintenance = weight * 22 * mult

            # -------- GOAL CALORIES -------- #
            goal = goal_var.get()
            if goal == "Lose Weight":
                calories = maintenance - 400
            elif goal == "Gain Weight":
                calories = maintenance + 300
            else:
                calories = maintenance

            # Results text update
            result_label.config(
                text=f"BMI: {bmi:.2f} ({cat})\n"
                     f"Daily Calories ({goal}): {calories:.0f} kcal"
            )

            # Update pointer
            bar_canvas.coords(bar_pointer, x, 0, x, 25)

            # -------- GAUGE DRAW -------- #
            gauge_canvas.delete("all")

            gauge_canvas.create_arc(10, 10, 290, 290, start=180, extent=180,
                                    style="arc", width=25, outline="#e6e6e6")

            angle = min(bmi, 40) * (180 / 40)

            if cat == "Underweight": color="#4da6ff"
            elif cat == "Normal": color="#66cc66"
            elif cat == "Overweight": color="#ffcc00"
            else: color="#ff6666"

            gauge_canvas.create_arc(10, 10, 290, 290, start=180, extent=angle,
                                    style="arc", width=25, outline=color)

            gauge_canvas.create_text(150, 120, text=f"{bmi:.1f}", font=("Segoe UI", 28, "bold"), fill=color)

        except:
            result_label.config(text="Invalid input. Please enter numbers.")

    # -------- BUTTONS -------- #
    tk.Button(card, text="Calculate", font=("Segoe UI", 16),
              bg="#4da6ff", fg="white", padx=20, pady=5,
              command=calculate).grid(row=8, column=0, columnspan=2, pady=(15, 5))

    tk.Button(card, text="🔙 Back to Main Menu", font=("Segoe UI", 14),
              bg="#e0e0e0", fg="black", padx=20, pady=5,
              command=main_menu).grid(row=9, column=0, columnspan=2, pady=10)



# =====================================================
# MEDICATION REMINDER PAGE 
# =====================================================
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

def load_reminders():
    return []

def save_reminders(data):
    pass

def is_valid_time(t):
    if len(t) != 5 or t[2] != ':':
        return False
    hh, mm = t.split(':')
    if not (hh.isdigit() and mm.isdigit()):
        return False
    hh = int(hh)
    mm = int(mm)
    return 0 <= hh < 24 and 0 <= mm < 60


def medication_page():
    clear_window()

    class ScheduleApp:
        def __init__(self, frame):
            self.frame = frame
            self.frame.configure(bg="#f0f4f8")

            self.reminders = load_reminders()
            self.setup_ui()
            self.update_list()
            self.update_countdown()

        # ------------------------ UI SETUP ------------------------
        def setup_ui(self):
            tk.Label(self.frame, text="Schedule Reminder 💊",
                     font=("Arial", 24), bg="#f0f4f8", fg="#0b3d91").pack(pady=(15, 10))

            self.label_next = tk.Label(self.frame, text="Next Schedule ⏰: --:--",
                                       font=("Arial", 18), bg="#f0f4f8", fg="#2c3e50")
            self.label_next.pack(pady=(0, 5))

            self.label_countdown = tk.Label(self.frame, text="Countdown ⏳: --:--:--",
                                            font=("Arial", 18), bg="#f0f4f8", fg="#27ae60")
            self.label_countdown.pack(pady=(0, 15))

            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview.Heading", background="#34495e", foreground="white",
                            font=("Arial", 12, "bold"))
            style.configure("Treeview", font=("Arial", 11), rowheight=25,
                            background="white", fieldbackground="white")
            style.map("Treeview",
                      background=[("selected", "#3498db")],
                      foreground=[("selected", "white")])

            columns = ("name", "dosage", "time", "on")
            self.tree = ttk.Treeview(self.frame, columns=columns, show="headings", height=14)
            self.tree.heading("name", text="Medicine Name")
            self.tree.heading("dosage", text="Dosage")
            self.tree.heading("time", text="Time")
            self.tree.heading("on", text="On/Off")

            self.tree.column("name", width=220)
            self.tree.column("dosage", width=140)
            self.tree.column("time", width=140)
            self.tree.column("on", width=80)

            self.tree.tag_configure("oddrow", background="#ecf0f1")
            self.tree.tag_configure("evenrow", background="white")

            self.tree.pack(expand=True, fill="both", padx=20)

            btn_frame = tk.Frame(self.frame, bg="#f0f4f8")
            btn_frame.pack(pady=20)

            tk.Button(btn_frame, text="➕ Add", font=("Arial", 16),
                      width=10, command=self.open_add_window, bg="#2980b9",
                      fg="white", relief="flat").pack(side="left", padx=10)

            tk.Button(btn_frame, text="✏️ Edit", font=("Arial", 16),
                      width=10, command=self.open_edit_window, bg="#2980b9",
                      fg="white", relief="flat").pack(side="left", padx=10)

            tk.Button(btn_frame, text="⬅ Back", font=("Arial", 16),
                      width=10, command=main_menu, bg="#2980b9",
                      fg="white", relief="flat").pack(side="left", padx=10)

        # ------------------------ DATA LIST ------------------------
        def update_list(self):
            for row in self.tree.get_children():
                self.tree.delete(row)

            for i, r in enumerate(self.reminders):
                tag = "evenrow" if i % 2 == 0 else "oddrow"
                self.tree.insert("", "end",
                                 values=(r["name"], r["dosage"], r["time"],
                                         "ON" if r["on"] else "OFF"),
                                 tags=(tag,))

        # ------------------------ NEXT REMINDER ------------------------
        def get_next_reminder(self):
            now = datetime.now()
            soonest = None
            item = None

            for r in self.reminders:
                if not r["on"]:
                    continue
                try:
                    h, m = map(int, r["time"].split(":"))
                except:
                    continue

                t = now.replace(hour=h, minute=m, second=0, microsecond=0)
                if t < now:
                    t += timedelta(days=1)

                if soonest is None or t < soonest:
                    soonest = t
                    item = r
            return soonest, item

        # ------------------------ COUNTDOWN TIMER ------------------------
        def update_countdown(self):
            next_time, item = self.get_next_reminder()

            if next_time:
                self.label_next.config(text=f"Next Schedule ⏰: {item['time']}")
                diff = next_time - datetime.now()

                if diff.total_seconds() <= 1:
                    messagebox.showinfo("Reminder",
                                        f"Time to take medicine 💉:\n{item['name']} ({item['dosage']})")
                    self.frame.after(1000, self.update_countdown)
                    return

                h = diff.seconds // 3600
                m = (diff.seconds % 3600) // 60
                s = diff.seconds % 60
                self.label_countdown.config(text=f"Countdown ⏳: {h:02}:{m:02}:{s:02}")
            else:
                self.label_next.config(text="Next Schedule ⏰: --:--")
                self.label_countdown.config(text="Countdown ⏳: --:--:--")

            self.frame.after(1000, self.update_countdown)

        # ------------------------ ADD NEW ------------------------
        def open_add_window(self):
            win = tk.Toplevel(self.frame)
            win.title("➕ Add Reminder")
            win.geometry("420x350")

            tk.Label(win, text="Medicine Name:", font=("Arial", 16)).pack(pady=10)
            name_entry = tk.Entry(win, font=("Arial", 16))
            name_entry.pack()

            tk.Label(win, text="Dosage:", font=("Arial", 16)).pack(pady=10)
            dose_entry = tk.Entry(win, font=("Arial", 16))
            dose_entry.pack()

            tk.Label(win, text="Time (HH:MM):", font=("Arial", 16)).pack(pady=10)
            time_entry = tk.Entry(win, font=("Arial", 16))
            time_entry.pack()

            def save_new():
                name = name_entry.get().strip()
                dose = dose_entry.get().strip()
                tim = time_entry.get().strip()

                if not name or not dose or not tim:
                    messagebox.showwarning("Error", "All fields required")
                    return
                if not is_valid_time(tim):
                    messagebox.showwarning("Error", "Invalid time format (HH:MM)")
                    return

                self.reminders.append({
                    "name": name,
                    "dosage": dose,
                    "time": tim,
                    "on": True
                })

                save_reminders(self.reminders)
                self.update_list()
                win.destroy()

            tk.Button(win, text="💾Save", font=("Arial", 18), command=save_new).pack(pady=20)

        # ------------------------ EDIT / DELETE ------------------------
        def open_edit_window(self):
            win = tk.Toplevel(self.frame)
            win.title("Edit Reminder")
            win.geometry("420x350")

            names = [r["name"] for r in self.reminders]

            tk.Label(win, text="Select Reminder:", font=("Arial", 16)).pack(pady=10)
            combo = ttk.Combobox(win, values=names, font=("Arial", 16))
            combo.pack()

            def edit_selected():
                sel = combo.get()
                if not sel:
                    messagebox.showwarning("Error", "Select one")
                    return

                for r in self.reminders:
                    if r["name"] == sel:
                        self.edit_item_window(r)
                        win.destroy()
                        return

            def delete_selected():
                sel = combo.get()
                if messagebox.askyesno("Confirm Delete", f"Delete '{sel}'?"):
                    self.reminders = [r for r in self.reminders if r["name"] != sel]
                    save_reminders(self.reminders)
                    self.update_list()
                    win.destroy()

            tk.Button(win, text="✏️ Edit", font=("Arial", 16), command=edit_selected).pack(pady=10)
            tk.Button(win, text="🗑 Delete", font=("Arial", 16), command=delete_selected).pack(pady=10)

        # ------------------------ EDIT WINDOW ------------------------
        def edit_item_window(self, item):
            win = tk.Toplevel(self.frame)
            win.title("Edit Item")
            win.geometry("420x360")

            tk.Label(win, text="Medicine Name:", font=("Arial", 16)).pack(pady=10)
            name_e = tk.Entry(win, font=("Arial", 16))
            name_e.insert(0, item["name"])
            name_e.pack()

            tk.Label(win, text="Dosage:", font=("Arial", 16)).pack(pady=10)
            dose_e = tk.Entry(win, font=("Arial", 16))
            dose_e.insert(0, item["dosage"])
            dose_e.pack()

            tk.Label(win, text="Time (HH:MM):", font=("Arial", 16)).pack(pady=10)
            time_e = tk.Entry(win, font=("Arial", 16))
            time_e.insert(0, item["time"])
            time_e.pack()

            on_var = tk.BooleanVar(value=item.get("on", True))
            tk.Checkbutton(win, text="Enabled Reminder",
                           variable=on_var, font=("Arial", 14)).pack(pady=10)

            def save_edit():
                name = name_e.get().strip()
                dose = dose_e.get().strip()
                tim = time_e.get().strip()

                if not name or not dose or not tim:
                    messagebox.showwarning("Error", "All fields required")
                    return
                if not is_valid_time(tim):
                    messagebox.showwarning("Error", "Invalid time")
                    return

                item["name"] = name
                item["dosage"] = dose
                item["time"] = tim
                item["on"] = on_var.get()

                save_reminders(self.reminders)
                self.update_list()
                win.destroy()

            tk.Button(win, text="💾Save Changes", font=("Arial", 18),
                      command=save_edit).pack(pady=20)

    # Create the new Schedule UI inside your main root window
    ScheduleApp(root)


# =====================================================
# DAILY WELLNESS LOG PAGE (MODERN DASHBOARD STYLE)
# =====================================================
def wellness_page():
    clear_window()

    # --- Beautiful Gradient Background ---
    root.configure(bg="#c9d6ff")  # soft cool gradient base color

    # --- Title ---
    tk.Label(root, text="Daily Wellness Log", font=("Arial", 22, "bold"),
             bg="#c9d6ff", fg="#2d2d2d").pack(pady=20)

    # --- Modern Center Card ---
    card = tk.Frame(root, bg="white", bd=0, relief="ridge")
    card.pack(pady=20, padx=20, fill="both", expand=True)

    card.configure(highlightbackground="#d0d0d0", highlightthickness=1)
    card.pack_propagate(False)

    # --- Inputs inside card ---
    input_frame = tk.Frame(card, bg="white")
    input_frame.pack(pady=20)

    # Mood
    tk.Label(input_frame, text="Mood Today:", bg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
    mood_entry = tk.Entry(input_frame, width=35, font=("Arial", 11), relief="groove", bd=2)
    mood_entry.grid(row=0, column=1, pady=10)

    # Sleep
    tk.Label(input_frame, text="Hours of Sleep:", bg="white", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
    sleep_entry = tk.Entry(input_frame, width=35, font=("Arial", 11), relief="groove", bd=2)
    sleep_entry.grid(row=1, column=1, pady=10)

    # Meals
    tk.Label(input_frame, text="Meals Summary:", bg="white", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
    meal_entry = tk.Entry(input_frame, width=35, font=("Arial", 11), relief="groove", bd=2)
    meal_entry.grid(row=2, column=1, pady=10)

    # --- Log Display ---
    tk.Label(card, text="Daily Logs", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

    log_list = tk.Listbox(card, width=70, height=10, font=("Arial", 11), bd=2, relief="ridge")
    log_list.pack(pady=10)

    # --- Add Log Function ---
    def add_log():
        mood = mood_entry.get()
        sleep = sleep_entry.get()
        meal = meal_entry.get()

        if mood == "" or sleep == "" or meal == "":
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        log_list.insert(tk.END, f"Mood: {mood} | Sleep: {sleep} hrs | Meals: {meal}")

        mood_entry.delete(0, tk.END)
        sleep_entry.delete(0, tk.END)
        meal_entry.delete(0, tk.END)

    # --- Add Log Button ---
    tk.Button(card, text="Add Log", width=15, height=1,
              bg="#6fa8dc", fg="white", font=("Arial", 12, "bold"),
              relief="flat", command=add_log).pack(pady=10)

    # --- Back Button ---
    tk.Button(root, text="🔙 Back to Main Menu", width=25,
              bg="#444444", fg="white", font=("Arial", 12),
              command=main_menu).pack(pady=15)


# =====================================================
# STEP COUNTER LOG PAGE (MODERN STYLE)
# =====================================================
def step_counter_page():
    clear_window()

    # Background upgrade
    root.configure(bg="#c9d6ff")  # soft gradient-like background

    # Title
    tk.Label(root, text="Step Counter Log", font=("Segoe UI", 22, "bold"),
             bg="#c9d6ff").pack(pady=20)

    # Modern card
    card = tk.Frame(root, bg="white", padx=30, pady=30)
    card.pack(pady=20)
    card.configure(highlightbackground="#d0d0d0", highlightthickness=1)

    # Input frame
    frame = tk.Frame(card, bg="white")
    frame.pack(pady=10)

    tk.Label(frame, text="Steps Today:", font=("Segoe UI", 14),
             bg="white").grid(row=0, column=0, padx=10, pady=10)
    
    step_entry = tk.Entry(frame, width=20, font=("Segoe UI", 14),
                          bd=2, relief="groove")
    step_entry.grid(row=0, column=1, pady=10)

    # Log title
    tk.Label(card, text="Step Log Records", font=("Segoe UI", 14, "bold"),
             bg="white").pack(pady=10)

    # Listbox
    log_list = tk.Listbox(card, width=50, height=8,
                          font=("Segoe UI", 12), bd=2, relief="ridge")
    log_list.pack(pady=10)

    # Add Step Function
    def add_steps():
        steps = step_entry.get()

        if steps == "":
            messagebox.showerror("Error", "Please enter the number of steps.")
            return

        log_list.insert(tk.END, f"Steps: {steps}")
        step_entry.delete(0, tk.END)

    # Add Steps button
    tk.Button(card, text="Add Steps", font=("Segoe UI", 14),
              bg="#6fa8dc", fg="white", padx=20, pady=5,
              relief="flat", command=add_steps).pack(pady=10)

    # Back button (same style as BMI + wellness)
    tk.Button(root, text="🔙 Back to Main Menu", font=("Segoe UI", 14),
              bg="#444444", fg="white", padx=20, pady=5,
              command=main_menu).pack(pady=15)



# =====================================================
# START APPLICATION
# =====================================================
root = tk.Tk()
root.title("Health & Wellness Assistant App ")
root.geometry("820x550")
root.configure(bg="#e6e6e6")

main_menu()
root.mainloop()