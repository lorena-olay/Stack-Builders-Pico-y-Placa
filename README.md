# Stack-Builders-Pico-y-Placa

This project is a Python application that predicts whether a vehicle is allowed to drive in Bogotá, Colombia, on a given date and time based on the Pico y Placa driving restriction policy.

## About Pico y Placa

Pico y Placa (Peak and Plate) is a driving restriction policy aimed at mitigating traffic congestion. It was first implemented in Bogotá, Colombia, in 1998. The policy restricts vehicles with license plate numbers ending in certain digits from accessing predetermined urban areas during peak hours on specific days.

# Prerequisites

You need to have Python 3 installed on your machine to run this project. You can download it from [here](https://www.python.org/downloads/).


# Getting Started

First, clone this repository to your local machine using git clone.

```sh
git clone https://github.com/lorena-olay/pico_y_placa.git
cd pico_y_placa
```

# Usage

The main Python file of the project is `main.py`. To run the program, open your command line or terminal and navigate to the project directory. Then, run the following command:

```sh
python main.py
```

The program will ask you to enter a plate number and a date and time (in the format dd/mm/yyyy hh:mm). It will then tell you whether a car with the given plate number can be on the road at the given date and time based on the Pico y Placa policy.

# Running the Tests

Unit tests are written for each of the components (plate_validator.py, pico_y_placa_checker.py, and main.py) in the test directory. To run the tests, navigate to the project directory and run the following command:

```sh
python -m unittest discover test
```
This will automatically discover and run all the tests in the test directory.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.