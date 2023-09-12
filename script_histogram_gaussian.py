# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:16:59 2023

@author: eladyos1
"""

import numpy as np
import matplotlib.pyplot as plt


def create_graphs(sno_name, NM_location, Chimeras_dict):
    Chimeras_dict = dict(sorted(Chimeras_dict.items(), key=lambda item: int(item[0])))

    counts = list(Chimeras_dict.values())
    locations = list(Chimeras_dict.keys())
    print(locations)
    locations_str = [str(i) for i in locations]
    loc = ["a", "b", "c", "e", "f", "g"]
    x = np.array(locations, dtype=int)
    y = np.array(counts)

    mu = int(NM_location)
    sigma = 1

    x_vals = np.linspace(x[0], x[-1], 100)
    y_vals = np.exp(-0.5 * ((x_vals - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

    figure, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 10), gridspec_kw={'hspace': 0.5})  # Increased hspace

    ax1.bar(x, y, edgecolor='black', width=0.9)
    ax1.set_xticks(x)
    ax1.set_xticklabels(locations_str)
    ax1.set_xlabel('Locations')
    ax1.set_ylabel('Chimeras count')
    ax1.set_title('Histogram bar \nSno: {0} , NM: {1}'.format(sno_name, NM_location))
    for j, v in enumerate(counts):
        ax1.text(x[j], v + 1, str(v), ha='center', va='bottom')  # Add y-values for each histogram bar

    ax2.plot(x_vals, y_vals, color='red', linewidth=2)
    ax2.axvline(x=int(NM_location), linestyle='--', color='black')
    ax2.text(int(NM_location), 0.1, f'x={NM_location}', ha='left', va='bottom')  # Add x-value label for dashed line
    ax2.set_xlabel('Locations')
    ax2.set_ylabel('Probability density')
    ax2.set_title('Gaussian Distribution \nSno: {0}, NM: {1} '.format(sno_name, NM_location))
    


if __name__ == '__main__':

    sno_names = ["TB8Cs3C3", "TB10Cs3C3", "TB6Cs1H3", "TB11Cs3C2", "TB9Cs4C2", "TB10Cs2ppC3", "TB10Cs2ppC3",
                 "TB10Cs3C2", "TB9Cs2C4", "TB10Cs4C3", "TB10Cs4C3", "TB10Cs1C3", "TB10Cs1C3", "TB10Cs1C3",
                 "TB10Cs1C3", "TB11Cs4C2", "TB11Cs4C2", "TB10Cs3C4","TB10Cs3C4","TB9Cs4C1","TB8Cs3C1","TB8Cs3C1",
                 "TB9Cs2C7","TB10Cs1C4","TB10Cs1C1","TB10Cs1C1","TB10Cs3C5","TB10Cs3C5","TB10Cs3C1","TB9Cs2C1"]

    NM_locations = ["1963", "2597", "2579", "3434", "4703", "3547", "6894", "3591", "3812", "4040", "4051", "3569",
                    "4547", "3569", "4547", "6205", "6216", "6434", "6470", "6556","6897","6909","8265",
                    "8159","8208","8216","8326","8335","8982","9020"]

    Chimeras_dicts = [
        {"1953": 107, "1957": 126, "1963": 143, "1973": 148, "1978": 147, "1983": 144},
        {"2579": 416, "2597": 338, "2631": 22, "2638": 14},
        {"2579": 215, "2597": 230, "2631": 65, "2638": 58},
        {"3434": 137, "3448": 136},
        {"4614": 121, "4615": 123, "4703": 373},
        {"3509": 6, "3513": 58, "3520": 182, "3529": 211, "3536": 214, "3547": 217, "3569": 46, "3591": 16, "3593": 16},
        {"6894": 77, "6897": 76, "6898": 76, "6903": 74, "6909": 68, "6923": 32, "6954": 32},
        {"3569": 105, "3591": 175, "3593": 177},
        {"3812": 451, "3816": 486, "3824": 499, "3848": 460, "3849": 459},
        {"4013": 80, "4033": 154, "4038": 153, "4051": 149, "4063": 107},
        {"4013": 80, "4033": 154, "4038": 153, "4051": 149, "4063": 107},
        {"3513": 7, "3520": 30, "3529": 38, "3536": 42, "3547": 45},
        {"4547": 79, "4583": 196, "4614": 59, "4615": 59},
        {"3513": 7, "3520": 30, "3529": 38, "3536": 42, "3547": 45, "3569": 86, "3591": 73, "3593": 74},
        {"4547": 79, "4583": 196, "4614": 59, "4615": 59},
        {"6156": 45, "6204": 243, "6205": 244, "6213": 234, "6216": 221, "6228": 118, "6274": 68},
        {"6156": 45, "6204": 243, "6205": 244, "6213": 234, "6216": 221, "6228": 118, "6274": 68},
        {"6418":164, "6434":244,"6447":324,"6455":398,"6458":421,"6469":391,"6470":407,"6537":173,"6547":182, "6556":232},
        {"6418": 164, "6434": 244, "6447": 324, "6455": 398, "6458": 421, "6469": 391, "6470": 407, "6537": 173,"6547": 182, "6556": 232},
        {"6537": 157, "6547":193, "6556":233},
        {"6894":119,"6897":124,"6898":122,"6903":130,"6909":102,"6923":57},
        {"6894":119,"6897":124,"6898":122,"6903":130,"6909":102,"6923":57},
        {"8229":117,"8236":170,"8251":236,"8253":245,"8265":315,"8279":317,"8287":308,"8292":324},
        {"8062" :	69,"8097":125,"8125" :146,"8126" :148,"8129" :147,"8131"  :145,"8135"  :145,"8137" :147,"8151": 177,"8152":181,"8159" :185,"8185" :190},
        {"8208": 72, "8216": 83, "8218": 81, "8220": 80, "8222": 79, "8229": 87, "8236": 77},
        {"8208": 72, "8216": 83, "8218": 81, "8220": 80, "8222": 79, "8229": 87, "8236": 77},
        {"8292":107,"8326":182,"8329":185,"8335":183,"8669":8},
        {"8292": 107, "8326": 182, "8329": 185, "8335": 183, "8669": 8},
        {"8941":57,"8977":365,"8982":365,"8984":366,"8995":324,"9005":194,"9007":190,"9016":120,"9020":112},
        {"9007":296,"9016":357,"9020":387,"9026":399,"9036":311,"9041":292,"9042":312}

    ]

    fig, axs = plt.subplots(len(sno_names), 1, figsize=(6, 10 * len(sno_names)), sharex=True)
    fig.subplots_adjust(hspace=0.5)

    for i, (sno_name, NM_location, Chimeras_dict) in enumerate(zip(sno_names, NM_locations, Chimeras_dicts)):
        create_graphs(sno_name, NM_location, Chimeras_dict)
        axs[i].set_title('Sno Name: {0}'.format(sno_name))
        plt.xlabel('Locations')
        plt.show()
