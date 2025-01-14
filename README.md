# Black-Scholes Stock Analysis

## Project Description
This project implements the Black-Scholes model to analyze stock performance for major companies such as Apple, Microsoft, and Amazon. It calculates key financial metrics, including the rate of return, volatility, and expected future prices. The analysis also estimates probabilities of price changes over specific periods, providing insights into stock trends and risk factors.

## Features
- **Stock Data Analysis**:
  - Retrieves historical stock data using Yahoo Finance.
  - Calculates the rate of return (`r`) and volatility (`s²`) of stocks.
  - Predicts expected stock prices for future dates.
- **Probability Estimation**:
  - Estimates the probability of a stock reaching a certain price by specific dates (e.g., 2020, 2022).
- **Black-Scholes Parameters**:
  - Implements Black-Scholes parameters for options pricing analysis.

## Motivation
This project was developed as part of an academic exercise to explore financial modeling and statistical analysis using Python. It highlights the use of the Black-Scholes model and other statistical methods in analyzing stock market trends and making predictions.

## Included Files
- `Black_Scholes.py`: Python script implementing the stock analysis and Black-Scholes model.

## Requirements
- Python 3.6 or higher.
- Libraries:
  - NumPy
  - SciPy
  - Matplotlib
  - pandas
  - pandas-datareader

Install dependencies:
```bash
pip install numpy scipy matplotlib pandas pandas-datareader
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/rmodregoe/black-scholes-stock-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd black-scholes-stock-analysis
   ```
3. Run the script:
   ```bash
   python Black_Scholes.py
   ```

## Results
The script provides:
1. Financial metrics for Apple, Microsoft, and Amazon stocks, including:
   - Rate of return (`r`).
   - Volatility (`s²`).
   - Expected stock price in 2020.
   - Probabilities of price increases by 2020 and 2022.
2. Black-Scholes parameters for Microsoft stock between 2018 and 2020.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
Created by Ricardo Modrego. For questions or comments, contact me at [r.modrego.e@gmail.com](mailto:r.modrego.e@gmail.com).
