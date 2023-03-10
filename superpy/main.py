# Imports
import random
import argparse
import csv
from datetime import datetime as dt
import pandas as pd
from my_date_time import datum, date_txt_file, date_today
import os
from my_revenue import Revenue
from profit import Profit
import uuid




# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

FILE_BOUGHT = "bought.csv"
FILE_SOLD = "sold.csv"
HEADER_B = ['id','product','Count','Buy date','Buy price','experation date']
HEADER_S = ['id','Bought_ID','product','Sell_date','Sell_price']

cwd = os.getcwd()
path = os.path.join(cwd, "txt_files")
now = dt.now()
id = ''

def make_files():

    try:
        with open(FILE_BOUGHT, 'r') as file:
            pass
    except FileNotFoundError:
        with open(FILE_BOUGHT, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(HEADER_B)

    try:
        with open(FILE_SOLD, 'r') as file:
            pass
    except FileNotFoundError:
        with open(FILE_SOLD, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(HEADER_S)


def choice_rev():
    choice = args.rev
    Revenue.revenue_calc(choice)

def txt_folder():  
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)        

def report_bought():
    make_files()
    df = pd.read_csv(FILE_BOUGHT)
    df.head(3)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
    txt_folder()
    write_day_file()
    
   


def report_sold():
    df = pd.read_csv(FILE_SOLD)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)


def ad_to_list():
    make_files() 
    shop_list = []
    unique_id = uuid.uuid1().hex[:8]
    with open(FILE_BOUGHT, mode ='r')as file:
        csvFile = csv.reader(file)
           
    shop_list.append(unique_id)     
    shop_list.append(args.product)
    shop_list.append(args.count)
    shop_list.append(date_today())
    shop_list.append(args.price)
    shop_list.append(args.expiration)
    print(f"You input is: {shop_list}")

    with open(FILE_BOUGHT,'a+', newline='') as csvfile:
    # Create a writer object from csv module
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(shop_list)
    txt_folder()    
    write_day_file()
     
def check_inventory():
    make_files()
    df = pd.read_csv(FILE_BOUGHT)
    check_stock = df[df["id"] == id]
    print(check_stock)
    data_top = check_stock.head() 
    for row in data_top.index:
        index_nr = row
    if df.at[index_nr,'Count'] < args.sell_count:
        print(f"Out of stock. Stock = {df.at[index_nr,'Count']}")
    
    else:
        total = df.at[index_nr,'Count'] - args.sell_count
        df.at[index_nr,'Count']= total
        if total < 1:
            print("This product is now out of stock")
            df.drop(df.loc[df['Count']==0].index, inplace=True)
            
    df.to_csv(FILE_BOUGHT, index=False)
        

def ad_sell_list():
    global id
    make_files()
    sell_list = []
    df = pd.read_csv(FILE_BOUGHT)
    if df['product'].eq(args.sell_product).any():
        check_stock = df[df["product"] == args.sell_product]
        id_str = check_stock["id"].values
        id = id_str[0]
        unique_id = uuid.uuid1().hex[:8]
        with open(FILE_SOLD, mode ='r')as file:
            sell_list.append(unique_id)     
            sell_list.append(id)
            sell_list.append(args.sell_product)
            sell_list.append(args.sell_count)
            sell_list.append(args.sell_date)
            sell_list.append(args.sell_price)
            #number = args.sell_count
            check_inventory()
            print(f"You input is: {sell_list}")

            with open(FILE_SOLD, 'a+', newline='') as csvfile:
            # Create a writer object from csv module
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(sell_list) 
    else:
        print('This product is not in stock')

def advance_t():
    nr = args.days
    txt_file = (datum(nr)) + ".txt"

    try:
        os.chdir("txt_files")
        with open(txt_file, 'r') as file:
            df = pd.read_csv(file)
            print(df)
    except FileNotFoundError:
        print("File not found")

def write_day_file():
    directory = "txt_files"
    data = pd.read_csv(FILE_BOUGHT, usecols=[1,2,4,5])
    file = date_txt_file()
    location = os.path.join(cwd, directory)
    path = os.path.join(location, file) 
    content = str(data)
    with open(path, 'w') as file_txt:
        file_txt.write(content)


    
