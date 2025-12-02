import tkinter as tk
import tkinter.messagebox as msg
import platform

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        # ---------------------------
        # Window Setup
        # ---------------------------
        self.title("Baldree-ToDo")     
        self.geometry("350x500")

        # ---------------------------
        # Instructions Label
        # ---------------------------
        instructions = tk.Label(
            self,
            text="** Add Items Below — Right Click Item to Delete **",
            bg="#8A2BE2",      # purple
            fg="white",
            pady=8,
            font=("Arial", 12, "bold")
        )
        instructions.pack(fill="x")

        # ---------------------------
        # Tasks List Setup
        # ---------------------------
        self.tasks = tasks if tasks else []

        self.tasks_canvas = tk.Canvas(self, bg="white")
        self.tasks_frame = tk.Frame(self.tasks_canvas, bg="white")
        self.text_frame = tk.Frame(self, bg="white")

        self.scrollbar = tk.Scrollbar(
            self.tasks_canvas,
            orient="vertical",
            command=self.tasks_canvas.yview
        )
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="nw"
        )

        # ---------------------------
        # New Task Entry
        # ---------------------------
        self.task_create = tk.Text(self.text_frame, height=2, bg="white", fg="black")
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # ---------------------------
        # Bindings
        # ---------------------------
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)

        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # ---------------------------
        # Alternating Blue / Yellow Color Schemes
        # ---------------------------
        self.colour_schemes = [
            {"bg": "#1E90FF", "fg": "white"},  # Blue
            {"bg": "#FFD700", "fg": "black"}   # Yellow
        ]

        # ---------------------------
        # Menu Bar (File → Exit)
        # ---------------------------
        menu_bar = tk.Menu(self)
        menu_bar.config(bg="#8A2BE2", fg="white")  # purple menu bar

        file_menu = tk.Menu(menu_bar, tearoff=0, bg="#FFD700", fg="black")  # gold dropdown
        file_menu.add_command(label="Exit", command=self.destroy)

        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

        # ---------------------------
        # Render any existing tasks
        # ---------------------------
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

    # ---------------------------
    # Add Task
    # ---------------------------
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(
                self.tasks_frame,
                text=task_text,
                pady=10,
                anchor="w"
            )

            # Set alternating BLUE/YELLOW color
            self.set_task_colour(len(self.tasks), new_task)

            # Right-click delete
            if platform.system() == "Darwin":  # macOS
                new_task.bind("<Button-2>", self.remove_task)
            else:
                new_task.bind("<Button-3>", self.remove_task)

            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    # ---------------------------
    # Delete Task
    # ---------------------------
    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Delete Item", f"Delete '{task.cget('text')}'?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    # ---------------------------
    # Reapply Colors
    # ---------------------------
    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        style = position % 2  # alternate between 0 and 1
        scheme = self.colour_schemes[style]
        task.configure(bg=scheme["bg"], fg=scheme["fg"])

    # ---------------------------
    # Canvas Config
    # ---------------------------
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    # ---------------------------
    # Mouse Scroll
    # ---------------------------
    def mouse_scroll(self, event):
        if event.delta:
            move = int(-1 * (event.delta / 120))
        else:
            move = 1 if event.num == 5 else -1

        self.tasks_canvas.yview_scroll(move, "units")


# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()
