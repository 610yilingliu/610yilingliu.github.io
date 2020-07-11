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

# heroes = [[1000, 0.2], [1200, 0.1], [500, 0.5]]

# for index in range(len(heroes)):
#     HeroEquipChoose(heroes[index][0], heroes[index][1])

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

f = open("E:/GitStorage/610yilingliu.github.io/code_example/data.txt", 'r')
content = f.readlines()
f.close()
for line in content:
    # after this step, you got a string like '1000, 0.2'
    deleted_enter = line.strip('\n')
    # after this step, you will get ['1000', '0.2']
    list_inside_list = deleted_enter.split(',')
    # contert `1000` to 1000.0, '0.2' to 0.2, and call function HeroEquipChoose()
    HeroEquipChoose(float(list_inside_list[0]), float(list_inside_list[1]))
