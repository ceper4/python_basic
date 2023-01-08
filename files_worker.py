import csv
import json


all_rows = [
    {
        'departure point': 'Borispyl',
        'departure time': '14:50',
        'destination point': 'Beijing',
        'arrival time': '15:15',
        'cost ticket': '950$'
    },
    {
        'departure point': 'London',
        'departure time': '12:10',
        'destination point': 'Paris',
        'arrival time': '13:25',
        'cost ticket': '60$'
     },
    {
        'departure point': 'Frankfurt',
        'departure time': '18:45',
        'destination point': 'Seoul',
        'arrival time': '17:40',
        'cost ticket': '230$'
    }
]

fieldnames = [
    'departure point',
    'departure time',
    'destination point',
    'arrival time',
    'cost ticket']
with open('schedule.csv', 'w', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    writer.writeheader()

    for input_row in all_rows:
        writer.writerow(input_row)

total = []
with open('schedule.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            print(

                f"{row=}, {type(row)=}, "
            )
            total.append(row)
with open("schedule.json", "w") as fh:
    json.dump(total, fh, indent=4, sort_keys=True)


