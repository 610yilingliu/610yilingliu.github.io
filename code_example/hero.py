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


HeroEquipChoose(800, 0.05)
HeroEquipChoose(1000, 0.2)
HeroEquipChoose(1500, 0)
HeroEquipChoose(400, 0.5)