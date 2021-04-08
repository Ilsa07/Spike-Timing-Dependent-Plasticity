# Spike Timind Dependent Plasticity

### Spike Traces

![pre_synaptic_trace](https://latex.codecogs.com/gif.latex?%5Ctau_&plus;%20%5Cfrac%7Bd%20x%5E%7Bpre%7D%20%7D%7Bdt%7D%3D-x%5E%7Bpre%7D&plus;%5Cdelta%28t-t%5E%7Bpre%7D%29)

![post_synaptic_trace](https://latex.codecogs.com/gif.latex?%5Ctau_-%20%5Cfrac%7Bd%20y%5E%7Bpost%7D%20%7D%7Bdt%7D%3D-y%5E%7Bpost%7D&plus;%5Cdelta%28t-t%5E%7Bpost%7D%29)

### Weight Update

![weight_update](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%7D%7Bdt%7Dw%3DA_&plus;%20x%5E%7Bpre%7D%20%5Cdelta%28t-t%5E%7Bpost%7D%29%20-%20A_-%20y%5E%7Bpost%7D%20%5Cdelta%28t-t%5E%7Bpost%7D%29)

## Getting Started
1. Clone the porject and create a virtual environment
2. Install the packages in the virtual environment
      ```
      pip3 install -r requirements.txt
      ```
