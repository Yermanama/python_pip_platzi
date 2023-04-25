import matplotlib.pyplot as plt
import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)


def generate_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()