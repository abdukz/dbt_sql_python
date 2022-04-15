import psycopg2
import pandas as pd

# connect to postgres 
con = psycopg2.connect(database='postgres', 
                       user='*************', 
                       password='*********', 
                       host='*************', 
                       port='****')

# selecting columns from daily_returns table
sql_query = pd.read_sql( "SELECT isin_code, DATE_PART('year', p_date) AS year, p_date, currency, one_day_pct FROM daily_returns " , con)
df1 = pd.DataFrame(sql_query, columns = ['isin_code','year', 'p_date','currency', 'one_day_pct'])

# selecting columns from security_reference table
sql_query_1 = pd.read_sql("SELECT proper_name, ticker_region, isin_code FROM security_reference", con)
df2 = pd.DataFrame(sql_query_1, columns = ['proper_name', 'ticker_region', 'isin_code'])

# mergin daily_returns & security_reference table.  
df3 = pd.merge(left = df1,right = df2, how = 'left') 

# average return for all stocks from 2015 to 2020 
avg_all = df3.groupby(['proper_name','year'])['one_day_pct'].mean()
# print(avg_all)
# print()

# total compound return % for all stock  
comp_rate = df3['one_day_pct'].mean()
#print('total compound return % for all stock ', comp_rate)
#print()

class CompoundCalc:
    def __init__(self):
        pass
    def calc_compound(self,principal_investment, interest_rate, comps_year, years):
        """
        # Compound Interest Formula  https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php#:~:text=The%20formula%20for%20compound%20interest,the%20number%20of%20time%20periods.
        Args:
            param1:  the principal investment amount (the initial deposit or loan amount)
            param2:  the annual interest rate (decimal)
            param3:  the number of times that interest is compounded per unit t
            param4:  the time the money is invested or borrowed for

        Returns:
            the future value of the investment/loan, including interest
        """
        investment_balace = principal_investment * (1 + (interest_rate/100) / comps_year ) ** (years * comps_year)
        return investment_balace
    
    
    def cagr(self, ending_value, beginning_value, years):
        """
        # CAGR formula https://www.investopedia.com/terms/c/cagr.asp (they forgot to add parentheses)

        Args:
            param1:  Ending value
            param2:  Beginnig value
            param3:  Number of years

        Returns:
            Compound Annual Growth Rate
        """
        return ((ending_value / beginning_value) ** (1/years)  - 1)  * 100


obj = CompoundCalc()

print("Calculating compounded investment balace")
principal_investment=float(input(" Principal Amount: "))
interest_rate=float(input("Annual rate: "))
comps_year = float (input("Compounds per year: "))
years=float(input("Years: "))

print()
print(obj.calc_compound(principal_investment, interest_rate, comps_year, years))
print()

print("Calculating compound annual growth rate")
ending_value = float(input("Ending Balance: "))
beginning_value  = float(input("Beginning Balance: "))
years = float(input("Number of Years: "))
# y = CompoundCalc()

print()
print(obj.cagr(ending_value, beginning_value, years))


con.close()  



