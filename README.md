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

### pi.py

This code was made from the concept introduced by Buffon and Laplace in which they said if we consider a square and circle inside it and randomly drop needles inside and if we consider the ratio of needle inside the circle to square of a unit circle we can find the value of $\pi$ by taking $\dfrac{r^2}{4r^2}$. So $\pi$ would be 4$\times \dfrac{Needles in circle}{Needles in square}$. More steps considered more accurate the value would be.
