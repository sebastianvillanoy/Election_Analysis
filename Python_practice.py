item = 'coat'
sticker_price= 1000
tax_rate= 0.13
print(f'Your {item} will cost ${(sticker_price * (1 + tax_rate)):,.2f} after taxes.')

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, value in counties_dict.items():
    print(f'{key} county has {value:,} registered voters.')


