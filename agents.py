from swarm import Agent
from swarm.repl import run_demo_loop


host_agent = Agent(
    name="Host Agent",
    instructions="Determine if the user wants to buy or rent a car and then transfer the conversation to the appropriate agent.",
)

car_rent_agent = Agent(
    name="Car Rent Agent",
    instructions="Assist the user with renting a car for a specified period. Provide information about different car models available for rent, rental prices, and terms in the USA.",
    functions=[],
)
cars_sales_agent = Agent(
    name="Cars Sales Agent",
    instructions="Assist the user with purchasing a car. Provide information about different car models, prices, and financing options available in the USA.",
    functions=[],
)

def transfer_back_to_host():
    """Call this function to transfer the conversation back to the host agent."""
    return host_agent

def transfer_to_rent():
    return car_rent_agent

def transfer_to_sales():
    return cars_sales_agent


host_agent.functions = [transfer_to_sales, transfer_to_rent, ]
car_rent_agent.functions.append(transfer_back_to_host)
cars_sales_agent.functions.append(transfer_back_to_host)


if __name__ == "__main__":
    # Run the demo loop
    run_demo_loop(host_agent, debug=False)