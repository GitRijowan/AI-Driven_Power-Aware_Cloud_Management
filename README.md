
#AI-Driven Power-Aware Cloud Management System
Overview

This project simulates an intelligent cloud management system that predicts power consumption and dynamically scales virtual machines (VMs) based on workload patterns.

The goal is to demonstrate how machine learning can be used to improve energy efficiency and optimize resource allocation in cloud environments.

Instead of relying on static CPU thresholds, this system uses a predictive AI model to make scaling decisions.

Motivation

Modern data centers consume a significant amount of electricity. Traditional autoscaling methods often react only to CPU utilization, which can lead to:

Over-provisioning (wasting energy and money)

Under-provisioning (performance degradation)

Inefficient power management

This project explores a smarter approach by predicting power consumption first, then scaling resources accordingly.
How to Run

Clone the repository:

git clone https://github.com/yourusername/ai-power-aware-cloud.git
cd ai-power-aware-cloud


Install dependencies:

pip install -r requirements.txt


Run the project:

python main.py


The system will:

Load data

Train the AI model

Run the dynamic scaling simulation

Print scaling decisions in the console
Results

Power prediction accuracy: R² ≈ 0.998

Demonstrated intelligent VM scaling behavior

Prevented uncontrolled scaling by enforcing capacity limits

Simulated realistic cloud resource management decisions
