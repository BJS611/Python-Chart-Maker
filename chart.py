import pandas as pd
import matplotlib.pyplot as plt
import os

def tampilkan_kolom(df, lang):
    print("\nAvailable columns:" if lang == 'en' else "\nKolom yang tersedia:")
    for i, col in enumerate(df.columns):
        print(f"{i + 1}. {col}")
    return df.columns

def buat_diagram(df, x_col, y_col, chart_type, lang):
    title_map = {
        "1": "Bar Chart" if lang == 'en' else "Diagram Batang",
        "2": "Pie Chart" if lang == 'en' else "Diagram Lingkaran",
        "3": "Histogram",
        "4": "Line Chart" if lang == 'en' else "Diagram Garis"
    }

    try:
        if chart_type == "1":
            df.groupby(x_col)[y_col].sum().plot(kind='bar')
        elif chart_type == "2":
            df.groupby(x_col)[y_col].sum().plot(kind='pie', autopct='%1.1f%%')
            plt.ylabel("")
        elif chart_type == "3":
            df[y_col].plot(kind='hist', bins=20)
        elif chart_type == "4":
            df.sort_values(by=x_col).plot(x=x_col, y=y_col, kind='line')
        else:
            print("Unknown chart type." if lang == 'en' else "Jenis diagram tidak dikenali.")
            return

        plt.title(title_map.get(chart_type, "Chart"))
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print("Error creating chart:" if lang == 'en' else "Gagal membuat diagram:", e)

def main():
    print("=== Select Language / Pilih Bahasa ===")
    print("1. English")
    print("2. Bahasa Indonesia")
    lang_input = input("Enter number / Masukkan nomor: ")
    lang = 'en' if lang_input == '1' else 'id'

    while True:
        print("\n=== Excel Data Visualization Program ===" if lang == 'en' else "\n=== Program Visualisasi Data Excel ===")
        file_path = input("Enter Excel file path (e.g., data.xlsx): " if lang == 'en' else "Masukkan path file Excel (misalnya: data.xlsx): ").strip()

        if not os.path.exists(file_path):
            print("File not found. Try again." if lang == 'en' else "File tidak ditemukan. Coba lagi.")
            continue

        try:
            df = pd.read_excel(file_path)
        except Exception as e:
            print("Failed to read file:" if lang == 'en' else "Gagal membaca file:", e)
            continue

        # Tampilkan kolom
        kolom = tampilkan_kolom(df, lang)

        # Input kolom X dan Y
        try:
            x_index = int(input("Enter X-axis column number: " if lang == 'en' else "Masukkan nomor kolom untuk sumbu X: ")) - 1
            y_index = int(input("Enter Y-axis column number: " if lang == 'en' else "Masukkan nomor kolom untuk sumbu Y: ")) - 1
            x_col = kolom[x_index]
            y_col = kolom[y_index]
        except:
            print("Invalid column input." if lang == 'en' else "Input kolom tidak valid.")
            continue

        # Pilih jenis diagram
        print("\nChoose chart type:" if lang == 'en' else "\nPilih jenis diagram:")
        print("1. Bar Chart" if lang == 'en' else "1. Diagram Batang")
        print("2. Pie Chart" if lang == 'en' else "2. Diagram Lingkaran")
        print("3. Histogram")
        print("4. Line Chart" if lang == 'en' else "4. Diagram Garis")
        chart_type = input("Enter number of chart type: " if lang == 'en' else "Masukkan nomor jenis diagram: ")

        buat_diagram(df, x_col, y_col, chart_type, lang)

        # Apakah ingin ulang?
        ulang = input("\nProcess another file? (y/n): " if lang == 'en' else "\nIngin memproses file lain? (y/n): ").lower()
        if ulang != 'y':
            print("Goodbye!" if lang == 'en' else "Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
