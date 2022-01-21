import numpy as np
import math as m
from Interpreteurtxt import *
import matplotlib.pyplot as plt





def lambd(S,
          I,
          N = Param["population"],        
          beta = Param["transmission"],
          gamma = Param["recuperation"],
        ):
    return beta/N*S*I+gamma*I