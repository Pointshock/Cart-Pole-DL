# Created by Chris Tomaskovic

# Import the modules for the Cart Pole gym environment
import gym
import random
import time

'''
References:
https://gym.openai.com/envs/CartPole-v1/
Action Space
==================
Number      Action
0           Push cart to the left
1           Push cart to the right

Observation Space
==================
Num     Observation             min     max
0       Cart Position           -4.8    4.8
1       Cart Velocity           -Inf    Inf
2       Pole Angle              -24 deg 24 deg
3       Pole Velocity At Tip    -Inf    Inf

Termination info
The cart x-position (index 0) can be take values between (-4.8, 4.8), 
but the episode terminates if the cart leaves the (-2.4, 2.4) range.

The pole angle can be observed between (-.418, .418) radians (or ±24°), 
but the episode terminates if the pole angle is not in the range (-.2095, .2095) (or ±12°)

'''

# Create our environment that the agent will interact with
env = gym.make('CartPole-v1', render_mode="human")

# Print the observation space for the user
print("Observation Space: ", env.observation_space)

# Print the action space for the user
print("Action Space: ", env.action_space)

# Create an agent that will interact with the environment
# The agent will be able to take action

class Agent():
    # Create a constructor for the agent
    def __init__(self, env):
        # Set the action space for the agent
        self.action_space = env.action_space.n

    # Create a function that will take an action
    def get_action(self, state):
        # Check the length of the state, and make sure it is 4.
        # This is due to the programmers of the gym environment package
        # changing the number of returns from the environment with out telling anyone.
        # This check prevent the program from breaking if the number of returns changes
        if len(state) < 3:
            # If the length of the state is less than 3, then we will print out an error
            print("Error: The state in this step is not the correct length")
            print("The state should be 4, but it is ", len(state))
            print("The state is: ", state)
            # We will then exit exit the step
            return 0
        # Write a simple rule for the agent to follow
        # If the pole is leaning to the left, move left
        # If the pole is leaning to the right, move right
        
        # Get the angle of the pole
        angle = state[2]

        # Print the angle of the pole for the user
        print("Angle: ", angle)

        # If the pole is leaning to the left, move left
        if angle < 0:
            action = 0
        # If the pole is leaning to the right, move right
        elif angle > 0:
            action = 1

        # End agent class and return the action
        return action
    
# Create an instance of the agent
agent = Agent(env)

# We will send the state of the environment to the agent to use for it's observations
# Set the environment to the initial state
state = env.reset()
# Print out the inital state of the environment for the user
print("Initial state: ", state)

# Set the number of time steps. This will determine the number actions
# the agent will take in the environment. The agent can take One action per step.
time_steps = 200
# Loop through the time steps
for each_step in range(time_steps):
    # The agent will take the action, and then the environment will return the next state
    # Print out a header for the user to break up the time steps
    print("\n" * 1)
    print("*" * 50)
    # Print out the time step for the user
    print("Starting the current Time Step: ", each_step, " of ", time_steps)
    # Get the action from the agent
    action = agent.get_action(state)
    # Print out the action to take for the user
    print("Action to take: ", action)
    # Take the action in the environment, and get the next state, reward, terminated, trunicated, and info.
    '''
    state is the next state of the environment based on the action taken in this step.
    
    reward is the reward for taking the action in this step.

    terminated is a boolean value that is True if the agent failed to reach the goal,
    for example if the pole fell over, or the cart went off the track, which is the end of screen,
    This ends the episode

    trunicated is a boolean value that is True if the agent has reached the goal, 
    and False if the agent has not reached the goal. This is good! This means the agent has not failed

    info is a dictionary that contains information about the environment, we will use this later
    '''
    # This is actually where the agent takes the action in the environment
    state, reward, terminated, trunicated, info = env.step(action)

    # Print out the next state of the environment for the user
    print("Next state: ", state)
    # Print out the reward for the user
    print("Reward: ", reward)
    # Print out the terminated value for the user
    print("Terminated: ", terminated)
    # Print out the trunicated value for the user
    print("Trunicated: ", trunicated)
    # Print out the info for the user
    print("Info: ", info)
    # Print out a footer for the user to break up the time steps
    print("*" * 50)
    print("\n" * 1)

    # Render the environment
    env.render()

    time.sleep(.5)

    # Check if the agent has reached passed or failed and end the episode
    if terminated or trunicated:
        # print out a header for the user to make it easier to read
        print("\n" * 2)
        print("=" * 50)
        print("Episode has ended")
        print("This means the agent has either failed (terminated) or passed (turnicated)")
        print("The agent has failed if terminated is True")
        print("The agent has passed if trunicated is True")
        print("State: ", state)
        print("Terminated: ", terminated)
        print("Trunicated: ", trunicated)
        print("Reward: ", reward)
        print("Info: ", info)
        # reset the environment
        state = env.reset()
        print("Resetting the environment")
        print("The evnironment has been reset")
        # Creat a footer for the user to make it easier to read
        print("=" * 50)
        print("\n" * 3)
        # Break the loop and end the episode
        break
