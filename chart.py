if __name__ == "__main__":
    print("=== PROGRAM PEMBUAT CHART ===\n")
    
    while True:
        print("\nPilihan:")
        print("1. Lihat demo semua chart")
        print("2. Buat chart custom")
        print("3. Buat file contoh data")
        print("4. Analisis statistik data")
        print("5. Keluar")
        
        choice = input("\nMasukkan pilihan (1-5): ")
        
        if choice == "1":
            demo_charts()
        elif choice == "2":
            create_custom_chart()
        elif choice == "3":
            create_sample_file()
        elif choice == "4":
            data_statistics()
        elif choice == "5":
            print("Terima kasih telah menggunakan Chart Maker!")
            break
        else:
            print("Pilihan tidak valid!") 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class ChartMaker:
    def __init__(self):
        plt.style.use('seaborn-v0_8')  # Menggunakan style yang lebih modern
        self.fig_size = (10, 6)
        
    def line_chart(self, x_data, y_data, title="Line Chart", xlabel="X", ylabel="Y", save_path=None):
        """Membuat line chart"""
        plt.figure(figsize=self.fig_size)
        plt.plot(x_data, y_data, marker='o', linewidth=2, markersize=6)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def bar_chart(self, categories, values, title="Bar Chart", xlabel="Categories", ylabel="Values", save_path=None):
        """Membuat bar chart"""
        plt.figure(figsize=self.fig_size)
        bars = plt.bar(categories, values, color='skyblue', edgecolor='navy', alpha=0.7)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=45)
        
        # Menambahkan nilai di atas setiap bar
        for bar, value in zip(bars, values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01*max(values),
                    f'{value:.1f}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def pie_chart(self, labels, sizes, title="Pie Chart", save_path=None):
        """Membuat pie chart"""
        plt.figure(figsize=(8, 8))
        colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
        wedges, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', 
                                          colors=colors, startangle=90, shadow=True)
        
        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('equal')
        
        # Memperbaiki tampilan teks
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def scatter_plot(self, x_data, y_data, title="Scatter Plot", xlabel="X", ylabel="Y", save_path=None):
        """Membuat scatter plot"""
        plt.figure(figsize=self.fig_size)
        plt.scatter(x_data, y_data, alpha=0.6, s=50, c='red', edgecolors='black')
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def histogram(self, data, bins=20, title="Histogram", xlabel="Values", ylabel="Frequency", save_path=None):
        """Membuat histogram"""
        plt.figure(figsize=self.fig_size)
        plt.hist(data, bins=bins, color='lightgreen', edgecolor='darkgreen', alpha=0.7)
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def multiple_line_chart(self, x_data, y_data_dict, title="Multiple Line Chart", 
                           xlabel="X", ylabel="Y", save_path=None):
        """Membuat chart dengan multiple lines"""
        plt.figure(figsize=self.fig_size)
        
        for label, y_data in y_data_dict.items():
            plt.plot(x_data, y_data, marker='o', linewidth=2, label=label)
        
        plt.title(title, fontsize=16, fontweight='bold')
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()

def demo_charts():
    """Fungsi demo untuk menunjukkan berbagai jenis chart"""
    chart_maker = ChartMaker()
    
    # Data contoh
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [100, 150, 200, 180, 220, 250]
    
    # Line Chart
    print("Membuat Line Chart...")
    chart_maker.line_chart(months, sales, "Penjualan Bulanan", "Bulan", "Penjualan (juta)")
    
    # Bar Chart
    print("Membuat Bar Chart...")
    products = ['Produk A', 'Produk B', 'Produk C', 'Produk D']
    revenue = [300, 450, 200, 350]
    chart_maker.bar_chart(products, revenue, "Pendapatan per Produk", "Produk", "Pendapatan (juta)")
    
    # Pie Chart
    print("Membuat Pie Chart...")
    categories = ['Marketing', 'Development', 'Sales', 'Support']
    budget = [30, 40, 20, 10]
    chart_maker.pie_chart(categories, budget, "Distribusi Budget")
    
    # Scatter Plot
    print("Membuat Scatter Plot...")
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100) * 0.5
    chart_maker.scatter_plot(x, y, "Korelasi X vs Y", "X", "Y")
    
    # Histogram
    print("Membuat Histogram...")
    data = np.random.normal(100, 15, 1000)
    chart_maker.histogram(data=data, bins=30, title="Distribusi Data", xlabel="Nilai", ylabel="Frekuensi")
    
    # Multiple Line Chart
    print("Membuat Multiple Line Chart...")
    x = np.linspace(0, 10, 100)
    y_data = {
        'sin(x)': np.sin(x),
        'cos(x)': np.cos(x),
        'sin(2x)': np.sin(2*x)
    }
    chart_maker.multiple_line_chart(x, y_data, "Fungsi Trigonometri", "X", "Y")

