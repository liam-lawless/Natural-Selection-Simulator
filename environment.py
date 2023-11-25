"""
File name: environment.py
Author(s): Liam Lawless
Date created: November 13, 2023
Last modified: November 24, 2023

Description:
    The environment.py file defines the Environment class, which manages the simulation space, orchestrates agent interactions, and maintains the overall state of the natural selection simulation.

Dependencies:

"""

class Environment:
    def __init__(self, population, adversaries, food, bounds):
        self.population = population
        self.adversaries = adversaries
        self.food = food
        self.bounds = bounds

    def update_environment(self):
        # Update agents
        for agent in self.population:
            if agent.energy > 0:
                agent.perform_action(self)

        # Check for agent-food collisions
        self.check_for_collisions()

        # Update adversaries
        for adversary in self.adversaries:
            adversary.seek_agents(self.population)

        # Check for agent-adversary collisions
        self.check_for_predation()

    def check_for_collisions(self):
        for agent in self.population:
            for food_item in self.food[:]:  # Copy the list to avoid modification during iteration
                agent_size = agent.ENTITY_RADIUS + agent.size # Factor in agent size

                if agent.position.distance_to(food_item.position) <= agent_size + food_item.ENTITY_RADIUS:
                    agent.consume_food()
                    self.remove_food(food_item)

    def check_for_predation(self):
        for adversary in self.adversaries:
            for agent in self.population[:]:  # Copy to avoid modification during iteration
                if adversary.position.distance_to(agent.position) <= adversary.ENTITY_RADIUS + agent.ENTITY_RADIUS:
                    # Handle the agent being eaten by the adversary
                    self.remove_agent(agent)

    def remove_food(self, food_item):
        self.food.remove(food_item)

    def remove_agent(self, agent):
        # Remove the agent from the population
        self.population.remove(agent)
