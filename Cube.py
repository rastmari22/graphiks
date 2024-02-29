import random
import pygal as pg
class Cube:
    def __init__(self, sides=6):
        self.sides = sides
    def throw(self):
        self.face = random.randint(1, self.sides)
        return self.face
# def culc_theory(c1,c2):
#     N=c1.sides*c2.sides
#     min_sides=min(c1.sides,c2.sides)
#     max_sides=max(c1.sides,c2.sides)
#     prob_dict=dict.fromkeys([i for i in range(2, (cub1.sides + cub2.sides) + 1)],0)
#     for val1 in range(1,min_sides+1):
#         for val2 in range(1,max_sides+1):
#             prob_dict[val1+val2]+=1
#     for k,v in prob_dict.items():
#         prob_dict[k]=(v / N).__round__(2)
#     return prob_dict
# def culc_statistic_by_cube_sides(c1,c2):
#     N=c1.side*c2.side
#     min_sides=min(c1.side,c2.side)
#     max_sides=max(c1.side,c2.side)
#     prob_dict=dict.fromkeys([i for i in range(2, (cub1.sides + cub2.sides) + 1)],0)
#     for val1 in range(1,min_sides+1):
#         for val2 in range(1,max_sides):
#             prob_dict[val1+val2]+=1
#     prob_dict=culc_statistic(prob_dict)
#     return prob_dict
#     # sd_v=list(statistic.keys())
#     # stat_dict = dict.fromkeys(sd_v,0)
#     # sides=int((len(sd_v)+2)/2)
#     # print(sides)
#     # print(stat_dict)
#     # for i in range(1, sides + 1):
#     #     for j in range(1,sides+1):
#     #         stat_dict[i+j] =stat_dict[i+j]+1
#     # stat_dict=culc_statistic(stat_dict)
#     # print(stat_dict)
#     # return stat_dict
#
# def probability(statistic):
#     cul_stat = dict()
#     N = sum(statistic.values())
#     for k, v in statistic.items():
#         cul_stat[k] = (v / N).__round__(2)
#     return cul_stat
#
# def after_throwing_cubs(c1, c2, statistic):
#     sum_score = c1.face + c2.face
#     statistic[sum_score] += 1
#     return statistic
#
# cub1 = Cube()
# cub2 = Cube()
# sides_count = dict.fromkeys([i for i in range(2, (cub1.sides+cub2.sides) + 1)], 0)
# n = 36000
# for i in range(n):
#     cub1.throw()
#     cub2.throw()
#     sides_count = after_throwing_cubs(cub1, cub2, sides_count)
#
# probab=probability(sides_count)
# theor=culc_theory(cub1,cub2)
# def show_result(sides_count, probab,theor,n):
#     # posibility = culc_statistic(statistic)
#     # sum_score=list(sides_count.keys())
#     # throw_count=list(sides_count.values())
#     # pr=list(probab.values())
#     # th=list(theor.values())
#
#     sum_score = list(map(lambda x: '{:>4}'.format(x), sides_count.keys()))
#     throw_count = list(map(lambda x: '{:>4}'.format(x), sides_count.values()))
#     pr = list(map(lambda x: '{:>4}'.format(x), probab.values()))
#     th = list(map(lambda x: '{:>4}'.format(x), theor.values()))
#     print("Количество бросков = ", n)
#     print("Сумма очков:         ", '   '.join(map(str, sum_score)))
#     print("Число выпадений:     ", '   '.join(map(str, throw_count)))
#     print("Вероятность:         ", '   '.join(map(str, pr)))
#     print("Теория:              ", '   '.join(map(str, th)))
#     # so=list(posibility.values())
#     # strso='   '.join(map(str, so))
#     # print(strso)
#
#
# show_result(sides_count,probab,theor,n)
#
# hist=pg.Bar()
#
# hist.title=f"Результаты моделирования двух кубиков по {cub1.sides} и {cub2.sides} граней {n} раз"
# hist.x_labels=sides_count.keys()
# hist.x_title="Сумма очков"
# hist.y_title="Число выпадений"
#
# hist.add('Сумма ',sides_count.values())
# hist.render_to_file("Результат.svg")