def get_chart_labels():
    """Mendapatkan label untuk chart dari user"""
    title = input("Masukkan judul chart: ") or "Chart"
    xlabel = input("Masukkan label sumbu X: ") or "X"
    ylabel = input("Masukkan label sumbu Y: ") or "Y"
    return title, xlabel, ylabel

def get_save_option():
    """Menanyakan apakah user ingin menyimpan chart"""
    save = input("Simpan chart sebagai file? (y/n): ").lower()
    if save == 'y':
        filename = input("Masukkan nama file (tanpa ekstensi): ") or "chart"
        return f"{filename}.png"
    return None

def input_data_manual():
    """Input data secara manual"""
    print("\n=== INPUT DATA MANUAL ===")
    
    # Pilih metode input
    print("1. Input satu per satu")
    print("2. Input sekaligus (pisahkan dengan koma)")
    method = input("Pilih metode input (1/2): ")
    
    if method == "1":
        # Input satu per satu
        print("Masukkan data (tekan Enter kosong untuk selesai):")
        data = []
        i = 1
        while True:
            value = input(f"Data ke-{i}: ")
            if value == "":
                break
            try:
                data.append(float(value))
                i += 1
            except ValueError:
                print("Masukkan angka yang valid!")
        return data
    
    else:
        # Input sekaligus
        data_input = input("Masukkan data (pisahkan dengan koma): ")
        try:
            data = [float(x.strip()) for x in data_input.split(',')]
            return data
        except ValueError:
            print("Format data tidak valid!")
            return []

def input_categorical_data():
    """Input data kategori dan nilai"""
    print("\n=== INPUT DATA KATEGORI ===")
    
    categories = []
    values = []
    
    print("Masukkan kategori dan nilai (tekan Enter kosong untuk selesai):")
    i = 1
    while True:
        category = input(f"Kategori ke-{i}: ")
        if category == "":
            break
        
        try:
            value = float(input(f"Nilai untuk '{category}': "))
            categories.append(category)
            values.append(value)
            i += 1
        except ValueError:
            print("Masukkan angka yang valid!")
    
    return categories, values

def read_from_file():
    """Membaca data dari file"""
    print("\n=== BACA DATA DARI FILE ===")
    print("Format file yang didukung: .txt, .csv")
    print("Format data dalam file:")
    print("- Untuk data tunggal: satu nilai per baris")
    print("- Untuk data kategori: kategori,nilai per baris")
    
    filename = input("Masukkan nama file: ")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Deteksi format file
        if ',' in lines[0]:
            # Format kategori,nilai
            categories = []
            values = []
            for line in lines:
                if line.strip():
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        categories.append(parts[0].strip())
                        values.append(float(parts[1].strip()))
            return categories, values
        else:
            # Format data tunggal
            data = []
            for line in lines:
                if line.strip():
                    data.append(float(line.strip()))
            return data
            
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan!")
        return None
    except Exception as e:
        print(f"Error membaca file: {e}")
        return None

