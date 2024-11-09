# Agents Playground

A Python project demonstrating multi-agent conversations using the OpenAI Swarm Framework. This playground simulates a car dealership scenario where agents can help users with purchasing or renting vehicles in the USA.

## Features
- Host agent that routes conversations
- Car sales agent for vehicle purchases
- Car rental agent for temporary rentals
- Seamless conversation transfers between agents

## Setup

1. **Set OpenAI API Key:**

```bash
export OPENAI_API_KEY='your-api-key-here'
```

2. **Create a virtual environment:**

```bash
python -m venv venv
```

3. **Activate the virtual environment:**

```bash
source venv/bin/activate
```

4. **Install dependencies:**

```bash
pip install git+ssh://git@github.com/openai/swarm.git
```

## Running the Project

To start the podcast agents system:

```bash
python agents.py
```   

## Credits

This project uses code from [OpenAI Swarm](https://github.com/openai/swarm), licensed under the [MIT License](LICENSE).