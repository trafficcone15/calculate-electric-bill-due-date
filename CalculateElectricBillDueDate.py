import numpy as np
import pandas as pd
import holidays

def calculate_dates(year, month_name):
    month = pd.to_datetime(month_name, format='%B').month
    
    invoice_date = pd.Timestamp(year, month, 22)

    nz_holidays = holidays.NewZealand(years=year)

    while invoice_date.dayofweek >= 5 or str(invoice_date.date()) in nz_holidays:
        invoice_date += pd.offsets.BDay()

    if str(invoice_date.date() - pd.offsets.BDay()) in nz_holidays:
        invoice_date += pd.offsets.BDay(1)

    due_date = invoice_date
    for i in range(11):
        due_date += pd.offsets.BDay()
        while str(due_date.date()) in nz_holidays:
            due_date += pd.offsets.BDay()

    return invoice_date, due_date

year = 2024
month = 'January'
invoice_date, due_date = calculate_dates(year, month)

print(f"Invoice Date: {invoice_date.strftime('%Y-%m-%d')}")
print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")