

from less17_dasauto import *

auto1 = DasAuto("vw","polo", 90)
auto1.__hp = 80
print(auto1.get_info())

auto2 = DasElektroCar("azlk", "moskvich 3", 193, 65.7)
auto2.__battCapacity = 90
print(auto2.get_info())
