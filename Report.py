from datetime import datetime
from Hyena import Hyena
from Lion import Lion
from Tiger import Tiger
from Bear import Bear


def gen_birth_date(birthday):
    if birthday is None:
        return "Birthday unknown"
    newdate = []
    splitdate = birthday.split("-")
    for date in splitdate:
        newdate.append(int(date))
    date = datetime(newdate[0], newdate[1], newdate[2])
    return date.isoformat()


def categorize(animal):
    info = str(animal.animal_id + ", " + animal.name + "; birthdate: " + str(animal.birth_date) + "; " + animal.color + "; " + animal.sex + "; " + animal.weight + "; " + animal.originating_zoo + "; arrived: " + str(animal.date_arrival) + "\n")
    return info


def create_report(animals):
    file = open('zooPopulation.txt', "w+")
    file.write("Zookeeper's Challenge Zoo Population\n")
    for key, lists in animals.items():
        file.write("------------\n")
        file.write(key.upper() + " Habitat\n")
        if key == "hyenas":
            file.write(f"Number of hyenas created: {Hyena.numOfHyenas}\n")
        elif key == "lions":
            file.write(f"Number of lions created: {Lion.numOfLions}\n")
        elif key == "Tigers":
            file.write(f"Number of tigers created: {Tiger.numOfTigers}\n")
        else:
            file.write(f"Number of bears created:{Bear.numOfBears}\n")
        for animal in lists:
            file.write(categorize(animal))
    file.close()
    print('File created.')
