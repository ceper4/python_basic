import csv
import json
with open('schedule.csv', 'w', newline='') as fh:
    fieldnames = ['departure point', 'departure time', 'destination point', 'arrival time', 'cost ticket']
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'departure point': 'Borispyl', 'departure time': '14:50', 'destination point': 'Beijing',
                     'arrival time': '15:15', 'cost ticket': '950$'})
    writer.writerow({'departure point': 'London', 'departure time': '12:10', 'destination point': 'Paris',
                     'arrival time': '13:25', 'cost ticket': '60$'})
    writer.writerow({'departure point': 'Frankfurt', 'departure time': '18:45', 'destination point': 'Seoul',
                     'arrival time': '17:40', 'cost ticket': '230$'})

with open('schedule.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(

                f"{row=}, {type(row)=}, "
            )

with open("schedule.json", "w") as fh:

    json.dump(row, fh, indent=4, sort_keys=True)

