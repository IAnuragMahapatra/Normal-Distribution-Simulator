# Normal Distribution Simulator

This application is a simple simulator for visualizing and calculating probabilities related to the normal distribution using Python's Tkinter, NumPy, SciPy, and Matplotlib libraries.

## Features

- Input mean (µ) and standard deviation (σ) to define the normal distribution.
- Calculate probabilities for:
  - A specific x value: P(X = x)
  - Cumulative probabilities: P(X < x), P(X <= x)
  - Tail probabilities: P(X > x), P(X >= x)
  - Probabilities for ranges: P(a <= X <= b), P(a < X < b), etc.
- Visualize the normal distribution curve with shaded areas representing the calculated probabilities.

## Requirements

To run this application, you need the following Python libraries:

- Tkinter (included with standard Python installations)
- NumPy
- SciPy
- Matplotlib

You can install the required libraries using pip:

```bash
pip install numpy scipy matplotlib
```

## Usage

1. **Input Parameters**: Enter the mean (µ) and standard deviation (σ) in their respective fields.
2. **Select Query Type**: Choose the type of probability query from the dropdown menu.
3. **Input Values**: Depending on the selected query, input the necessary values (x, a, b).
4. **Calculate**: Click the "Calculate and Plot" button to compute the probability and visualize the normal distribution.

## Code Structure

The main components of the code include:

- **Input Frame**: This section collects user inputs for mean, standard deviation, x value, and range values (a and b).
- **Plotting**: Utilizes Matplotlib to plot the normal distribution based on user-defined parameters.
- **Probability Calculation**: Uses SciPy's `norm` module to compute various probabilities based on the user’s input.
- **Error Handling**: Displays error messages for invalid inputs using Tkinter's messagebox.

## Example

To calculate the probability of a value \( x \) given a mean of 155 and a standard deviation of 15:

- Input **Mean (µ)**: `155`
- Input **Standard Deviation (σ)**: `15`
- Select **P(X >= x)** from the dropdown.
- Input **x Value**: `170`
- Click **Calculate and Plot**.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- Inspired by the need for educational tools in statistics.
- Uses libraries: [NumPy](https://numpy.org/), [SciPy](https://www.scipy.org/), [Matplotlib](https://matplotlib.org/) for calculations and plotting.
