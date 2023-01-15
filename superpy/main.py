# Imports
import random
import argparse
import csv
from datetime import datetime as dt
import pandas as pd
from date_time import datum




# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

file_bought = "bought.csv"
file_sold = "sold.csv"
now = dt.now()

def date_txt_file():
    # Getting current date and time
    today_date = now.strftime("%d-%m-%Y") + '.txt'
    return today_date

def report_bought():
    df = pd.read_csv(file_bought)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)
    write_day_file()



def report_sold():
    df = pd.read_csv(file_sold)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)


def ad_to_list(): 
    shop_list = []
    with open(file_bought, mode ='r')as file:
           # reading the CSV file
        csvFile = csv.reader(file)
            # displaying the contents of the CSV file
        random_number = random.randint(1000, 9999)
        if random_number in file:
            random_number = random.randint(1000, 9999)
    shop_list.append(random_number)     
    shop_list.append(args.product)
    shop_list.append(args.count)
    shop_list.append(args.buy_date)
    shop_list.append(args.price)
    shop_list.append(args.exparation)
    print(f"You input is: {shop_list}")

    with open(file_bought,'a+', newline='') as csvfile:
    # Create a writer object from csv module
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(shop_list)
     
    write_day_file()
   

def ad_sell_list():
    sell_list = []

    with open(file_sold, mode ='r')as file:
        csvFile = csv.reader(file)

        random_number = random.randint(1000, 9999)
        if random_number in file:
            random_number = random.randint(1000, 9999)
    sell_list.append(random_number)     
    sell_list.append(args.bought_id)
    sell_list.append(args.sell_date)
    sell_list.append(args.sell_price)
 
    print(f"You input is: {sell_list}")

    with open(file_sold, 'a+', newline='') as csvfile:
    # Create a writer object from csv module
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(sell_list) 

def advance_t():
    day = now.strftime("%d-%m-%Y")
    nr = args.days
    txt_file = (datum(nr)) + ".txt"
    try:
        with open(txt_file, 'r') as file:
            df = pd.read_csv(file)
            #file_contents = file.read()
            print(df)

    except FileNotFoundError:
        print("File not found")

def write_day_file():
    data = pd.read_csv(file_bought, usecols=[1,2,4,5])
    file = date_txt_file()
    data.to_csv(file, index=False)
 
    
def products():
    pass

def total_products():
    pass

def price_bought():
    pass

def sold_price():
    pass

def experation():
    pass

def is_expired():
    pass

parser = argparse.ArgumentParser(description='Shop inventory management!')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

    # Create a subcommand    
parser_report = subparsers.add_parser('report_bought', help='print bought report')
parser_report.set_defaults(func=report_bought)

parser_report = subparsers.add_parser('report_sold', help='print sold report')
parser_report.set_defaults(func=report_sold)

    # create the parser for the "buy" command
parser_a = subparsers.add_parser('buy', help='buy help')
parser_a.add_argument('product', type=str, help='Product name')
parser_a.add_argument('count', type=int, help='How many products have you bought')
parser_a.add_argument('buy_date', type=str, help='When did you buy the product "date"')
parser_a.add_argument('price', type= float, help='price off the product you pay')
parser_a.add_argument('exparation', type= str, help='Whats the exparation date')
parser_a.set_defaults(func=ad_to_list)


    # create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('count', type=int, help='How many products have you bought')

    # create the parser for the "c" command
parser_c = subparsers.add_parser('c', help='c help')
parser_c.add_argument('report_bought', help='How many products have you bought')

     # create the parser for the "d" command
parser_d = subparsers.add_parser('sell', help='d help')
parser_d.add_argument('bought_id', type=int, help='Bought ID number')
parser_d.add_argument('sell_date', type=str, help='Sell date')
parser_d.add_argument('sell_price', type=int, help='Sell price')
parser_d.set_defaults(func=ad_sell_list)

   # create the parser for the "e" command
parser_e = subparsers.add_parser('e', help='e help')
parser_e.add_argument('report_sold', help='How many products have you sold')

   # create the parser for the "f" command
parser_f = subparsers.add_parser('advance_time', help='How many days back?')
parser_f.add_argument('days', type=int, help='How many products have you sold')
parser_f.set_defaults(func=advance_t)

args = parser.parse_args()
args.func()