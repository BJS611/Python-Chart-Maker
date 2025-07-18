import pandas as pd
import matplotlib.pyplot as plt
import os

def tampilkan_kolom(df):
    print("\nKolom yang tersedia:")
    for i, col in enumerate(df.columns):
        print(f"{i + 1}. {col}")
    return df.columns

def buat_diagram(df, x_col, y_col, chart_type):
    if chart_type == "1":
        df.groupby(x_col)[y_col].sum().plot(kind='bar')
        plt.title("Diagram Batang")
    elif chart_type == "2":
        df.groupby(x_col)[y_col].sum().plot(kind='pie', autopct='%1.1f%%')
        plt.title("Diagram Lingkaran")
        plt.ylabel("")  # Hilangkan label Y
    elif chart_type == "3":
        df[y_col].plot(kind='hist', bins=20)
        plt.title("Histogram")
    elif chart_type == "4":
        df.sort_values(by=x_col).plot(x=x_col, y=y_col, kind='line')
        plt.title("Diagram Garis")
    else:
        print("Jenis diagram tidak dikenali.")
        return

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\n=== Program Visualisasi Data Excel ===")
        file_path = input("Masukkan path file Excel (misalnya: data.xlsx): ").strip()

        if not os.path.exists(file_path):
            print("File tidak ditemukan. Coba lagi.")
            continue

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            print("Gagal membaca file:", e)
            continue

        # Tampilkan kolom
        kolom = tampilkan_kolom(df)

        # Input kolom X dan Y
        try:
            x_index = int(input("Masukkan nomor kolom untuk sumbu X: ")) - 1
            y_index = int(input("Masukkan nomor kolom untuk sumbu Y: ")) - 1
            x_col = kolom[x_index]
            y_col = kolom[y_index]
        except:
            print("Input kolom tidak valid.")
            continue

        # Pilih jenis diagram
        print("\nPilih jenis diagram:")
        print("1. Diagram Batang (Bar Chart)")
        print("2. Diagram Lingkaran (Pie Chart)")
        print("3. Histogram")
        print("4. Diagram Garis (Line Chart)")
        chart_type = input("Masukkan nomor jenis diagram: ")

        try:
            buat_diagram(df, x_col, y_col, chart_type)
        except Exception as e:
            print("Gagal membuat diagram:", e)

        # Apakah ingin ulang?
        ulang = input("\nIngin memproses file lain? (y/n): ").lower()
        if ulang != 'y':
            break

if __name__ == "__main__":
    main()
