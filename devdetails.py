import tkinter as tk
from tkinter import ttk

class Developers:
    def __init__(self, root=None):
        # Use the provided root or create a new Tk instance
        self.root = root if root else tk.Tk()
        self.root.title("Developers' Details")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f8ff")  # Light azure background
        self.create_ui()

    def create_ui(self):
        # Heading
        heading = tk.Label(
            self.root,
            text="Developers' Details",
            font=("Helvetica", 20, "bold"),
            bg="#002855",  # Navy blue background for heading
            fg="white",    # White text color
            pady=10
        )
        heading.pack(fill=tk.X)

        # Developer details
        developers = [
            {"Name": "SUMIT TIWARI", "Skills": "Python, Flask", "Projects": "TODO List App, Diabetic Model Prediction"},
            {"Name": "SUYOG ACHARYA", "Skills": "Web Development, CSS", "Projects": "Portfolio Website, Diabetic Model Prediction"},
            {"Name": "SAURAV SHARMA WAGLE", "Skills": "Python, JavaScript, React", "Projects": "E-commerce App, Diabetic Model Prediction"},
            {"Name": "AYUSHMAN PANTHI", "Skills": "Python, JavaScript, React", "Projects": "Diabetic Model Prediction, E-commerce App"},
        ]

        # Create a frame for developer details
        details_frame = ttk.Frame(self.root, style="Details.TFrame")
        details_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Create labels for each developer
        for dev in developers:
            dev_frame = ttk.LabelFrame(
                details_frame,
                text=dev["Name"],
                padding=(10, 10),
                style="DevFrame.TLabelframe"
            )
            dev_frame.pack(fill=tk.X, pady=10)

            skills_label = tk.Label(
                dev_frame,
                text=f"Skills: {dev['Skills']}",
                bg="#f9f9f9",  # Light gray background for better contrast
                fg="#002855",  # Navy blue text
                font=("Helvetica", 12),
                anchor="w"
            )
            skills_label.pack(fill=tk.X)

            projects_label = tk.Label(
                dev_frame,
                text=f"Projects: {dev['Projects']}",
                bg="#f9f9f9",  # Light gray background for better contrast
                fg="#002855",  # Navy blue text
                font=("Helvetica", 12),
                anchor="w"
            )
            projects_label.pack(fill=tk.X)

        # Apply styles for ttk widgets
        self.apply_styles()

    def apply_styles(self):
        style = ttk.Style()
        style.configure(
            "DevFrame.TLabelframe",
            background="#f9f9f9",  # Light gray background for frames
            foreground="#002855",  # Navy blue text for frame titles
            font=("Helvetica", 14, "bold")
        )
        style.configure(
            "DevFrame.TLabelframe.Label",
            background="#f9f9f9",  # Light gray background for frame titles
            foreground="#002855",  # Navy blue text
        )
        style.configure(
            "Details.TFrame",
            background="#f0f8ff"  # Light azure background for details area
        )

    def run(self):
        self.root.mainloop()