import tkinter as tk
from tkinter import ttk

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("iRacing Fuel Calculator")
        self.root.geometry("500x400")
        
        # Dropdown options
        options = ["Select an Option", "Time Race", "Lap Race"]
        self.dropdown = ttk.Combobox(root, values=options, state="readonly")
        self.dropdown.current(0)  # sets default selected option to index 0
        self.dropdown.pack(pady=5)
        
        # Bind the dropdown to update UI when selection changes
        self.dropdown.bind("<<ComboboxSelected>>", self.on_dropdown_change)
        
        # Create frame for inputs that will contain all our dynamic fields
        self.input_frame = ttk.LabelFrame(root, text="Input Fields")
        self.input_frame.pack(fill="x", expand="no", padx=10, pady=10)
        
        # Create buttons frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill="x", padx=10, pady=5)
        
        # Create Calculate button
        self.process_button = ttk.Button(self.button_frame, text="Calculate", command=self.process_inputs)
        self.process_button.pack(side=tk.RIGHT, padx=5)
        
        # Create Clear button
        self.clear_button = ttk.Button(self.button_frame, text="Clear Output", command=self.clear_all)
        self.clear_button.pack(side=tk.RIGHT, padx=5)
        
        # Create output area
        self.output_frame = ttk.LabelFrame(root, text="Output")
        self.output_frame.pack(fill="both", expand="yes", padx=10, pady=10)
        
        self.output_text = tk.Text(self.output_frame, wrap=tk.WORD, width=50, height=10)
        self.output_text.pack(fill="both", expand="yes", padx=5, pady=5)
        
        # Add a scrollbar to the output
        scrollbar = tk.Scrollbar(self.output_text, command=self.output_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.config(yscrollcommand=scrollbar.set)
        
        # Dictionary to store entry widgets
        self.entries = {}
        
        # Initialize with default UI (dropdown set to "Select an Option")
        self.on_dropdown_change()
    
    def on_dropdown_change(self, event=None):
        """Event handler for dropdown selection change"""
        # Clear all widgets from the input frame
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        # Clear the entries dictionary
        self.entries.clear()
        
        current_selection = self.dropdown.current()
        
        if current_selection == 0:
            # "Select an Option" - Show message
            label = ttk.Label(self.input_frame, text="Please select a race type from the dropdown above.")
            label.pack(padx=10, pady=20)
            
        elif current_selection == 1:
            # "Time Race" option
            self.create_time_race_inputs()
            
        elif current_selection == 2:
            # "Lap Race" option
            self.create_lap_race_inputs()
    
    def create_time_race_inputs(self):
        """Create input fields for Time Race option"""
        # First input field
        ttk.Label(self.input_frame, text="Race Length (minutes):").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.entries['raceLength'] = ttk.Entry(self.input_frame, width=40)
        self.entries['raceLength'].grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        # Second input field
        ttk.Label(self.input_frame, text="Fuel used per lap:").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.entries['fuelPerLap'] = ttk.Entry(self.input_frame, width=40)
        self.entries['fuelPerLap'].grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        
        # Third input field
        ttk.Label(self.input_frame, text="Lap Time (minutes):").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.entries['lapTimeMin'] = ttk.Entry(self.input_frame, width=40)
        self.entries['lapTimeMin'].grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        
        # Fourth input field
        ttk.Label(self.input_frame, text="Lap Time (seconds):").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.entries['lapTimeSec'] = ttk.Entry(self.input_frame, width=40)
        self.entries['lapTimeSec'].grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        # Fifth input field
        ttk.Label(self.input_frame, text="Fuel Tank Size:").grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.entries['tanksize'] = ttk.Entry(self.input_frame, width=40)
        self.entries['tanksize'].grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
        
        # Sixth input field
        ttk.Label(self.input_frame, text="Tank Restrictions (%):").grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        self.entries['tankRestrict'] = ttk.Entry(self.input_frame, width=40)
        self.entries['tankRestrict'].grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)
    
    def create_lap_race_inputs(self):
        """Create input fields for Lap Race option"""
        # First input field
        ttk.Label(self.input_frame, text="Number of Laps:").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.entries['numLaps'] = ttk.Entry(self.input_frame, width=40)
        self.entries['numLaps'].grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        # Second input field
        ttk.Label(self.input_frame, text="Fuel per Lap:").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.entries['fuelPerLap'] = ttk.Entry(self.input_frame, width=40)
        self.entries['fuelPerLap'].grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        
        # Third input field
        ttk.Label(self.input_frame, text="Safety Margin (%):").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.entries['safetyMargin'] = ttk.Entry(self.input_frame, width=40)
        self.entries['safetyMargin'].grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        # Fourth input field
        ttk.Label(self.input_frame, text="Fuel Tank Size:").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.entries['tanksize'] = ttk.Entry(self.input_frame, width=40)
        self.entries['tanksize'].grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        
        # Fifth input field
        ttk.Label(self.input_frame, text="Tank Restrictions (%):").grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.entries['tankRestrict'] = ttk.Entry(self.input_frame, width=40)
        self.entries['tankRestrict'].grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
    
    def process_inputs(self):
        """Process the inputs and display in the output area"""
        current_selection = self.dropdown.current()
        
        if current_selection == 0:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Please select a race type first.")
            return
        
        try:
            if current_selection == 1:  # Time Race
                # Get values from entries
                raceLength = float(self.entries['raceLength'].get())
                fuelPerLap = float(self.entries['fuelPerLap'].get())
                lapTimeMin = float(self.entries['lapTimeMin'].get())
                lapTimeSec = float(self.entries['lapTimeSec'].get())
                tankSize = float(self.entries['tanksize'].get())
                restrict = float(self.entries['tankRestrict'].get())
                
                # Calculate lap time in minutes
                lapTimeTotal = lapTimeMin + (lapTimeSec / 60)
                
                # Calculate number of laps
                numLaps = raceLength / lapTimeTotal
                
                # Calculate fuel needed
                fuelNeeded = numLaps * fuelPerLap

                # Max Fuel with restriction
                maxLoad = tankSize * restrict/100
                
                # Display results
                result = f"Time Race Analysis:\n"
                result += f"Race Length: {raceLength} minutes\n"
                result += f"Lap Time: {lapTimeMin}m {lapTimeSec}s ({lapTimeTotal:.2f} minutes)\n"
                result += f"Estimated Number of Laps: {numLaps:.2f}\n"
                result += f"Fuel Needed: {fuelNeeded:.2f} gal\n"
                result += f"Max Fuel Load: {maxLoad:.2f} gal\n"
                
                
                
            elif current_selection == 2:  # Lap Race
                # Get values from entries
                numLaps = float(self.entries['numLaps'].get())
                fuelPerLap = float(self.entries['fuelPerLap'].get())
                safetyMargin = float(self.entries['safetyMargin'].get())
                tankSize = float(self.entries['tanksize'].get())
                restrict = float(self.entries['tankRestrict'].get())
                
                # Calculate fuel needed with safety margin
                baseFuel = numLaps * fuelPerLap
                fuelNeeded = baseFuel * (1 + safetyMargin/100)

                maxLoad = tankSize * restrict/100
                
                # Display results
                result = f"Lap Race Analysis:\n"
                result += f"Number of Laps: {numLaps}\n"
                result += f"Fuel per Lap: {fuelPerLap} gal\n"
                result += f"Base Fuel Required: {baseFuel:.2f} gal\n"
                result += f"Max Fuel Load: {maxLoad:.2f} gal\n"
                
            
            # Update output
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, result)
            
        except ValueError:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Error: Please enter valid numbers in all fields.")
        except KeyError:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Error: Missing input fields.")
    
    def clear_all(self):
        """Clear all input fields and output text"""
        # Clear output
        self.output_text.delete(1.0, tk.END)
        
        # Clear input fields
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Create the main application
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUI(root)
    root.mainloop()
    main()