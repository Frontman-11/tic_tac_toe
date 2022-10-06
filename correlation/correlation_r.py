from pearson_r import pearson_r
from spearman_r import spearman_rs

# raw_data = {
#     'x': (100, 200, 300, 400, 500, 600),
#     'y': (1.4, 3.1, 4.8, 5.5, 6.4, 8.1)
# }
# raw_data = {
#     'x': (8, 10, 3, 9, 6, 5, 1, 7, 2, 4),
#     'y': (10, 8, 7, 6, 9, 4, 1, 5, 2, 3)
# }

# raw_data = {'x': (0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10),
#             'y': (1.6, 2.7, 4.5, 7.4, 12.2, 20.1, 33.1, 54.6, 90, 148.4, 244.7, 403.4, 665.1, 1096.6, 1808.0,
#                   2981, 4914.8, 8103.1, 13359.7, 22026.5)
#             }

raw_data = {'x': [0.8, 1.93, 0.97, 11.8, 1.41, 2.41, 3.4, 0.98, 2.46, 0.26, 9.97, 0.37, 6.7, 0.09, 1.72, 6.76,
                  10.27, 0.13, 2.87, 3.1, 0.96, 3.77, 7.09],
            'y': [678.1, 818.93, 302.38, 1149.60, 573.14, 1034.55, 633.25, 1095.42,
                  1122.58, 686.51, 1172.84, 593.7, 1247.95, 533.99, 605.51, 696.96, 1282.95, 531.16, 788.36, 956.06,
                  1149.38, 1069.82, 1124.17]
            }


r = pearson_r(raw_data)
rs = spearman_rs(raw_data)

print(f'Observed data:\nx:{raw_data["x"]}\ny:{raw_data["y"]}')
print('')
print(f'Pearson\'s Coefficient: {r}')
print(f'Spearman\'s Coefficient: {rs}')
print('')
