# use_eq_a = (800 + 200) * (1 + 0.05 + 0.1)
# print('DMG if use a ' + str(use_eq_a))

# use_eq_b = (800 + 100) * (1 + 0.05 + 0.2)
# print('DMG if use using b ' + str(use_eq_b))

# if use_eq_a > use_eq_b:
#     print('choose a')
# elif use_eq_a < use_eq_b:
#     print('choose b')
# else:
#     print('two equipments are the same')

def HeroEquipChoose(ori_atk, ori_edm):
    use_eq_a = (ori_atk + 200) * (1 + ori_edm + 0.1)
    # print('DMG if use a ' + str(use_eq_a))

    use_eq_b = (ori_atk + 100) * (1 + ori_edm + 0.2)
    # print('DMG if use using b ' + str(use_eq_b))

    if use_eq_a > use_eq_b:
        print('choose a')
    elif use_eq_a < use_eq_b:
        print('choose b')
    else:
        print('two equipments are the same')


heroes = [[1000, 0.2], [1200, 0.1], [500, 0.5]]

for index in range(len(heroes)):
    HeroEquipChoose(heroes[index][0], heroes[index][1])

