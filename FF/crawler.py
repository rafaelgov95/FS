# -*-coding: utf-8-*-
import json
import codecs
import perfil
import lugares
import numpy as np

sys_api_token = 0
sys_client_version = 0
lista = []

def get_json(user_id):
    crawl_tips = {}
    crawl_tips['user_info'] = perfil.fetch_user_profile(user_id)
    if crawl_tips['user_info'] != -1:
        crawl_tips['tips'] = lugares.fetch_usr_tips(user_id)
    else:
        return -1
    return crawl_tips


def run(start_point, finish_point, step):
    output_file = codecs.open("4sq_date_%d_ate_%d.txt" % (start_point, finish_point), "w", "utf-8-sig")
    for UID in range(start_point, finish_point + 1, step):
        result = get_json(str(UID))
        if result != -1:
            print UID, 'Done'
            lista.append(result)
            output_file.write("%s\n" % json.dumps(result))
    output_file.close()
from collections import namedtuple
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
import matplotlib.pyplot as plt

if __name__ == '__main__':
    bar_color_b = 'blue'
    bar_color_p = 'pink'
    start_point = 1
    finish_point = 100
    step = 1
    width_n = 0.4
    run(start_point, finish_point, step)
    somaM=0
    somaF=0
    for i in lista:
        if(i.get('user_info')['gender']=='m'):
            somaM=somaM +i.get('tips')['count']
        else:
            somaF=somaF +i.get('tips')['count']
    # plt.bar(2, [somaM,somaF], width=width_n, color=bar_color_b)
    # plt.bar(1, [somaF], width=width_n, color=bar_color_p)


    bar_1 = [somaF]
    bar_2 = [somaM]
    # Range com a quantidade de itens das barras
    x_pos =np.arange(len(bar_1))

    first_bar = plt.bar(x_pos, bar_1, 0.5, color='b')
    second_bar = plt.bar(x_pos, bar_2, 0.5, color='y', bottom=bar_1)
    # Definir posição e labels no eixo X
    plt.xticks(x_pos, ('Female', 'Male'))

    plt.show()