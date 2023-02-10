import pandas as pd


df = pd.read_csv(r'goods.csv')
data = pd.DataFrame(df, columns=['Copper'])


copper_prices = data.values.tolist()


differences = []

for i in range (1, len(copper_prices)-1):
    current_value = copper_prices[i][0]
    previous_value = copper_prices[i-1][0]

    difference = abs(current_value - previous_value)
    differences.append(difference)



d = {'col': differences}

d = pd.DataFrame(data=d)



stdev = d.std()

print(stdev)

average = sum(differences)/len(differences)

print(average)




