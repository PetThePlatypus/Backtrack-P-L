import yfinance as yf

## Backtrack Hypothetical P&L Returns.

# Function to calculate investment returns
def calculate_returns(symbol, start_date, end_date, investment_amount):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    initial_price = stock_data['Close'][0]
    final_price = stock_data['Close'][-1]
    final_investment_value = (investment_amount / initial_price) * final_price
    returns_percentage = ((final_investment_value - investment_amount) / investment_amount) * 100
    return initial_price, final_price, final_investment_value, returns_percentage

# Ticker, date, investment input
symbol = 'AAPL'
start_date = '2023-01-12'
end_date = '2023-09-14'
investment_amount = 1000

# Calculate returns
initial_price, final_price, final_investment_value, returns_percentage = calculate_returns(symbol, start_date, end_date, investment_amount)

# Display results
print(f'Initial Investment: ${investment_amount:.2f}')
print(f'Final Investment Value: ${final_investment_value:.2f}')
print(f'Percentage Return/Loss: {returns_percentage:.2f}%')