def products():
    make_files()
    data = pd.read_csv(FILE_BOUGHT, usecols=[1,2,4,5])
    print(data)

def is_expired():
    make_files()
    df = pd.read_csv(FILE_BOUGHT)
    day = date_today()
    filter_df = df.loc[(df['experation date'] < day)]
    print(filter_df)
    answer = input("delete rows j/n : ")
    if answer == 'j':
        df.drop(df.loc[df['experation date'] < day].index, inplace=True)
        df.to_csv(FILE_BOUGHT, index=False)
        print("products are removed from inventory") 

def choice():
    revenue_choice = args.rev
    if revenue_choice == "today":
        df = pd.read_csv(FILE_BOUGHT)
        day = date_today()
        filter_df = df.loc[(df['Buy date'] == day)]
        print(filter_df)

def reven_date():
    given_date = args.rev_date
    Revenue.rev_date_calc(given_date)

def choice_profit():
    choice = args.prof
    Profit.profit_calc(choice)

def profit_date():
    given_date = args.prof_date
    Profit.prof_date_calc(given_date)

parser = argparse.ArgumentParser(description='Shop inventory manager!')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

# Create a subcommands 
parser_report = subparsers.add_parser('report_bought', help='print bought report')
parser_report.set_defaults(func=report_bought)
    
parser_experation = subparsers.add_parser('is_expired', help='print is_expired report')
parser_experation.set_defaults(func=is_expired)

parser_sold = subparsers.add_parser('report_sold', help='print sold report')
parser_sold.set_defaults(func=report_sold)

parser_products = subparsers.add_parser('products', help='print products')
parser_products.set_defaults(func=products)

parser_revenue = subparsers.add_parser('revenue', help='Revenue, CHOICE: "today" or "yesterday"')
parser_revenue.add_argument('rev', type=str, choices=['today', 'yesterday'])
parser_revenue.set_defaults(func=choice_rev)

parser_profit = subparsers.add_parser('profit', help='Profit, CHOICE: "today" or "yesterday"')
parser_profit.add_argument('prof', type=str, choices=['today', 'yesterday'])
parser_profit.set_defaults(func=choice_profit)

parser_profit_date = subparsers.add_parser('profit_date', help='Profit, give date: "dd-mm-yy"')
parser_profit_date.add_argument('prof_date', type=str, help='Profit give date: "dd-mm-yy"')
parser_profit_date.set_defaults(func=profit_date)

parser_revenue_date = subparsers.add_parser('revenue_date', help='Revenue, give date "dd-mm-yy"')
parser_revenue_date.add_argument('rev_date', type=str, help='Revenue give date')
parser_revenue_date.set_defaults(func=reven_date)

parser_buy = subparsers.add_parser('buy', help='buy help')
parser_buy.add_argument('product', type=str, help='Product name')
parser_buy.add_argument('count', type=int, help='How many products have you bought')
parser_buy.add_argument('price', type= float, help='price off the product you pay')
parser_buy.add_argument('expiration', type= str, help='Whats the expiration date')
parser_buy.set_defaults(func=ad_to_list)

parser_count = subparsers.add_parser('count', help='count help')
parser_count.add_argument('count', type=int, help='How many products have you bought')

parser_sell = subparsers.add_parser('sell', help='Sell help')
parser_sell.add_argument('sell_product', type=str, help='Productname')
parser_sell.add_argument('sell_count', type=int, help='count')
parser_sell.add_argument('sell_date', type=str, help='Sell date')
parser_sell.add_argument('sell_price', type=float, help='Sell price')
parser_sell.set_defaults(func=ad_sell_list)

parser_sold = subparsers.add_parser('sold', help='report sold help')
parser_sold.add_argument('report_sold', help='How many products have you sold')

parser_advance_t = subparsers.add_parser('advance_time', help='How many days back?')
parser_advance_t.add_argument('days', type=int, help='How many products have you sold')
parser_advance_t.set_defaults(func=advance_t)

parser_expired = subparsers.add_parser('Is expired', help='is_expired help')
parser_expired.add_argument('is_expired', help='print is_expired report')

parser_prod_stock = subparsers.add_parser('products_stock', help='products in stock')
parser_prod_stock.add_argument('products', help='print products')

args = parser.parse_args()
args.func()


