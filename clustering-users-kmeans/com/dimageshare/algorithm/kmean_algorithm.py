from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D


class KmeanAlgorithm(object):
    @staticmethod
    def read_data():
        root = Path(__file__).parent.parent.parent.parent
        df = pd.read_csv(str(root) + "/data/user.csv")
        df.head()

        return df

    @staticmethod
    def show_age_fregquency(df):
        plt.figure(figsize=(10, 6))
        plt.title('ages frequency')
        sns.axes_style('dark')
        sns.violinplot(y=df['age'])
        plt.show()

    @staticmethod
    def show_spendingscore_salary_frequency(df):
        plt.figure(figsize=(25, 10))
        plt.subplot(1, 2, 1)
        sns.boxplot(y=df["spending_score"], color="yellow")
        plt.subplot(1, 2, 2)
        sns.boxplot(y=df["salary"])
        plt.show()

    @staticmethod
    def show_gender_frequency(df):
        genders = df.gender.value_counts()
        sns.set_style("darkgrid")
        plt.figure(figsize=(20, 14))
        sns.barplot(x=genders.index, y=genders.values)
        plt.show()

    @staticmethod
    def show_age_count(df):
        age18_25 = df.age[(df.age <= 25) & (df.age >= 18)]
        age26_35 = df.age[(df.age <= 35) & (df.age >= 26)]
        age36_45 = df.age[(df.age <= 45) & (df.age >= 36)]
        age46_55 = df.age[(df.age <= 55) & (df.age >= 46)]
        age55above = df.age[df.age >= 56]

        x = ["18-25", "26-35", "36-45", "46-55", "55+"]
        y = [len(age18_25.values), len(age26_35.values), len(age36_45.values), len(age46_55.values),
             len(age55above.values)]

        plt.figure(figsize=(25, 16))
        sns.barplot(x=x, y=y, palette="rocket")
        plt.title("number of customer and ages")
        plt.xlabel("age")
        plt.ylabel("number of customer")
        plt.show()

    @staticmethod
    def show_spending_score_count(df):
        ss1_20 = df["spending_score"][
            (df["spending_score"] >= 1) & (df["spending_score"] <= 20)]
        ss21_40 = df["spending_score"][
            (df["spending_score"] >= 21) & (df["spending_score"] <= 40)]
        ss41_60 = df["spending_score"][
            (df["spending_score"] >= 41) & (df["spending_score"] <= 60)]
        ss61_80 = df["spending_score"][
            (df["spending_score"] >= 61) & (df["spending_score"] <= 80)]
        ss81_100 = df["spending_score"][
            (df["spending_score"] >= 81) & (df["spending_score"] <= 100)]

        ssx = ["1-20", "21-40", "41-60", "61-80", "81-100"]
        ssy = [len(ss1_20.values), len(ss21_40.values), len(ss41_60.values), len(ss61_80.values), len(ss81_100.values)]

        plt.figure(figsize=(20, 10))
        sns.barplot(x=ssx, y=ssy, palette="nipy_spectral_r")
        plt.title("Spending Scores")
        plt.xlabel("Score")
        plt.ylabel("Number of Customer Having the Score")
        plt.show()

    @staticmethod
    def show_salary_count(df):
        sl0_30 = df["salary"][(df["salary"] >= 0) & (df["salary"] <= 30)]
        sl31_60 = df["salary"][(df["salary"] >= 31) & (df["salary"] <= 60)]
        sl61_90 = df["salary"][(df["salary"] >= 61) & (df["salary"] <= 90)]
        sl91_120 = df["salary"][(df["salary"] >= 91) & (df["salary"] <= 120)]
        sl121_150 = df["salary"][(df["salary"] >= 121) & (df["salary"] <= 150)]

        slx = ["$ 0 - 30,000", "$ 30,001 - 60,000", "$ 60,001 - 90,000", "$ 90,001 - 120,000", "$ 120,001 - 150,000"]
        sly = [len(sl0_30.values), len(sl31_60.values), len(sl61_90.values), len(sl91_120.values),
               len(sl121_150.values)]

        plt.figure(figsize=(15, 6))
        sns.barplot(x=slx, y=sly, palette="Set2")
        plt.title("salary")
        plt.xlabel("results")
        plt.ylabel("number of user")
        plt.show()

    @staticmethod
    def kmean_clustering(df):
        km = KMeans(n_clusters=5)
        clusters = km.fit_predict(df.iloc[:, 2:])
        df["label"] = clusters
        return df

    @staticmethod
    def show_kmean_clustering(df):
        df = KmeanAlgorithm().kmean_clustering(df)
        fig = plt.figure(figsize=(20, 13))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(df.age[df.label == 0], df["salary"][df.label == 0],
                   df["spending_score"][df.label == 0], c='yellow', s=80)
        ax.scatter(df.age[df.label == 1], df["salary"][df.label == 1],
                   df["spending_score"][df.label == 1], c='red', s=80)
        ax.scatter(df.age[df.label == 2], df["salary"][df.label == 2],
                   df["spending_score"][df.label == 2], c='green', s=80)
        ax.scatter(df.age[df.label == 3], df["salary"][df.label == 3],
                   df["spending_score"][df.label == 3], c='black', s=80)
        ax.scatter(df.age[df.label == 4], df["salary"][df.label == 4],
                   df["spending_score"][df.label == 4], c='blue', s=80)
        ax.view_init(30, 185)
        plt.xlabel("age")
        plt.ylabel("salary")
        ax.set_zlabel('spending score (1-100)')
        plt.show()


# Show demo
if __name__ == '__main__':
    df = KmeanAlgorithm().read_data()

    KmeanAlgorithm().show_age_fregquency(df)
    KmeanAlgorithm().show_spendingscore_salary_frequency(df)
    KmeanAlgorithm().show_gender_frequency(df)
    KmeanAlgorithm().show_age_count(df)
    KmeanAlgorithm().show_spending_score_count(df)
    KmeanAlgorithm().show_salary_count(df)
    KmeanAlgorithm().show_kmean_clustering(df)
