import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_csv(path):
    try:
        df = pd.read_csv(path)
        print(f"\n✓ Successfully loaded: {path}\n")
        return df
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def show_summary(df):
    print("\n===== SUMMARY STATISTICS =====\n")
    print(df.describe(include='all'))

def show_info(df):
    print("\n===== DATA INFO =====\n")
    print(df.info())

def missing_report(df):
    print("\n===== MISSING VALUE REPORT =====\n")
    print(df.isnull().sum())

def plot_histograms(df):
    print("\nGenerating histograms...\n")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    for col in numeric_cols:
        df[col].plot(kind='hist')
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.savefig(f"hist_{col}.png")
        plt.close()
    print("✓ Histograms saved as hist_*.png")

def plot_bar(df):
    print("\nGenerating bar plots for categorical columns...\n")
    cat_cols = df.select_dtypes(include=['object']).columns
    
    for col in cat_cols:
        df[col].value_counts().plot(kind='bar')
        plt.title(f"Bar Plot of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.savefig(f"bar_{col}.png")
        plt.close()
    print("✓ Bar plots saved as bar_*.png")

def plot_correlation(df):
    print("\nGenerating correlation heatmap...\n")
    numeric = df.select_dtypes(include=['int64', 'float64'])
    corr = numeric.corr()
    
    plt.imshow(corr, cmap='viridis')
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title("Correlation Heatmap")
    plt.savefig("correlation_heatmap.png")
    plt.close()

    print("✓ Correlation heatmap saved as correlation_heatmap.png")

def menu():
    print("""
==============================
   CSV DATA EXPLORER TOOL
==============================

1. Summary statistics
2. Data info
3. Missing value report
4. Plot histograms
5. Plot bar charts
6. Correlation heatmap
7. Exit
""")

if __name__ == "__main__":
    path = input("Enter CSV file path: ")
    df = load_csv(path)

    while True:
        menu()
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            show_summary(df)
        elif choice == '2':
            show_info(df)
        elif choice == '3':
            missing_report(df)
        elif choice == '4':
            plot_histograms(df)
        elif choice == '5':
            plot_bar(df)
        elif choice == '6':
            plot_correlation(df)
        elif choice == '7':
            print("Bye! 👋")
            break
        else:
            print("Invalid option, try again!")
