# CurvBasedRWNNPrune

## About
This repository contains the codes and data associated with the following manuscript: <br>

Pavithra Elumalai#, Sudharsan Vijayaraghavan#, Madhumita Mondal*, and Areejit Samal*, [<i>Application of discrete Ricci curvature in pruning randomly wired neural networks: 
A case study with chest x-ray classification of COVID-19</i>](link of the article). <br>
(# Equally contributed, * Corresponding authors)
<br>

## Required packages:
1. tensorboardX
2. pot
3. torchvision
4. ptflops
5. networkx
6. matplotlib
7. igraph
### Custom packages from github to allow RandWire to work, and FLOPs counter to work
1. git+https://github.com/JiaminRen/CVdevKit.git
2. git+git://github.com/sovrasov/flops-counter.pytorch.git@64d38fd47cb0795437056745c64a987d944c1885


The repository contains five folders. A brief description of each is provided below.

## Codes
Contains all the necessary codes to reproduce the results in the manuscript.

1. utils (folder): Contains codes to creat the configuration of networks.

2. Data_prep.ipynb: Preprocess the raw chest X-ray images for training and testing. The code is implemented in Python and executed on <i>Google Colab</i>.

3. Small_Regime_WS.ipynb: Main code for creating RWNNs based on the Watts–Strogatz (WS) model, with pruning implemented using three edge-centric network measures: 
Forman–Ricci curvature (FRC), Ollivier–Ricci curvature (ORC), and Edge Betweenness Centrality (EBC).
The same code can also generate Erdős–Rényi (ER) and Barabási–Albert (BA) models by simply changing the graph model parameter. 
The code is implemented in Python and executed on <i>Google Colab</i>.

4. Plot_Before&AfterPrune.ipynb: Code to generate box plots for six performance measures (Accuracy, Specificity, Sensitivity, AUC-ROC, Precision, and F1-score), 
comparing results before pruning and after pruning using three edge-centric network measures: FRC, ORC, and EBC.

5. Plot_Pruned_Performance.ipynb: Code to generate box plots for compression ratio and theoretical speedup, comparing results after pruning with the three edge-centric 
network measures: FRC, ORC, and EBC.

6. Plot_Networkmeasures.ipynb: Code to generate box plots for modularity and global efficiency of the random network, comparing results before pruning and after pruning 
based on FRC, ORC, and EBC


## Covid_data
Contains the training (train) and testing (test) chest X-ray images of COVID-19. The data is downloaded from the [*COVID-XRay-5K*](https://github.com/shervinmin/DeepCovid) dataset.

## PRUNING
Contains two folders: UNPRUNED and PRUNED.

1. UNPRUNED: Results before pruning 
2. PRUNED: Results after pruning

## Outputs
Contains all the necessary data to generate the figures in the manuscript.

## Figures
Contains all the figures present in the manuscript (can be generated as well from the given code)

## Citation
In case you use the codes herein, please cite the following manuscript:

Pavithra Elumalai, Sudharsan Vijayaraghavan, Madhumita Mondal, and Areejit Samal, [<i>Application of discrete Ricci curvature in pruning randomly wired neural networks: 
A case study with chest x-ray classification of COVID-19</i>](link of the article).