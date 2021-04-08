# Spike Timind Dependent Plasticity (STDP)
This project simulates STDP, which is a model for how weights between neurons change depending on the timing of the pre and post-synaptic spikes. If a pre-synaptic spike occurs before a post-synaptic one the weight that connects the two increases, and if it is the other way around it decreases. STDP explains how the brain can predict sequences and how we can respond to earlier stimulus. The simulation plots the weight changes for different lags, which are the timing difference between the pre and post-synaptic spikes.

### Spike Traces
For this model it is assumed that both pre and post-synaptic spikes leave a trace, which follows the following equations:

![pre_synaptic_trace](https://latex.codecogs.com/gif.latex?%5Ctau_&plus;%20%5Cfrac%7Bd%20x%5E%7Bpre%7D%20%7D%7Bdt%7D%3D-x%5E%7Bpre%7D&plus;%5Cdelta%28t-t%5E%7Bpre%7D%29)

![post_synaptic_trace](https://latex.codecogs.com/gif.latex?%5Ctau_-%20%5Cfrac%7Bd%20y%5E%7Bpost%7D%20%7D%7Bdt%7D%3D-y%5E%7Bpost%7D&plus;%5Cdelta%28t-t%5E%7Bpost%7D%29)

### Weight Update
The weight change of the synapse is modelled by the following equation:

![weight_update](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%7D%7Bdt%7Dw%3DA_&plus;%20x%5E%7Bpre%7D%20%5Cdelta%28t-t%5E%7Bpost%7D%29%20-%20A_-%20y%5E%7Bpost%7D%20%5Cdelta%28t-t%5E%7Bpost%7D%29)

## Getting Started
1. Clone the porject and create a virtual environment
2. Install the packages in the virtual environment
      ```
      pip3 install -r requirements.txt
      ```
