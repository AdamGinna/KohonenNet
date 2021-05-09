# Kohonen SOM
It is Deep Learning project visualizes training process of self-organizing map
(SOM) on a two-dimensional data set.
## Requirements
* numpy
* pygame
## Theory 
SOM is recursive neural network which can be present as a graph in n-dimensional space. Traning this network is about changing position of vertex based on training data. Change are started from the nearest neighbour to its neighbour, . 
The update formula for a neuron v with weight vector W<sub>v</sub>(s) is

<img src="https://latex.codecogs.com/png.image?\dpi{100}&space;W_{v}(s&plus;1)=W_{v}(s)&plus;\theta&space;(u,v)\cdot&space;\alpha&space;(s)\cdot&space;(Data(t)-W_{v}(s))" title="W_{v}(s+1)=W_{v}(s)+\theta (u,v)\cdot \alpha (s)\cdot (Data(t)-W_{v}(s))" />

Where <img src="https://latex.codecogs.com/png.image?\dpi{100}&space;\inline&space;\alpha&space;(s)=&space;\alpha_{0}&space;*&space;exp(\frac{-s}{allSteps})" title="\inline \alpha (s)= \alpha_{0} * exp(\frac{-s}{allSteps})" /> 
and <img src="https://latex.codecogs.com/png.image?\dpi{100}&space;\theta&space;(u,v)=exp(\frac{-|u-v|}{2\sigma^2})" title="\theta (u,v)=exp(\frac{-|u-v|}{2\sigma^2})" /> 

## Start 

```python DeepLearnig.py```

If you want specify hyperparameters: alpha0 and sigma use:

```python DeepLearnig.py 0.6 0.8```

Also it is possible to declare size of map using up and down button. Then click `run` button and see 400 animation frames of learnig network.  
