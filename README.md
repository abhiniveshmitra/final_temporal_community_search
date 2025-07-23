# Intelligent Road Network Community Detection with Gravity-Based Assignment

This repository contains the official source code used in the research paper:

> **S. M. Salam and A. Mitra**, “A Base Algorithm for Intelligent Traffic Management System for Urban Transportation using 6G Network,” 2024 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Guwahati, India, 2024, pp. 1–6.  
> **DOI:** 10.1109/ANTS63515.2024.10898282

**Keywords:**  
- 6G mobile communication  
- Roads  
- Heuristic algorithms  
- Urban areas  
- Transportation  
- Clustering algorithms  
- Traffic control  
- Real-time systems  
- Planning  
- Partitioning algorithms  
- Traffic management  
- Urban transportation network  
- Community detection  
- Dijkstra’s Algorithm  
- Shortest Path Algorithm

> _Note: This repository includes the exact code used to generate the results in the above paper. The author is a co-author of the publication._

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Requirements](#requirements)  
  - [Installation](#installation)  
  - [Usage](#usage)  
- [File Structure](#file-structure)  
- [Citation](#citation)  
- [Contact](#contact)  

---

## Project Overview

This project models urban road networks as graphs and implements a gravity-based community detection algorithm for intelligent traffic management in 6G-enabled cities:

1. **Graph Modeling**  
   - Intersections → nodes  
   - Road segments → edges  

2. **Gravity-Based Assignment**  
   Groups road segments into communities based on traffic density, node weighting, and proximity.

3. **Critical Node Analysis**  
   Computes betweenness centrality to identify ‘bridge’ nodes critical for efficient routing.

4. **Fast Route Planning**  
   Utilizes precomputed metrics combined with Dijkstra’s (or A*) algorithm for rapid, optimal pathfinding.

---

## Features

- 🗺️ **Graph Construction**: Flexible generation of synthetic or real-world road networks.  
- ⚖️ **Gravity Clustering**: Adaptive community detection tuned by traffic flow and spatial distance.  
- 🌉 **Bridge Node Detection**: Identifies chokepoints for targeted traffic alleviation.  
- 🚀 **Optimized Routing**: Near-real-time shortest path queries leveraging preprocessed data.  

---

## Getting Started

### Requirements

- **Python** 3.8+  
- **Libraries**:  
  - `networkx`  
  - `matplotlib` (optional, for visualization)

### Installation

Install the required packages via pip:

```bash
pip install networkx matplotlib
```

### Usage

To reproduce the full workflow as used in the publication, run:

```bash
python Complete_Code.py
```

This single script will:

1. Generate the road network  
2. Detect communities using gravity-based assignment  
3. Compute and store key network metrics  
4. Demonstrate optimized shortest-path calculations  

---

## File Structure

```text
├── Complete_Code.py
├── README.md
├── a_star.py
├── assign_nodes_to_communities.py
├── calculate_gravity_table.py
├── calculate_max_gravity_table.py
├── find_community_bridges.py
├── find_optimal_threshold.py
├── find_shortest_path_with_communities.py
├── generate_synthetic_graph.py
├── main.py
└── plot_graph.py
```

> **Note:**  
> - `Complete_Code.py` is an all-in-one script that amalgamates the functionality from the other modules into a single workflow.  
> - The individual `.py` files contain modular implementations of each step for clarity and potential reuse.

---

## Citation

If you make use of this repository, please cite:

> S. M. Salam and A. Mitra, “A Base Algorithm for Intelligent Traffic Management System for Urban Transportation using 6G Network,” 2024 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS), Guwahati, India, 2024, pp. 1–6, doi: 10.1109/ANTS63515.2024.10898282.

---

## Contact

For research inquiries or collaboration opportunities, please:

- Open an issue on GitHub  
- Email **S. M. Salam** (co-author)  

---

_Run `Complete_Code.py` to replicate all experimental results from the IEEE ANTS 2024 paper._  
