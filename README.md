Intelligent Road Network Community Detection with Gravity-Based Assignment
This repository contains the official source code used in the research paper:

S. M. Salam and A. Mitra, "A Base Algorithm for Intelligent Traffic Management System for Urban Transportation using 6G Network," 2024 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Guwahati, India, 2024, pp. 1-6, doi: 10.1109/ANTS63515.2024.10898282.

Keywords: {6G mobile communication; Roads; Heuristic algorithms; Urban areas; Transportation; Clustering algorithms; Traffic control; Real-time systems; Planning; Partitioning algorithms; Traffic management; Urban transportation network; Community detection; 6G Network; Dijkstra’s Algorithm; Shortest path Algorithm}

Note: This repository includes the exact code used to generate the results in the above paper. I am a co-author of the publication.

Project Overview
This project models urban road networks as graphs and implements a gravity-based community detection algorithm for intelligent traffic management, leveraging the advancements of 6G networks.

Graph Modeling: Intersections and road segments as nodes and edges.

Gravity-Based Assignment: Road segments are grouped into communities based on traffic density, node weighting, and proximity.

Critical Node Analysis: Calculates betweenness centrality to find bridge nodes that are key to efficient route planning.

Fast Route Planning: Uses precomputed metrics with Dijkstra's (or A*) algorithm for quick, optimal path finding.

Getting Started
Requirements
Python 3.8+

No requirements.txt is needed. This repository uses only standard library modules, plus networkx and (optionally) matplotlib for graph visualization.

You can install these packages with:

pip install networkx matplotlib

Usage
All major functions are organized in separate .py files for clarity and modularity.

To run the complete workflow (as used in the publication), simply execute:

python Complete_Code.py

This script:

Generates the road network

Detects communities with gravity-based assignment

Computes and stores key metrics

Demonstrates optimized shortest path calculation

File Structure
Individual algorithm components are in separate Python files for easy inspection and modification.

All steps can be run in sequence with Complete_Code.py.

Citation
If you use this repository, please cite as follows:

S. M. Salam and A. Mitra, "A Base Algorithm for Intelligent Traffic Management System for Urban Transportation using 6G Network," 2024 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Guwahati, India, 2024, pp. 1-6, doi: 10.1109/ANTS63515.2024.10898282.

Contact
For research questions or collaborations, please open a GitHub issue or contact S. M. Salam (co-author).

This is the reproducible source code underpinning the above IEEE publication. Anyone may reproduce all paper results by running Complete_Code.py.
