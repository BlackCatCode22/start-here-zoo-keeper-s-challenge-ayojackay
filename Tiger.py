from Animal import Animal


class Tiger(Animal):
    numOfTigers = 0
    tiger_sound = "Rawr... rawr"
    list_of_tiger_names = []
    file_path = r'./animalNames.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()

        line_num = 1
        for line in lines:
            if line_num == 15:
                list_of_tiger_names.extend(line.strip().split(', '))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id="an_id", birth_date="2022-03-13", color="Orange", sex="a_sex", weight="a_weight", originating_zoo="a_zoo", date_arrival="2024-04-22"):
        Tiger.numOfTigers +=1
        super().__init__("tiger", name, animal_id, birth_date, color, sex, weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.tiger_sound

    def get_tiger_name(self):
        return self.list_of_tiger_names.pop(0)
