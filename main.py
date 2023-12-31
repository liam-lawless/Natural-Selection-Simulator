"""
File name: main.py
Author(s): Liam Lawless
Date created: November 22, 2023
Last modified: November 26, 2023

Description:
    This script serves as the entry point for the natural selection simulation. It sets up the environment, initializes the simulation agents and food sources, and starts the main application loop.

Dependencies:
    - tkinter: Provides GUI components for the simulation.
    
"""

import tkinter as tk
from controller.simulation import SimulationRunner

# Configuration Constants
BOUNDS = (500, 500)
NUM_AGENTS = 5
NUM_ADVERSARIES = 0
FOOD_AMOUNT = 30
MAX_TICKS = 5000
TICK_RATE = 1  # Milliseconds between ticks
NUM_GENERATIONS = 5  # The total number of generations to simulate
DELAY_BETWEEN_GENERATIONS = 5  # Delay in milliseconds between generations
TRAINING_ENABLED = False

if __name__ == "__main__":
    # Set up the GUI
    root = tk.Tk()
    root.title("Natural Selection Simulation")
    canvas = tk.Canvas(root, width=BOUNDS[0], height=BOUNDS[1], bg='white')
    canvas.pack()

    # Create and run the simulation
    simulation_runner = SimulationRunner(
        root, canvas, BOUNDS, NUM_AGENTS, NUM_ADVERSARIES, FOOD_AMOUNT,
        MAX_TICKS, TICK_RATE, NUM_GENERATIONS, DELAY_BETWEEN_GENERATIONS, TRAINING_ENABLED
    )
    simulation_runner.run()

    # Start the Tkinter event loop
    root.mainloop()

