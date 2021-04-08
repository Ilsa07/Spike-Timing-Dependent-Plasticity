
import numpy as np
import matplotlib.pyplot as plt



# Simulation Parameters
dt = 1          # Euler integration time step
p = 60          # Number of pairings
rep = 1000      # Time between the pairing [ms] = 1 Hz
lag_range = np.linspace(-50, 50, 21)    # Array of Lags for the simulation in steps of 5
dw_range = np.zeros(len(lag_range))     # Array to record the weight changes

# Model Parameters
tau_plus = 10       # Long Term Potentiation Time Constant
tau_minus = 20      # Long Term Depression Time constant
A_plus = 1          # Long Term Potentiation learning rate
A_minus = 1         # Long Term Depression learning rate


for counter, lag in enumerate(lag_range):
    T = rep*(p-1) + 2*abs(lag) + 1  # Spike train totel time length
    pre_spikes = np.zeros(int(T))        # Pre-Synaptic Spike Train
    post_spikes = np.zeros(int(T))       # Post-Synaptic Spike Train

    # Calculate the pre and post-synaptic spiketrain (1 is spike, 0 is no spike)
    pre_spikes[int(lag + abs(lag) + 1): int(lag + abs(lag) + T): rep] = 1
    post_spikes[int(abs(lag) + 1)     : int(abs(lag) + T)      : rep] = 1
    
    x = np.zeros(int(T))    # Presynaptic trace
    y = np.zeros(int(T))    # Postsynaptic trace
    dw = 0                  # Initialise synaptic weight change

    for t in range(int(T)-1):
        x[t+1] = x[t] + dt*(-x[t] + pre_spikes[t])/tau_plus     # Pre-Synaptic trace update
        y[t+1] = y[t] + dt*(-y[t] + post_spikes[t])/tau_minus   # Post-Synaptic trace update
        dw = dw + (A_plus * x[t] * post_spikes[t] - A_minus *y[t] * pre_spikes[t])  # Weight Update
    
    # Append the weight change to the array and increase the index counter
    dw_range[counter] = dw



# Plot the results of the simulation
# **********************************
plt.plot(lag_range, dw_range)
plt.xlabel("Lag: Pre-Spike Time - Post-Spike Time")
plt.ylabel("Weight Change")
plt.title("Simulation Results")
plt.show()