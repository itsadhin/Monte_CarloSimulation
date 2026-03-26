# MonteCarlo Simulation

The objective for making this repo is to understand how Montecarlo simulation works by understanding it from its basis form

---

## Cloning the repository
```
git clone https://github.com/itsadhin/MonteCarlo_Simulation
cd MonteCarlo_Simulation/
```
### Installing required packages
#### Linux or MacOS
```
python -m venv venv
source venv/bin/activate
pip install -r packages.txt
```

#### Windows
##### If using Command Prompt(cmd)
```
python -m venv venv
venv\Scripts\activate
pip install -r packages.txt
```
##### If using PowerShell
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r packages.txt
```
---

## Code
### distance.py

This code considers a unit square and takes two random points on it then the calucaltes the distance between it for n steps and calculates the average for it.

