# python-week-5-assignment
Vehicle Movement Simulator

A PyGame application that demonstrates object-oriented programming (OOP) concepts through a visual simulation of different vehicle types moving in their respective environments.

Features

· Multiple Vehicle Types: Cars, airplanes, and boats with unique movement patterns
· Polymorphism in Action: Each vehicle implements the move() method differently
· Interactive Interface: Add vehicles, clear the screen, and select vehicles to view information
· Visual Effects: Realistic movement effects like contrails, wakes, and exhaust
· Clean UI: Intuitive buttons and information display

OOP Concepts Demonstrated

1. Inheritance: All vehicle types inherit from a base Vehicle class
2. Polymorphism: Each vehicle implements the move() method differently
3. Encapsulation: Classes encapsulate their own data and behavior
4. Abstraction: The base class defines the interface that all vehicles must implement

Requirements

· Python 3.x
· PyGame library

Installation

1. Ensure you have Python installed on your system
2. Install PyGame using pip:
  
   pip install pygame
   
3. Download or clone this repository
4. Run the script:
  
   python vehicle_simulator.py
   
How to Use

1. Run the application: Execute the Python script to start the simulation
2. Add vehicles: Use the buttons at the top to add cars, airplanes, or boats
3. Select vehicles: Click on any vehicle to view its information
4. Clear the screen: Use the "Clear All" button to remove all vehicles
5. Observe movement: Each vehicle type moves differently according to its environment

Vehicle Types

Cars

· Move along the road
· Have realistic wheels and body
· Produce exhaust effects when moving

Airplanes

· Fly through the sky with slight vertical movement
· Have wings, tail, and windows
· Leave contrails behind them

Boats

· Float on water with gentle rocking motion
· Feature sails, masts, and cabins
· Create wake effects in the water

Code Structure

· Vehicle: Base class with common attributes and methods
· Car, Airplane, Boat: Specialized vehicle classes that inherit from Vehicle
· Button: UI component for interactive controls
· Main game loop: Handles drawing, updates, and user input

Extending the Project

You can easily add new vehicle types by:

1. Creating a new class that inherits from Vehicle
2. Implementing the move() method with unique movement logic
3. Implementing the draw() method with custom visuals
4. Adding a button to create instances of your new vehicle type

License

This project is open source and available under the MIT License.
