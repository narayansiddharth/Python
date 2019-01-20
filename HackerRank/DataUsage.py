import csv
import datetime


class DataUsage:

    def __init__(self):
        pass

    def parseCSV(self, fileName):
        dataUsageList = []
        with open(fileName, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                dataUsageList.append(dict(row))
        csvFile.close()

        return dataUsageList

    def classifyDayUsage(self, dataUsageList):

        customerUsage = {}
        print("Customer\tUsage")

        for row in dataUsageList:
            if 6 < int(datetime.datetime.strptime(row['Time'], '%H:%M:%S').hour) < 18:
                if row['Customer Id'] not in customerUsage.keys():
                    customerUsage[row['Customer Id']] = row['Pulse']
                else:
                    customerUsage[row['Customer Id']] = customerUsage[row['Customer Id']] + row['Pulse']

        for key, value in customerUsage.items():
            print(f"{key}\t{value}")

    def classifyNightUsage(self, dataUsageList):

        customerUsage = {}
        print("Customer\tUsage")

        for row in dataUsageList:
            if not (6 < int(datetime.datetime.strptime(row['Time'], '%H:%M:%S').hour) < 18):
                if row['Customer Id'] not in customerUsage.keys():
                    customerUsage[row['Customer Id']] = row['Pulse']
                else:
                    customerUsage[row['Customer Id']] = customerUsage[row['Customer Id']] + row['Pulse']

        for key, value in customerUsage.items():
            print(f"{key}\t{value}")

    def classifyWeeklyUsage(self, dataUsageList):
        customerUsage = {}
        print("Customer\tUsage")

        for row in dataUsageList:
            dt = datetime.datetime.strptime(row['Date'], '%d-%b-%Y')
            start = dt - datetime.timedelta(days=dt.weekday())
            end = start + datetime.timedelta(days=6)
            key = row['Customer Id'] + "_" + start.date().__str__() + "-" + end.date().__str__()
            if key not in customerUsage.keys():
                customerUsage[key] = row['Pulse']
            else:
                customerUsage[key] = customerUsage[row['Customer Id']] + row['Pulse']
        for key, value in customerUsage.items():
            print(f"{str(key).split('_')[0]}\t{value}")

    def classifyWeekDayUsage(self, dataUsageList):

        customerUsage = {}
        print("Customer\tUsage")

        for row in dataUsageList:
            dt = datetime.datetime.strptime(row['Date'], '%d-%b-%Y')
            start = dt - datetime.timedelta(days=dt.weekday())
            end = start + datetime.timedelta(days=6)
            key = row['Customer Id'] + "_" + start.date().__str__() + "-" + end.date().__str__()
            if 6 < int(datetime.datetime.strptime(row['Time'], '%H:%M:%S').hour) < 18:
                if key not in customerUsage.keys():
                    customerUsage[key] = row['Pulse']
                else:
                    customerUsage[key] = customerUsage[row['Customer Id']] + row['Pulse']
        for key, value in customerUsage.items():
            print(f"{str(key).split('_')[0]}\t{value}")

    def displayCustomerUsage(self, customerUsageMap):

        customerUsage = {}
        print("Customer\tUsage")

        for row in dataUsageList:
            if row['Customer Id'] not in customerUsage.keys():
                customerUsage[row['Customer Id']] = row['Pulse']
            else:
                customerUsage[row['Customer Id']] = customerUsage[row['Customer Id']] + row['Pulse']

        for key, value in customerUsage.items():
            print(f"{key}\t{value}")


def select_choice(choice):
    if choice == 1:
        du.classifyDayUsage(dataUsageList)
    elif choice == 2:
        du.classifyNightUsage(dataUsageList)
    elif choice == 3:
        du.classifyWeeklyUsage(dataUsageList)
    elif choice == 4:
        du.classifyWeekDayUsage(dataUsageList)
    elif choice == 5:
        exit(0)
    else:
        print("Invalid Choice")


if __name__ == '__main__':

    du = DataUsage()
    dataUsageList = du.parseCSV("scratch.csv")

    while True:
        print("1) Day Time Usage")
        print("2) Night Time Usage")
        print("3) Weekly Usage")
        print("4) Weekly Day Usage")
        print("5) Exit")
        choice = input("Enter your choice:")
        select_choice(int(choice))
