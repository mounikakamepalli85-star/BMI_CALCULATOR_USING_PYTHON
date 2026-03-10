import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter valid positive values")
            return

        if unit_var.get() == "metric":
            if height < 50:
                messagebox.showerror("Error", "Enter height in cm (Example: 170)")
                return
            height = height / 100
        else:
            weight = weight * 0.453592
            height = height * 0.0254

        bmi = round(weight / (height ** 2), 1)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"{bmi}  {category}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    unit_var.set("metric")



root = tk.Tk()
root.title("BMI")
root.geometry("700x620")
root.configure(bg="#0f7c67")
root.resizable(False, False)


tk.Label(root,
         text="BMI Calculator",
         font=("Arial", 26, "bold"),
         fg="yellow",
         bg="#0f7c67").pack(pady=15)


info_frame = tk.LabelFrame(root,
                           text="Personal Info",
                           fg="yellow",
                           bg="#0f7c67",
                           font=("Arial", 11, "italic","bold"),
                           padx=20,
                           pady=15)
info_frame.pack(padx=20, pady=10, fill="x")

tk.Label(info_frame, text="Name :",
         fg="yellow", bg="#0f7c67",
         font=("Arial", 12)).grid(row=0, column=0, pady=5)

name_entry = tk.Entry(info_frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(info_frame, text="Age :",
         fg="yellow", bg="#0f7c67",
         font=("Arial", 12)).grid(row=1, column=0, pady=5)

age_entry = tk.Entry(info_frame, width=30)
age_entry.grid(row=1, column=1)


unit_frame = tk.LabelFrame(root,
                           text="Unit of measurement",
                           fg="yellow",
                           bg="#0f7c67",
                           font=("Arial", 11, "italic","bold"),
                           padx=20,
                           pady=15)
unit_frame.pack(padx=20, pady=10, fill="x")

unit_var = tk.StringVar(value="metric")

tk.Radiobutton(unit_frame,
               text="lbs / in",
               variable=unit_var,
               value="us",
               fg="white",
               bg="#0f7c67",
               selectcolor="#0f7c67").grid(row=0, column=0, sticky="w")

tk.Radiobutton(unit_frame,
               text="kg / cm",
               variable=unit_var,
               value="metric",
               fg="white",
               bg="#0f7c67",
               selectcolor="#0f7c67").grid(row=1, column=0, sticky="w")

body_frame = tk.LabelFrame(unit_frame,
                           text="Body Profile",
                           fg="yellow",
                           bg="#0f7c67",
                           font=("Arial", 10, "italic","bold"),
                           padx=20,
                           pady=15)
body_frame.grid(row=0, column=1, rowspan=2, padx=60)

tk.Label(body_frame,
         text="Weight (kg):",
         fg="yellow",
         bg="#0f7c67").grid(row=0, column=0, pady=5)

weight_entry = tk.Entry(body_frame, width=12)
weight_entry.grid(row=0, column=1)

tk.Label(body_frame,
         text="Height (cm):",
         fg="yellow",
         bg="#0f7c67").grid(row=1, column=0, pady=5)

height_entry = tk.Entry(body_frame, width=12)
height_entry.grid(row=1, column=1)


btn_frame = tk.Frame(root, bg="#0f7c67")
btn_frame.pack(pady=20)

tk.Button(btn_frame,
          text="Calculate BMI",
          bg="yellow",
          fg="black",
          width=15,
          command=calculate_bmi).grid(row=0, column=0, padx=30)

tk.Button(btn_frame,
          text="Clear",
          bg="yellow",
          fg="black",
          width=15,
          command=clear_fields).grid(row=0, column=1, padx=30)


result_frame = tk.LabelFrame(root,
                             text="Result",
                             fg="yellow",
                             bg="#0f7c67",
                             font=("Arial", 11, "italic","bold"),
                             padx=20,
                             pady=20)
result_frame.pack(padx=20, pady=15, fill="x")

result_label = tk.Label(result_frame,
                        text="",
                        font=("Arial", 20, "bold"),
                        fg="yellow",
                        bg="#0f7c67")
result_label.pack()


footer = tk.Label(root,
                  text="Created by MOUNIKA K",
                  fg="yellow",
                  bg="#0f7c67",
                  font=("Arial", 10,"italic", "bold"))
footer.place(x=20, y=590)

root.mainloop()
