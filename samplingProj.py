import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics as stats
import random

df = pd.read_csv("tempData.csv")
temps = df["temp"].tolist()
population_mean = stats.mean(temps)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(temps))
        value = temps[random_index]
        dataset.append(value)
    mean = stats.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(1, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean_of_sample = stats.mean(mean_list)

def show_fig(mean_list):
    graph_data = mean_list
    fig = ff.create_distplot([graph_data], ["temp"], show_hist = False)
    fig.show()

setup()