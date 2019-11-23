import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from AbstractCritic import AbstractCritic


class CriticRL(AbstractCritic):
    '''
    TODO:
    Critic Model
    a. Input: a state (e.g. one phase, 81 * 35 vector)
    b. Output: (7,) vector representing the value for each power.
    '''
    def loss(self, predicted_values, n_step_returns):
        """
        Args:
        predicted values - [-1, 7] vector of predicted values for each power
        returns - [n, 7] vector of actual values for each power, 
        where n is the number of steps before return. n = 15

        Returns:
        MSE(predicted, returns + V(t + n))
        - possibly batch here?
        """
        raise NotImplementedError("TODO!")
    