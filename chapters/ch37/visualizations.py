import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizations:
    """
    데이터 시각화를 위한 클래스.
    `matplotlib`와 `seaborn`을 사용하여 다양한 플롯을 생성합니다.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_bar(self, x, y, title, filename="bar_plot.png"):
        """
        막대 그래프를 생성합니다.
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x, y=y, data=self.df)
        plt.title(title)
        plt.savefig(filename)
        plt.close() # 메모리 해제

    def plot_scatter(self, x, y, hue, title, filename="scatter_plot.png"):
        """
        산점도를 생성합니다.
        """
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x, y=y, hue=hue, data=self.df)
        plt.title(title)
        plt.savefig(filename)
        plt.close() # 메모리 해제

    def plot_hist(self, x, title, filename="hist_plot.png"):
        """
        히스토그램을 생성합니다.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df[x], kde=True)
        plt.title(title)
        plt.savefig(filename)
        plt.close() # 메모리 해제
