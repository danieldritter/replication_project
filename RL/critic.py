import numpy as np
import tensorflow as tf
from tensorflow.keras import Model

class Critic(Model):
    '''
    TODO:
    Critic Model
    a. Input: a state (e.g. one phase, 81 * 35 vector)
    b. Output: (7,) vector representing the value for each power.
    '''

    def __init__(self):
        '''
        Initialization for Critic Model

        Args:
        
        '''

        super(Critic, self).__init__()

        

    def call(self, states):
        '''
        Call method for critic

        Args:
        states - [-1, state_size] vector where state_size = 81*35
        
        Returns:
        [-1, 7] vector of the values for each power in each state.
        '''
        pass

    def loss(self, predicted_values, n_step_returns):
        """
        Args:
        predicted values - [-1, 7] vector of predicted values for each power
        returns - [n, 7] vector of actual values for each power, 
        where n is the number of steps before return. n = 15
        
        Returns:
        MSE(predicted, returns + V(t + n))
        """
        pass
    