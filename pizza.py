import sys
import csv
from tabulate import tabulate

def main():

    menu = []
    chek_sysargv()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not find")
    print(tabulate(menu[1:], headers=menu[0], tablefmt='grid'))

def chek_sysargv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if "csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__=="__main__":
    main()