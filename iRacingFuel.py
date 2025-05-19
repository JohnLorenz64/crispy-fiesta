import tkinter as tk
from tkinter import ttk

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("iRacing Fuel Calculator")
        self.root.geometry("500x400")
        
        # Create frame for inputs
        input_frame = ttk.LabelFrame(root, text="Input Fields")
        input_frame.pack(fill="x", expand="no", padx=10, pady=10)
        
        # First input field
        ttk.Label(input_frame, text="Race Length (minutes):").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.input1 = ttk.Entry(input_frame, width=40)
        self.input1.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        # Second input field
        ttk.Label(input_frame, text="Fuel used per lap:").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.input2 = ttk.Entry(input_frame, width=40)
        self.input2.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        # Third input field
        ttk.Label(input_frame, text="Lap Time (minutes):").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.input3 = ttk.Entry(input_frame, width=40)
        self.input3.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        # Forth input field
        ttk.Label(input_frame, text="Lap Time (seconds):").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.input4 = ttk.Entry(input_frame, width=40)
        self.input4.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

        # Fifth input field
        ttk.Label(input_frame, text="Tank Restrictions:").grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        self.input5 = ttk.Entry(input_frame, width=40)
        self.input5.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)
        
        # Process button
        self.process_button = ttk.Button(input_frame, text="Calculate", command=self.process_inputs)
        self.process_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
        
        # Clear button
        self.clear_button = ttk.Button(input_frame, text="Clear Output", command=self.clear_all)
        self.clear_button.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
        
        # Output area
        output_frame = ttk.LabelFrame(root, text="Output")
        output_frame.pack(fill="both", expand="yes", padx=10, pady=10)
        
        self.output_text = tk.Text(output_frame, wrap=tk.WORD, width=50, height=10)
        self.output_text.pack(fill="both", expand="yes", padx=5, pady=5)
        
        # Add a scrollbar to the output
        scrollbar = ttk.Scrollbar(self.output_text, command=self.output_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.config(yscrollcommand=scrollbar.set)
        

    # putting the calcs in here    
    def process_inputs(self):
        """Process the inputs and display in the output area"""
        raceLength = float(self.input1.get())
        fuelPerLap = float(self.input2.get())
        lapTimeMin = float(self.input3.get())
        lapTimeSec = float(self.input4.get())
        restrict = float(self.input5.get())

        #gr86 cup tank size 22 gal
        tank = 22    

        laptime = round(lapTimeMin + lapTimeSec / 60, 3)
        laps = round(raceLength / laptime, 2)
        totalFuel = round(laps * fuelPerLap, 2)
        qualiFuel = round(fuelPerLap * 3, 2)
        restrictSize = round(22 * restrict, 2)
        

        outputMessage = f"Laps: {laps} \nRace Fuel: {totalFuel} gal \nQualifying Fuel: {qualiFuel} gal \nMax Fuel Load: {restrictSize} gal \n"
        self.output_text.insert(tk.END, outputMessage)
        
        
        
    def clear_all(self):
        """Clear all inputs and output"""
        self.input1.delete(0, tk.END)
        self.input2.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = SimpleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()