# Max Profit Algorithm

This project solves the **Max Profit Optimization Problem**, where the goal is to determine the optimal combination of buildings—**Theatre**, **Pub**, and **Commercial Park**—that maximizes total earnings within a given number of time units.

The main constraint is that **only one building can be constructed at a time**, and each building starts generating revenue **only after its construction is completed**.  
A simple and interactive **Streamlit UI** is used to demonstrate the algorithm clearly.

<img width="961" height="673" alt="Maxprofitproblem" src="https://github.com/user-attachments/assets/4c8cfa12-6cd4-400f-9f23-2f1e3d3f1d12" />

Demo : https://max-profit-algorithm.streamlit.app/

---

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

---

## Prerequisites

- Python **3.10+** (Tested on Python 3.12)
- pip (Python package manager)

---

## Installing

### Step 1: Clone the repository

git clone https://github.com/Gopinath-chinnadurai/Max-profit-algorithm.git

### Step 2: Navigate to the project directory
cd Max-profit-algorithm

### Step 3: Install dependencies

pip install streamlit
Virtual environment (venv) is optional for this project.

### Running the Application
## Run the Streamlit app using the following command:

python -m streamlit run app.py
Open your browser and visit:

### How the Project Works
1.User enters the total available time units (n)

2.The algorithm evaluates all valid combinations of:

- Theatre (T)

- Pub (P)

- Commercial Park (C)

3.Each building:

- Has a fixed construction time

- Generates earnings per unit time after construction

4.Parallel construction is not allowed

5.The combination that produces the maximum total profit is displayed

### Example
## Input
Total Time Units: 13

## Output
Theatres (T): 2 | Pubs (P): 0 | Commercial Parks (C): 0
Total Earnings: $16500
### Running the Tests
This project is algorithm-focused and small in scope.
Manual testing is performed using sample inputs from the problem statement.

### Deployment
This project can be deployed using:

- Streamlit Community Cloud

- Any Python-supported server

For interview and demonstration purposes, local execution is sufficient.

### Built With
- Python – Core algorithm logic

- Streamlit – Simple user interface

### Contributing
This project was created as part of an interview assignment and learning exercise.
Contributions are welcome via pull requests.

### Versioning
Semantic Versioning is followed.

- v1.0.0 – Initial implementation with Streamlit UI

### Author
## Gopinath Chinnadurai
GitHub: https://github.com/Gopinath-chinnadurai

### License
This project is intended for educational and demonstration purposes.

### Acknowledgments
- Interview problem inspiration

- Python documentation

- Streamlit documentation
