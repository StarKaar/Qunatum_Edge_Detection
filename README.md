# 🌌 Quantum Edge Detection

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Qiskit](https://img.shields.io/badge/Qiskit-1.0+-6133BD.svg)](https://qiskit.org/)

A hybrid classical-quantum algorithm utilizing Quantum Image Processing to perform edge detection on classical images. This project demonstrates the integration of classical image preprocessing (via OpenCV and NumPy) with quantum state preparation and execution (via Qiskit), mapping classical pixels to quantum probability amplitudes to identify visual boundaries.

## ✨ Features

* **Hybrid Architecture:** Seamlessly bridges classical image data with quantum probability distributions.
* **Modular Design:** Cleanly separated concerns (image utilities, quantum circuit engine, post-processing) for easy debugging and scientific scalability.
* **Hardware Ready:** Designed to easily switch between local simulator testing and real IBM Quantum hardware execution.
* **Secure Setup:** Built-in configuration structure ensures that personal IBM API tokens remain strictly local and secure.

## 📂 Project Structure

Quantum_Edge_Detection  

├── src  

│   ├── __init__.py         # Package initialization  

│   ├── config.py           # Local configuration and API token management (Git-ignored)  

│   ├── image_utils.py      # OpenCV image padding and classical state-vector math  

│   ├── quantum_engine.py   # Qiskit circuit generation and State Preparation  

│   └── post_process.py     # Probability thresholding and visual boundary mapping  

├── main.py                 # The orchestrator script  

├── requirements.txt        # Environment dependencies  

├── .gitignore              # Security and caching rules  

└── README.md               # Project documentation  

