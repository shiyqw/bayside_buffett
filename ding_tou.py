import csv
total_eq = 0.
total_cost = 0.
prev_data_0 = 'hahahahaha'
with open('TQQQ.csv', 'r') as f:
    for l in f.readlines():
        data = l.split(',')
        if data[0][0:7] != prev_data_0[0:7]:
            print data[0:2]
            price = float(data[1])
            eq = 10000. / price
            total_eq += eq
            total_cost += 10000.
        prev_data_0 = data[0]

print total_eq
print total_cost

