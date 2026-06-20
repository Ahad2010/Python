import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 200, 300, 200]

plt.plot(months, sales, marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()