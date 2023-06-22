import sys
import csv

def main():

    school = []
    chek_sysargv()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                l_name, f_name = row["name"].split(",")
                house = row["house"]
                school.append({"Last":l_name, "First" :f_name, "House":house})

        with open(sys.argv[2], "w") as n_file:
            writer = csv.DictWriter(n_file, fieldnames=["First", "Last", "House"])
            writer.writerow({"First":"First", "Last":"Last", "House":"House"})
            for w_row in school:
                (writer.writerow({"First":w_row["First"], "Last":w_row["Last"], "House":w_row["House"]}))
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def chek_sysargv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit(f"The |{sys.argv[1]}| not a CSV files")
    if ".csv" not in sys.argv[2]:
        sys.exit(f"The |{sys.argv[2]}| not a CSV files")

if __name__=="__main__":
    main()