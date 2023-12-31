"""
File name: simulation_view.py
Author(s): Liam Lawless
Date created: November 23, 2023
Last modified: November 25, 2023

Description:
    This file contains the SimulationView class, which handles all the graphical representations of the simulation on the Tkinter canvas.

"""

from view.agent_sensing_view import AgentSensingView
import math

class SimulationView:
    SHOW_SENSING = False

    def __init__(self, canvas, environment):
        self.canvas = canvas
        self.environment = environment
        self.agent_shapes = {}  # Maps agents to their canvas shapes
        self.food_shapes = {}   # Maps Food objects to their canvas shapes
        self.adversary_shapes = {}  # Maps adversaries to their canvas shapes
        self.sensing_view = AgentSensingView(canvas)  # Instantiate once for reusability

    def draw_initial_state(self):
        self.draw_agents()
        self.draw_food()
        self.draw_adversaries()

    def draw_agents(self):
        # Clear existing agents from the canvas
        for shape in self.agent_shapes.values():
            self.canvas.delete(shape)
        self.agent_shapes.clear()

        # Clear existing sensing radii from the canvas
        self.sensing_view.clear_sensing_radii()

        for agent in self.environment.population:
            # Agent's center position
            x, y = agent.position.x, agent.position.y

            # Factor agent size (Agent should be drawn with radius of 5 at smallest size)
            agent_size = (agent.ENTITY_RADIUS - 1) + agent.size

            # If sensing, draw the vision radius first
            if SimulationView.SHOW_SENSING:
                # Calculate the top-left corner of the sensing radius
                sensing_radius = agent.vision * agent.VISION_RANGE_MULTIPLIER
                top_left_x = x - sensing_radius
                top_left_y = y - sensing_radius

                # Convert the agent's heading to a start_angle that corresponds to the canvas orientation
                heading_degrees = math.degrees(agent.heading)

                if agent.is_safe():
                    body_color = 'green'
                else:
                    body_color = 'blue'

                # Draw the sensing radius centered on the agent
                self.sensing_view.create_sensing_radius(
                    int(top_left_x), int(top_left_y),
                    int(sensing_radius * 2), int(sensing_radius * 2),  # width and height
                    heading_angle=30,  # Fixed arc angle for the heading indicator
                    body_fill=body_color, heading_fill="green",
                    body_alpha=0.25, heading_alpha=0.4, start_angle=heading_degrees
                )

            # Draw the agent on top of the radius if necessary
            agent_shape = self.canvas.create_oval(
                x - agent_size, y - agent_size,
                x + agent_size, y + agent_size,
                fill='blue',
                outline=''
            )
            self.agent_shapes[agent] = agent_shape

    def draw_food(self):
        for shape in self.food_shapes.values():
            self.canvas.delete(shape)
        self.food_shapes = {}

        for food_item in self.environment.food:
            x, y = food_item.position.x, food_item.position.y
            shape = self.canvas.create_oval(
                x - food_item.ENTITY_RADIUS, y - food_item.ENTITY_RADIUS,
                x + food_item.ENTITY_RADIUS, y + food_item.ENTITY_RADIUS,
                fill= 'green',
                outline=''
            )
            self.food_shapes[food_item] = shape

    def draw_adversaries(self):
        # Clear existing adversaries from the canvas
        for shape in self.adversary_shapes.values():
            self.canvas.delete(shape)
        self.adversary_shapes.clear()

        for adversary in self.environment.adversaries:
            shape = self.canvas.create_oval(
                adversary.position.x - adversary.ENTITY_RADIUS,
                adversary.position.y - adversary.ENTITY_RADIUS,
                adversary.position.x + adversary.ENTITY_RADIUS,
                adversary.position.y + adversary.ENTITY_RADIUS,
                fill='red',
                outline=''
            )
            self.adversary_shapes[adversary] = shape

    def update_view(self):
        self.draw_agents()
        self.draw_food()
        self.draw_adversaries()

    def clear_canvas(self):
        # Clear existing adversaries from the canvas
        for shape in self.adversary_shapes.values():
            self.canvas.delete(shape)
        self.adversary_shapes.clear()

        # Clear existing food from the canvas
        for shape in self.food_shapes.values():
            self.canvas.delete(shape)
        self.food_shapes = {}

        # Clear existing agents from the canvas
        for shape in self.agent_shapes.values():
            self.canvas.delete(shape)
        self.agent_shapes.clear()