def create_custom_chart():
    """Fungsi untuk membuat chart dengan data custom"""
    chart_maker = ChartMaker()
    
    print("\n=== CHART MAKER INTERAKTIF ===")
    print("1. Line Chart")
    print("2. Bar Chart")
    print("3. Pie Chart")
    print("4. Scatter Plot")
    print("5. Histogram")
    print("6. Multiple Line Chart")
    
    choice = input("\nPilih jenis chart (1-6): ")
    
    if choice == "1":
        # Line Chart
        print("\n=== MEMBUAT LINE CHART ===")
        print("Pilih sumber data:")
        print("1. Input manual")
        print("2. Baca dari file")
        
        source = input("Pilih sumber (1/2): ")
        
        if source == "1":
            print("Data X:")
            x_data = input_data_manual()
            print("Data Y:")
            y_data = input_data_manual()
            
            if len(x_data) != len(y_data):
                print("Jumlah data X dan Y harus sama!")
                return
                
        elif source == "2":
            print("Format file: x,y per baris")
            data = read_from_file()
            if data and len(data) == 2:
                x_data, y_data = data
            else:
                print("Format file tidak sesuai!")
                return
        else:
            print("Pilihan tidak valid!")
            return
        
        title, xlabel, ylabel = get_chart_labels()
        save_path = get_save_option()
        
        chart_maker.line_chart(x_data, y_data, title, xlabel, ylabel, save_path)
        
    elif choice == "2":
        # Bar Chart
        print("\n=== MEMBUAT BAR CHART ===")
        print("Pilih sumber data:")
        print("1. Input manual")
        print("2. Baca dari file")
        
        source = input("Pilih sumber (1/2): ")
        
        if source == "1":
            categories, values = input_categorical_data()
        elif source == "2":
            data = read_from_file()
            if data and len(data) == 2:
                categories, values = data
            else:
                print("Format file tidak sesuai!")
                return
        else:
            print("Pilihan tidak valid!")
            return
        
        title, xlabel, ylabel = get_chart_labels()
        save_path = get_save_option()
        
        chart_maker.bar_chart(categories, values, title, xlabel, ylabel, save_path)
        
    elif choice == "3":
        # Pie Chart
        print("\n=== MEMBUAT PIE CHART ===")
        print("Pilih sumber data:")
        print("1. Input manual")
        print("2. Baca dari file")
        
        source = input("Pilih sumber (1/2): ")
        
        if source == "1":
            labels, sizes = input_categorical_data()
        elif source == "2":
            data = read_from_file()
            if data and len(data) == 2:
                labels, sizes = data
            else:
                print("Format file tidak sesuai!")
                return
        else:
            print("Pilihan tidak valid!")
            return
        
        title = input("Masukkan judul chart: ") or "Pie Chart"
        save_path = get_save_option()
        
        chart_maker.pie_chart(labels, sizes, title, save_path)
        
    elif choice == "4":
        # Scatter Plot
        print("\n=== MEMBUAT SCATTER PLOT ===")
        print("Pilih sumber data:")
        print("1. Input manual")
        print("2. Baca dari file")
        
        source = input("Pilih sumber (1/2): ")
        
        if source == "1":
            print("Data X:")
            x_data = input_data_manual()
            print("Data Y:")
            y_data = input_data_manual()
            
            if len(x_data) != len(y_data):
                print("Jumlah data X dan Y harus sama!")
                return
                
        elif source == "2":
            data = read_from_file()
            if data and len(data) == 2:
                x_data, y_data = data
            else:
                print("Format file tidak sesuai!")
                return
        else:
            print("Pilihan tidak valid!")
            return
        
        title, xlabel, ylabel = get_chart_labels()
        save_path = get_save_option()
        
        chart_maker.scatter_plot(x_data, y_data, title, xlabel, ylabel, save_path)
        
    elif choice == "5":
        # Histogram
        print("\n=== MEMBUAT HISTOGRAM ===")
        print("Pilih sumber data:")
        print("1. Input manual")
        print("2. Baca dari file")
        
        source = input("Pilih sumber (1/2): ")
        
        if source == "1":
            data = input_data_manual()
        elif source == "2":
            data = read_from_file()
            if isinstance(data, tuple):
                data = data[1]  # Ambil nilai jika format kategori,nilai
        else:
            print("Pilihan tidak valid!")
            return
        
        bins = input("Masukkan jumlah bins (default 20): ")
        bins = int(bins) if bins.isdigit() else 20
        
        title, xlabel, ylabel = get_chart_labels()
        save_path = get_save_option()
        
        chart_maker.histogram(data, bins, title, xlabel, ylabel, save_path)
        
    elif choice == "6":
        # Multiple Line Chart
        print("\n=== MEMBUAT MULTIPLE LINE CHART ===")
        print("Data X:")
        x_data = input_data_manual()
        
        y_data_dict = {}
        print("\nMasukkan multiple data Y (tekan Enter kosong untuk selesai):")
        i = 1
        while True:
            label = input(f"Label untuk data Y ke-{i} (kosong untuk selesai): ")
            if label == "":
                break
            
            print(f"Data Y untuk '{label}':")
            y_data = input_data_manual()
            
            if len(y_data) != len(x_data):
                print(f"Jumlah data Y untuk '{label}' harus sama dengan data X!")
                continue
            
            y_data_dict[label] = y_data
            i += 1
        
        if not y_data_dict:
            print("Tidak ada data Y yang diinput!")
            return
        
        title, xlabel, ylabel = get_chart_labels()
        save_path = get_save_option()
        
        chart_maker.multiple_line_chart(x_data, y_data_dict, title, xlabel, ylabel, save_path)
        
    else:
        print("Pilihan tidak valid!")

