import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title("Normal Distribution Simulator")
root.geometry("900x600")
root.config(bg="#F5F5F5")

style = ttk.Style()
style.configure("TLabel", background="#F5F5F5",
                foreground="#333333", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=5)
style.configure("TEntry", font=("Helvetica", 12),
                foreground="#000000", padding=5)
style.configure("TCombobox", font=("Helvetica", 12), padding=5)


def calculate_and_plot():
    try:
        mu = mu_entry.get()
        sigma = sigma_entry.get()
        x_value = x_entry.get()
        a_value = a_entry.get()
        b_value = b_entry.get()
        query_type = query_combo.get()

        if not (is_number(mu) and is_number(sigma)):
            messagebox.showerror(
                "Invalid Input", "Mean (µ) and Standard Deviation (σ) must be numeric values.")
            return

        mu = float(mu)
        sigma = float(sigma)

        if sigma <= 0:
            messagebox.showerror(
                "Invalid Input", "Standard deviation (σ) must be greater than zero.")
            return

        x_value = float(x_value) if x_value else None
        a_value = float(a_value) if a_value else None
        b_value = float(b_value) if b_value else None

        if "x" in query_type:
            if x_value is None:
                messagebox.showerror(
                    "Invalid Input", "Please enter a value for x.")
                return
        if "a" in query_type or "b" in query_type:
            if a_value is None or b_value is None:
                messagebox.showerror(
                    "Invalid Input", "Both a and b values must be provided.")
                return
            if a_value > b_value:
                messagebox.showerror(
                    "Invalid Input", "a must be less than or equal to b.")
                return

        x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
        y = norm.pdf(x, mu, sigma)

        fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
        ax.plot(x, y, color='#007ACC', lw=2)
        ax.set_title("Normal Distribution", fontsize=14, fontweight='bold')
        ax.set_xlabel("X Values", fontsize=12)
        ax.set_ylabel("Probability Density", fontsize=12)
        ax.grid(color='#D3D3D3', linestyle='--', linewidth=0.5)

        result = ""
        if query_type == "P(X = x)":
            prob = norm.pdf(x_value, mu, sigma)
            result = f"P(X = {x_value}) = {prob:.5f}"
            ax.axvline(x_value, color='red', linestyle='--', label='X Value')
            ax.legend()
        elif query_type == "P(X <= x)":
            prob = norm.cdf(x_value, mu, sigma)
            result = f"P(X <= {x_value}) = {prob:.5f}"
            ax.fill_between(x, y, where=(x <= x_value),
                            color='#FFA07A', alpha=0.5, label='Area P(X <= x)')
            ax.axvline(x_value, color='red', linestyle='--', label='X Value')
            ax.legend()
        elif query_type == "P(X >= x)":
            prob = 1 - norm.cdf(x_value, mu, sigma)
            result = f"P(X >= {x_value}) = {prob:.5f}"
            ax.fill_between(x, y, where=(x >= x_value),
                            color='#FFA07A', alpha=0.5, label='Area P(X >= x)')
            ax.axvline(x_value, color='red', linestyle='--', label='X Value')
            ax.legend()
        elif query_type in ["P(a <= X <= b)", "P(a <= X < b)", "P(a < X <= b)", "P(a < X < b)"]:
            prob = norm.cdf(b_value, mu, sigma) - norm.cdf(a_value, mu, sigma)
            if query_type == "P(a <= X <= b)":
                ax.fill_between(x, y, where=(x >= a_value) & (
                    x <= b_value), color='#FFD700', alpha=0.5, label='Area P(a <= X <= b)')
            elif query_type == "P(a <= X < b)":
                ax.fill_between(x, y, where=(x >= a_value) & (
                    x < b_value), color='#FFD700', alpha=0.5, label='Area P(a <= X < b)')
            elif query_type == "P(a < X <= b)":
                ax.fill_between(x, y, where=(x > a_value) & (
                    x <= b_value), color='#FFD700', alpha=0.5, label='Area P(a < X <= b)')
            elif query_type == "P(a < X < b)":
                ax.fill_between(x, y, where=(x > a_value) & (
                    x < b_value), color='#FFD700', alpha=0.5, label='Area P(a < X < b)')
            result = f"{query_type.replace('X', 'X')}: {prob:.5f}"
            ax.axvline(a_value, color='green', linestyle='--', label='a Value')
            ax.axvline(b_value, color='purple',
                       linestyle='--', label='b Value')
            ax.legend()
        elif query_type == "P(X < x)":
            prob = norm.cdf(x_value, mu, sigma)
            result = f"P(X < {x_value}) = {prob:.5f}"
            ax.fill_between(x, y, where=(x < x_value),
                            color='#FFA07A', alpha=0.5, label='Area P(X < x)')
            ax.axvline(x_value, color='red', linestyle='--', label='X Value')
            ax.legend()
        elif query_type == "P(X > x)":
            prob = 1 - norm.cdf(x_value, mu, sigma)
            result = f"P(X > {x_value}) = {prob:.5f}"
            ax.fill_between(x, y, where=(x > x_value),
                            color='#FFA07A', alpha=0.5, label='Area P(X > x)')
            ax.axvline(x_value, color='red', linestyle='--', label='X Value')
            ax.legend()

        output_label.config(text=result)

        for widget in plot_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


input_frame = ttk.Frame(root, padding="10")
input_frame.pack(side=tk.TOP, fill=tk.X)

plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

ttk.Label(input_frame, text="Mean (µ):").grid(row=0, column=0, padx=5, pady=5)
mu_entry = ttk.Entry(input_frame, width=10)
mu_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Standard Deviation (σ):").grid(
    row=0, column=2, padx=5, pady=5)
sigma_entry = ttk.Entry(input_frame, width=10)
sigma_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(input_frame, text="x Value:").grid(row=0, column=4, padx=5, pady=5)
x_entry = ttk.Entry(input_frame, width=10)
x_entry.grid(row=0, column=5, padx=5, pady=5)

ttk.Label(input_frame, text="a Value:").grid(row=1, column=0, padx=5, pady=5)
a_entry = ttk.Entry(input_frame, width=10)
a_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="b Value:").grid(row=1, column=2, padx=5, pady=5)
b_entry = ttk.Entry(input_frame, width=10)
b_entry.grid(row=1, column=3, padx=5, pady=5)

query_combo = ttk.Combobox(input_frame, values=[
    "P(X = x)", "P(X < x)", "P(X > x)", "P(X <= x)", "P(X >= x)", "P(a <= X <= b)", "P(a < X < b)",
    "P(a <= X < b)", "P(a < X <= b)"], state="readonly")
query_combo.set("P(X = x)")
query_combo.grid(row=1, column=4, columnspan=2, padx=5, pady=5)

calculate_button = ttk.Button(
    input_frame, text="Calculate and Plot", command=calculate_and_plot)
calculate_button.grid(row=1, column=6, padx=5, pady=5)

output_label = ttk.Label(root, text="", font=(
    "Helvetica", 14), foreground="#000000")
output_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
