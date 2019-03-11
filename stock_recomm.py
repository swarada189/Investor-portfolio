
# coding: utf-8


import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime
from sys import exit
import fix_yahoo_finance as yf
yf.pdr_override() 


company_names = []
company_symbols = []
stock_values = pd.DataFrame()
close_rates = pd.DataFrame()
start_date="2017-11-10"
end_date="2018-02-10"
today="2018-02-10"
purchase_prices=[]


def read_symbols(filename):
	#Function to read the company names and company symbols from the file.
	with open(filename,"r") as fp:
		line = fp.readlines()
	for text in line:
		company_names.append(text.split()[0])
		company_symbols.append(text.split()[1])
		purchase_prices.append(text.split()[2])

def read_stock_values(start_date,end_date):
	#Function to read the stock data from yahoo exchange website
	#https://in.finance.yahoo.com/
	i = 0
	global stock_values
	for symbol in company_symbols:
		print "Getting the data for %s"%company_names[i]
		df=pdr.get_data_yahoo(symbol,start_date,end_date)[["Open","Close"]]
		df["Company"] = company_names[i]
		stock_values = stock_values.append(df)
		i+=1

def recommend_stock():
	#returns the recommended stock based on the opening and closing rates of stocks 
	stock_values["Difference"] = stock_values["Open"] - stock_values["Close"]
	stock_values["Rate"] = (stock_values["Difference"] / stock_values["Close"])*100
	#print stock_values.head(2)
	pivoted_value = pd.pivot_table(stock_values,values=["Rate"],columns=["Company"],aggfunc=np.std)
	print "PROFIT ANALYSIS..."	
	print pivoted_value 
	print "System recommends you to buy shares of ",pivoted_value.idxmax(axis=1).values


def write_data(filename):
	#Writes the results into a file passed by the user(in this case output.csv)
	stock_values.to_csv(filename,encoding='utf-8')


def sell_shares():
	global close_rates
	i=0
	#close_rates = pd.read_csv("stock_today.csv",index_col=0,parse_dates=True)	
	for symbol in company_symbols:
		print "Getting today's data for %s"%company_names[i]
		df=pdr.get_data_yahoo(symbol,today,today)[["Open","Close"]]
		df["Company"] = company_names[i]
		close_rates = close_rates.append(df)
		i+=1
	pp=[]
	for i in purchase_prices:
		pp.append(float(i))
	close_rates["Purchase_price"]=pp
	print close_rates

	close_rates["Diff"]=close_rates["Close"]-close_rates["Purchase_price"]
	print close_rates

	profit=[]
	loss=[]
	for i in range(len(close_rates.index)):
	    	if close_rates["Diff"][i]>0:
			profit.append(close_rates["Company"][i])
	   	else:
			loss.append(close_rates["Company"][i])
	print "Sell shares for following companies ",loss
	print "Keep shares for following companies",profit



def main():
	read_symbols("selected_companies.txt")
	choice = 0
	while(choice != 3):
		choice = input("Enter your choice:\n1.Buy a share\n2.Sell a share\n3.Exit : ")
		
		if choice == 1:
			read_stock_values(start_date,end_date)
			recommend_stock()
			write_data("output.csv")

		elif choice == 2:
			sell_shares()
	

		elif choice == 3:
			exit
			
		else:
			print ("Invalid choice..Try again")


		
		
if __name__ == '__main__':
	main()

'''
swarada@swarada-HP:~/Stock$ python stock_recomm.py 
Enter your choice:
1.Buy a share
2.Sell a share
3.Exit : 1

Getting the data for Reliance
[*********************100%***********************]  1 of 1 downloaded
Getting the data for IBM
[*********************100%***********************]  1 of 1 downloaded
Getting the data for Sears
[*********************100%***********************]  1 of 1 downloaded
Getting the data for Barclays
[*********************100%***********************]  1 of 1 downloaded
PROFIT ANALYSIS...
Company  Barclays       IBM  Reliance     Sears
Rate     0.972624  0.992852  7.219105  6.166453
System recommends you to buy shares of  ['Reliance']
Enter your choice:
1.Buy a share
2.Sell a share
3.Exit : 2
Getting today's data for Reliance
[*********************100%***********************]  1 of 1 downloaded
Getting today's data for IBM
[*********************100%***********************]  1 of 1 downloaded
Getting today's data for Sears
[*********************100%***********************]  1 of 1 downloaded
Getting today's data for Barclays
[*********************100%***********************]  1 of 1 downloaded
                  Open       Close   Company  Purchase_price
Date                                                        
2018-02-09   25.400000   27.000000  Reliance           30.00
2018-02-09  148.600006  149.509995       IBM          143.00
2018-02-09    2.120000    2.150000     Sears            1.50
2018-02-09   10.710000   10.750000  Barclays           11.23
                  Open       Close   Company  Purchase_price      Diff
Date                                                                  
2018-02-09   25.400000   27.000000  Reliance           30.00 -3.000000
2018-02-09  148.600006  149.509995       IBM          143.00  6.509995
2018-02-09    2.120000    2.150000     Sears            1.50  0.650000
2018-02-09   10.710000   10.750000  Barclays           11.23 -0.480000
Sell shares for following companies  ['Reliance', 'Barclays']
Keep shares for following companies ['IBM', 'Sears']
Enter your choice:
1.Buy a share
2.Sell a share
3.Exit : 3
swarada@swarada-HP:~/Stock$ 

'''
