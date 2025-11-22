import tkinter as tk

# FUNCTIONS
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_results_label.config(text=str(km))


# OBJECTS
window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

# Create the miles input
miles_input = tk.Entry(width=7)
miles_input.grid(column=1,row=0)

# Simple label to display Miles
miles_label = tk.Label(text="Miles")
miles_label.grid(column=2,row=0)

# Simple label to display is equal to
is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

# Label which will display the calculated result from miles to km
km_results_label = tk.Label(text="0")
km_results_label.grid(column=1,row=1)

# Simple label to display Kilometers
km_label = tk.Label(text="km")
km_label.grid(column=2,row=1)

# Button which will convert the miles to km
calculate_button = tk.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1,row=2)



window.mainloop()