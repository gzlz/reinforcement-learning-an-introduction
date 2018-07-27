#######################################################################
# Copyright (C)                                                       #
# 2018 Oscar González Herraiz(osgohe@gmail.com)                       #                             #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

# maximum gambler capital
MAX_CAPITAL = 100

# current policy
policy = np.zeros(MAX_CAPITAL + 1)

# current state value
state_values = np.zeros(MAX_CAPITAL + 1)

# final state
state_values[MAX_CAPITAL]=1

# all possible states
states = np.arange(MAX_CAPITAL + 1)

# heads probability
heads_probability = 0.4



# @state: [gambler capital]
# @action: gambler stake 
# @state_value: state value array
def expected_return(state, action, state_value):  
    returns = 0.0 
    for head in (True,False): 
        if head:
            returns += heads_probability * (state_values[state + action])
        else:
            returns += (1-heads_probability) * (state_values[state - action]) 
    return returns


iteration = 0

while True:
     
        iteration += 1
    
        for s in states[1:MAX_CAPITAL]:
            
            delta = 0.0
            action_returns = []
            actions = np.arange(min(s, MAX_CAPITAL - s) + 1)
            
            # go through all posible actions          
            for action in actions:
                    action_returns.append(expected_return(s, action, state_values))
               
            best_action = np.argmax(action_returns)
            policy[s] = actions[best_action]
            new_value = np.max(action_returns)
            delta += np.abs(state_values[s] - new_value)
            state_values[s] = new_value

               
        if delta < 1e-9:    
            plt.figure(1)
            plt.xlabel('Capital')
            plt.ylabel('Value estimates')
            plt.plot(state_values)
            plt.figure(2)
            plt.scatter(states, policy)
            plt.xlabel('Capital')
            plt.ylabel('Final policy (stake)')
            plt.show()
            
            break

        







