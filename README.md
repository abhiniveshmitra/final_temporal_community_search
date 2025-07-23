+++markdown

Intelligent Road Network Community Detection with Gravity-Based Assignment
This repository contains the official source code used in the research paper:

S. M. Salam and A. Mitra, “A Base Algorithm for Intelligent Traffic Management System for Urban Transportation using 6G Network,” 2024 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Guwahati, India, 2024, pp. 1–6.
DOI: 10.1109/ANTS63515.2024.10898282

Keywords: 6G mobile communication · Roads · Heuristic algorithms · Urban areas · Transportation · Clustering algorithms · Traffic control · Real-time systems · Planning · Partitioning algorithms · Traffic management · Urban transportation network · Community detection · Dijkstra’s Algorithm · Shortest path Algorithm

Note: This repository includes the exact code used to generate the results in the above paper. The author is a co-author of the publication.

Table of Contents
Project Overview

Features

Getting Started

Requirements

Installation

Usage

File Structure

Citation

Contact

Project Overview
This project models urban road networks as graphs and implements a gravity-based community detection algorithm for intelligent traffic management in 6G-enabled cities:

Graph Modeling

Intersections → nodes

Road segments → edges

Gravity-Based Assignment

Groups road segments into communities based on traffic density, node weighting, and proximity.

Critical Node Analysis

Computes betweenness centrality to identify ‘bridge’ nodes critical for efficient routing.

Fast Route Planning

Utilizes precomputed metrics combined with Dijkstra’s (or A*) algorithm for rapid, optimal pathfinding.

Features
🗺️ Graph Construction: Flexible generation of synthetic or real-world road networks.

⚖️ Gravity Clustering: Adaptive community detection tuned by traffic flow and spatial distance.

🌉 Bridge Node Detection: Identifies chokepoints for targeted traffic alleviation.

🚀 Optimized Routing: Near-real-time shortest path queries leveraging preprocessed data.

Getting Started
Requirements
Python 3.8+

Libraries: Only standard library modules, plus:

networkx

matplotlib (optional, for visualization)

Installation
Install the required packages via pip:

nginx
Copy
Edit
pip install networkx matplotlib
Usage
All major functions are modularized into separate .py files for clarity. To reproduce the full workflow as used in the publication:

nginx
Copy
Edit
python Complete_Code.py
This single script will:

Generate the road network

Detect communities using gravity-based assignment

Compute and store key network metrics

Demonstrate optimized shortest-path calculations

File Structure
bash
Copy
Edit
├── Complete_Code.py       # Main script orchestrating the full workflow
├── graph_model.py         # Functions for generating and loading road networks
├── gravity_assignment.py  # Implements the gravity-based clustering algorithm
├── centrality_analysis.py # Betweenness centrality and critical node detection
├── routing.py             # Dijkstra’s / A* shortest-path implementations
└── utils.py               # Shared utilities for I/O, logging, and visualization
Citation
If you make use of this repository, please cite:

S. M. Salam and A. Mitra, “A Base Algorithm for Intelligent Traffic Management System for Urban Transportation using 6G Network,” 2024 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Guwahati, India, 2024, pp. 1–6, doi: 10.1109/ANTS63515.2024.10898282.

Contact
For research inquiries or collaboration opportunities, please:

Open an issue on GitHub

Email S. M. Salam (co-author)

This repository provides a fully reproducible implementation of the algorithms presented in the IEEE ANTS 2024 paper. Run Complete_Code.py to replicate all experimental results.
+++