def create_sample_file():
    """Membuat file contoh untuk membantu user"""
    print("\n=== MEMBUAT FILE CONTOH ===")
    print("1. File data tunggal (untuk histogram)")
    print("2. File data kategori (untuk bar/pie chart)")
    print("3. File data X,Y (untuk line/scatter plot)")
    
    choice = input("Pilih jenis file contoh (1-3): ")
    
    if choice == "1":
        # File data tunggal
        filename = input("Nama file (tanpa ekstensi): ") or "data_tunggal"
        with open(f"{filename}.txt", 'w') as f:
            sample_data = [23, 45, 56, 78, 32, 44, 67, 89, 12, 34, 56, 78, 90, 23, 45]
            for value in sample_data:
                f.write(f"{value}\n")
        print(f"File '{filename}.txt' berhasil dibuat!")
        
    elif choice == "2":
        # File data kategori
        filename = input("Nama file (tanpa ekstensi): ") or "data_kategori"
        with open(f"{filename}.csv", 'w') as f:
            f.write("Produk A,150\n")
            f.write("Produk B,230\n")
            f.write("Produk C,180\n")
            f.write("Produk D,320\n")
            f.write("Produk E,95\n")
        print(f"File '{filename}.csv' berhasil dibuat!")
        
    elif choice == "3":
        # File data X,Y
        filename = input("Nama file (tanpa ekstensi): ") or "data_xy"
        with open(f"{filename}.csv", 'w') as f:
            for i in range(1, 11):
                f.write(f"{i},{i*2 + np.random.randint(-5, 5)}\n")
        print(f"File '{filename}.csv' berhasil dibuat!")
        
    else:
        print("Pilihan tidak valid!")

def data_statistics():
    """Menampilkan statistik data yang diinput"""
    print("\n=== STATISTIK DATA ===")
    print("Pilih sumber data:")
    print("1. Input manual")
    print("2. Baca dari file")
    
    source = input("Pilih sumber (1/2): ")
    
    if source == "1":
        data = input_data_manual()
    elif source == "2":
        data = read_from_file()
        if isinstance(data, tuple):
            data = data[1]  # Ambil nilai jika format kategori,nilai
    else:
        print("Pilihan tidak valid!")
        return
    
    if not data:
        print("Tidak ada data untuk dianalisis!")
        return
    
    # Hitung statistik
    import statistics
    
    print(f"\n=== HASIL STATISTIK ===")
    print(f"Jumlah data: {len(data)}")
    print(f"Nilai minimum: {min(data):.2f}")
    print(f"Nilai maksimum: {max(data):.2f}")
    print(f"Rata-rata: {statistics.mean(data):.2f}")
    print(f"Median: {statistics.median(data):.2f}")
    
    try:
        print(f"Modus: {statistics.mode(data):.2f}")
    except:
        print("Modus: Tidak ada (semua nilai unik)")
    
    if len(data) > 1:
        print(f"Standar deviasi: {statistics.stdev(data):.2f}")
        print(f"Varians: {statistics.variance(data):.2f}")
    
    # Tanya apakah ingin membuat chart
    make_chart = input("\nBuat histogram dari data ini? (y/n): ").lower()
    if make_chart == 'y':
        chart_maker = ChartMaker()
        bins = input("Masukkan jumlah bins (default 20): ")
        bins = int(bins) if bins.isdigit() else 20
        
        title = input("Masukkan judul chart: ") or "Histogram Data"
        xlabel = input("Masukkan label sumbu X: ") or "Nilai"
        ylabel = input("Masukkan label sumbu Y: ") or "Frekuensi"
        
        save_path = get_save_option()
        chart_maker.histogram(data, bins, title, xlabel, ylabel, save_path)