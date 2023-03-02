

class DasAuto():
    """Class for Gazoline auto"""
    def __init__(self, vendor: str, model: str, hp: int):
        self.__vendor = vendor
        self.__model = model
        self.__hp = hp

    def get_vendor(self):
        return self.__vendor

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_info(self) -> str:
        return str(self.__vendor).upper() + " \t\t" + (self.__model + " \t\t" + str(self.__hp) + " hp").title()


class DasElektroCar(DasAuto):
    """Class for ElectroCar"""
    def __init__(self, vendor, model, hp, batt_capacity: int):
        super().__init__(vendor, model, hp)
        self.__battCapacity = batt_capacity

    def get_info(self) -> str:
        return (str(self.get_vendor()).upper() + " \t" + (self.get_model() + " \t" +
                str(self.get_hp()) + " hp ").title() + "Batt: " + str(self.__battCapacity) + " kWph")

