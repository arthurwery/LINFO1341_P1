# inspired from chatGPT
# modified by Nathan Zeep and Arthur Wery

import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ['appel simple', 'appel avec caméra', "partage d'écran"]
map = {
    "DNS"  :    [9,    10000,  494],
    "QUIC" :    [842,  2085,   1190],
    "RTCP" :    [123,  665,    389],
    "TCP"  :    [129,  57,     339],
    "TLS"  :    [445,  441,    2.06],
    "UDP"  :    [2819, 170000, 12000]
}

bar_width = 0.1
x_pos = np.arange(len(categories))

# Create a figure and axis object
fig, ax = plt.subplots()
i = -2
for key in map:
    ax.bar(x_pos + i*bar_width, map[key], width=bar_width, label=key)
    i += 1

# Set the title, axis labels and legend
ax.set_yscale('log')
ax.set_xlabel('Catégories')
ax.set_ylabel('Débit moyen [o/s]')
ax.set_xticks(x_pos + bar_width / 2)
ax.set_xticklabels(categories)
ax.legend()

plt.savefig("data.pdf", bbox_inches='tight')