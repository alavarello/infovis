import matplotlib.pyplot as plt
import numpy as np
import pandas

w13 = [{"topping":"Mushrooms","total":65,"male":63,"female":68},
{"topping":"Onion","total":62,"male":62,"female":63},
{"topping":"Ham","total":61,"male":66,"female":56},
{"topping":"Peppers","total":60,"male":63,"female":57},
{"topping":"Chicken","total":56,"male":60,"female":52},
{"topping":"Pepperoni","total":56,"male":66,"female":46},
{"topping":"Tomato","total":51,"male":49,"female":54},
{"topping":"Bacon","total":49,"male":56,"female":43},
{"topping":"Pineapple","total":42,"male":40,"female":44},
{"topping":"Sweetcorn","total":42,"male":38,"female":46},
{"topping":"Beef","total":36,"male":47,"female":26},
{"topping":"Olives","total":33,"male":33,"female":32},
{"topping":"Chillies","total":31,"male":42,"female":22},
{"topping":"Jalapenos","total":30,"male":39,"female":21},
{"topping":"Spinach","total":26,"male":20,"female":32},
{"topping":"Pork","total":25,"male":34,"female":17},
{"topping":"Tuna","total":22,"male":23,"female":21},
{"topping":"Anchovies","total":18,"male":21,"female":15},
{"topping":"Something else","total":11,"male":12,"female":10}];

toppings = []
male = []
female = []
total = []

for topping in w13:
    toppings.append(topping['topping'])
    male.append(topping['male'])
    female.append(topping['female'])
    total.append(topping['total'])

df = pandas.DataFrame(dict(graph=toppings,
                           male=male, female=female))

ind = np.arange(len(df))
width = 0.4

fig, ax = plt.subplots()
ax.barh(ind, df.male, width, label='Male')
ax.barh(ind + width, df.female, width, label='Female')

ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
ax.legend()
ax.xaxis.grid(True)
plt.xlabel("%")
plt.ylabel("Toppings")
plt.title("UK's favorite pizza toppings", fontname='sans', fontsize=20)
plt.show()
