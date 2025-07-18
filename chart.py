import pandas as pd
import matplotlib.pyplot as plt
import os

def load_excel_file():
    file_path = input("Enter the path to your Excel file (.xlsx): ").strip()
    if not os.path.exists(file_path):
        print("File not found. Please check the path.")
        return None

    try:
        xls = pd.ExcelFile(file_path)
        print("\nAvailable sheets:", xls.sheet_names)
        sheet_name = input("Enter sheet name to load: ").strip()
        df = pd.read_excel(xls, sheet_name=sheet_name)
        print("Data loaded successfully.\n")
        print("Columns found:", list(df.columns))
        return df
    except Exception as e:
        print("Error reading Excel file:", e)
        return None

def select_columns(df, chart_type):
    print("\nAvailable columns:")
    for idx, col in enumerate(df.columns):
        print(f"{idx+1}. {col}")

    if chart_type in ['bar', 'line', 'histogram']:
        x_col = input("Enter column name for X-axis: ").strip()
        y_col = input("Enter column name for Y-axis: ").strip()
        return x_col, y_col
    elif chart_type == 'pie':
        label_col = input("Enter column name for labels: ").strip()
        value_col = input("Enter column name for values: ").strip()
        return label_col, value_col
    else:
        return None, None

def create_chart(df, chart_type, col1, col2):
    plt.figure(figsize=(10,6))
    title = f"{chart_type.title()} Chart of {col2} vs {col1}"

    try:
        if chart_type == 'bar':
            plt.bar(df[col1], df[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
        elif chart_type == 'line':
            plt.plot(df[col1], df[col2], marker='o')
            plt.xlabel(col1)
            plt.ylabel(col2)
        elif chart_type == 'histogram':
            plt.hist(df[col2], bins=30)
            plt.xlabel(col2)
            plt.ylabel("Frequency")
        elif chart_type == 'pie':
            plt.pie(df[col2], labels=df[col1], autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
        else:
            print("Unsupported chart type.")
            return

        plt.title(title)
        plt.tight_layout()
        file_name = f"{chart_type}_chart.png"
        plt.savefig(file_name)
        plt.show()
        print(f"Chart saved as: {file_name}")
    except Exception as e:
        print("Failed to generate chart:", e)

def main():
    print("=== Office Chart Generator ===")
    df = load_excel_file()
    if df is None:
        return

    print("\nSelect Chart Type:")
    print("1. Bar")
    print("2. Line")
    print("3. Pie")
    print("4. Histogram")
    choice = input("Enter chart type number: ").strip()

    chart_map = {
        "1": "bar",
        "2": "line",
        "3": "pie",
        "4": "histogram"
    }

    chart_type = chart_map.get(choice)
    if not chart_type:
        print("Invalid chart type.")
        return

    col1, col2 = select_columns(df, chart_type)
    if col1 not in df.columns or col2 not in df.columns:
        print("Invalid column names.")
        return

    create_chart(df, chart_type, col1, col2)

if __name__ == "__main__":
    main()
