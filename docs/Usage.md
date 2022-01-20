[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
<!--[![LinkedIn][linkedin-shield]][linkedin-url]-->

## About The Project

There is a new viral game called [wordle](https://www.powerlanguage.co.uk/wordle/).
As per usual I was bored and so i decided to try to program an algorithm to solve it for you!


### Built With

* Python version: 3.9 (Tested)
* Python version: 3.x

# Recap on how to build

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Install git and python
  ```
   $ sudo apt-get update
   $ sudo apt-get install git
   $ sudo apt-get install python
  ```

### Installation

Clone the repo with ```$ git clone https://github.com/BizTecBritain/Wordle-Solver.git```

Then enter the directory with ```$ cd Wordle-Solver```

## Usage

First verify you are in the correct directory, if not, run
```
$ cd Wordle-Solver
```

Then to use this code run
```
$ python Wordle-Solver.py
```
1. When the program is running you must first choose a starting word, the words EARTH and YEAST are recommended due their high-frequency letters
2. Then you type in the score that the game gives you where a black letter is zero, a yellow letter is one and a green letter is two (e.g. 01120)
3. The program will then print a word for you to type in
4. DO NOT STOP THE PROGRAM NOW, you must return to step 2 and write in the new code until you have completed the wordle

This program does not guarantee that you will be able to guess the wordle!

[contributors-shield]: https://img.shields.io/github/contributors/BizTecBritain/Wordle-Solver.svg?style=for-the-badge
[contributors-url]: https://github.com/BizTecBritain/Wordle-Solver/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BizTecBritain/Wordle-Solver.svg?style=for-the-badge
[forks-url]: https://github.com/BizTecBritain/Wordle-Solver/network/members
[issues-shield]: https://img.shields.io/github/issues/BizTecBritain/Wordle-Solver.svg?style=for-the-badge
[issues-url]: https://github.com/BizTecBritain/Wordle-Solver/issues
<!--[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/username-->
