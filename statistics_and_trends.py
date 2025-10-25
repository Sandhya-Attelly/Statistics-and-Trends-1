"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x="GPA",
        y="Statistics",
        hue="class",
        style="gender",
        alpha=0.8,
        palette="viridis"
    )
    plt.title("Relationship between GPA and Statistics by Class and Gender")
    plt.xlabel("GPA")
    plt.ylabel("Statistics Score")
    plt.tight_layout()
    plt.show()
    plt.savefig('relational_plot.png')
    return


def plot_categorical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(
        data=df,
        x="gender",
        y="GPA",
        hue="class",
        palette="Set2"
    )
    plt.title("GPA Distribution by Gender and Class")
    plt.xlabel("Gender")
    plt.ylabel("GPA")
    plt.tight_layout()
    plt.show()
    plt.savefig('categorical_plot.png')
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df["GPA"], kde=True, color="skyblue")
    plt.title("Distribution of GPA")
    plt.xlabel("GPA")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
    plt.savefig('statistical_plot.png')
    return


def statistical_analysis(df, col: str):
    series = df[col]
    mean = series.mean()
    stddev = series.std()
    skew = series.skew()
    excess_kurtosis = series.kurt()
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
 print("First five rows of data:")
 print(df.head())

 print("\nSummary statistics:")
 print(df.describe())

 print("\nMissing values per column:")
 print(df.isnull().sum()) 
 return df


def writing(moments, col):

    mean, stddev, skew, excess_kurtosis = moments 
    print(f"\nFor the attribute '{col}':")
    print(f"Mean = {mean:.2f}")
    print(f"Standard Deviation = {stddev:.2f}")
    print(f"Skewness = {skew:.2f}")
    print(f"Excess Kurtosis = {excess_kurtosis:.2f}")

    if skew > 0.5:
        skew_text = "right-skewed"
    elif skew < -0.5:
        skew_text = "left-skewed"
    else:
        skew_text = "approximately symmetric"

  
    if excess_kurtosis > 1:
        kurt_text = "leptokurtic (heavy tails)"
    elif excess_kurtosis < -1:
        kurt_text = "platykurtic (light tails)"
    else:
        kurt_text = "mesokurtic (normal tails)"

    print(f"The data is {skew_text} and {kurt_text}.")
    return

   


def main():
    df = pd.read_csv('data.csv')
    df = preprocessing(df)
    col = 'GPA'
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
