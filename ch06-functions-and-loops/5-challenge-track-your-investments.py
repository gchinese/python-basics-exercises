# 6.5 - Challenge: Track Your Investments
# Solution to challenge


# Calculate interest to track the growth of an investment
amount = float(input("Write your initial amount: "))
rate = float(input("Write your rate: "))
years =int(input("How many years: ")) 

def invest(amount, rate, years):
    """Display year on year growth of an initial investment"""
    for year in range(1, years + 1):
        amount += amount * (rate / 100)
        print(f"year {year}: ${amount:,.2f}")

invest(amount, rate, years)

