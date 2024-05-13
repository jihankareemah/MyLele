import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image
import PIL

import tkinter
from tkinter import ttk,messagebox
import mysql.connector

from tkinter.ttk import *
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askinteger

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="budidaya"
)

#MEMBUAT JENDELA UTAMA 
window = ctk.CTk()
window.title('MyLele')
window.geometry(f'1250x720')
window.resizable(width=False, height=False)
ctk.set_appearance_mode("light") 

head = ctk.CTkFrame(window, border_width=3, fg_color="LIGHT BLUE", 
                    border_color="white")
head.pack(side=ctk.TOP, fill=ctk.X)
head.pack_propagate(False)
head.configure(height=80)

frame_utama=ctk.CTkFrame(master=window, width=1250, height=660, corner_radius=15, 
                         fg_color="white", bg_color="white")
frame_utama.place(relx=0.5, rely=0.540, anchor=tkinter.CENTER)

def home():
    home_frame=ctk.CTkFrame(master=frame_utama, width=1250, height=650, corner_radius=15, 
                            fg_color="white", bg_color="white")
    home_frame.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)
    
    judul = ctk.CTkLabel(master=home_frame, text="Selamat Datang di Aplikasi MyLele!", 
                          font=('Arial', 24, "bold"), text_color="#326497")
    judul.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    
    deskripsi = ctk.CTkLabel(master=home_frame, 
                             text="MyLele adalah aplikasi yang dirancang untuk membantu Anda menghitung laba rugi dari penjualan lele dan mengelola data lele yang Anda budidayakan. Dengan MyLele, Anda dapat dengan mudah melacak biaya pengeluaran seperti biaya bibit, pakan, obat-obatan, dan biaya perawatan, serta menghitung pendapatan dari penjualan lele berdasarkan harga jual per kilogram. Aplikasi ini juga memberikan saran tentang harga jual yang optimal untuk mencapai keuntungan maksimum.", 
                             font=('Arial', 16, "bold"), text_color="#326497", width=70, wraplength=1000, justify="center")
    deskripsi.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Panggil fungsi home di sini
home()

mycursor = db.cursor()

def tambah():
    JUMLAH_LELE = ""
    MASA_PANEN = ""
    HARGA_JUAL = ""
    BIAYA_BIBIT = ""
    BIAYA_PAKAN = ""
    BIAYA_OBAT = ""
    BIAYA_PERAWATAN = ""

    tambah_frame=ctk.CTkFrame(master=frame_utama, width=1250, height=680, corner_radius=15, fg_color="white", bg_color="white")
    tambah_frame.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)
    label_judul=ctk.CTkLabel(master=tambah_frame, text="Tambah Data Lele",font=('Century Gothic',30), text_color="#326497")
    label_judul.place(x=470, y=40)

    jumlah_lele_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Jumlah Lele', border_color="#326497")
    jumlah_lele_entry.place(x=200, y=165)

    masa_panen_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Masa Panen', border_color="#326497")
    masa_panen_entry.place(x=650, y=165)

    harga_jual_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Harga Jual (/kg)', border_color="#326497")
    harga_jual_entry.place(x=200, y=220)

    biaya_bibit_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Bibit (/pcs)', border_color="#326497")
    biaya_bibit_entry.place(x=650, y=220)

    biaya_pakan_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Pakan', border_color="#326497")
    biaya_pakan_entry.place(x=200, y=275)

    biaya_obat_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Obat', border_color="#326497")
    biaya_obat_entry.place(x=650, y=275)

    biaya_perawatan_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Perawatan', border_color="#326497")
    biaya_perawatan_entry.place(x=200, y=330)

    tambah_button = ctk.CTkButton(master=tambah_frame, text="Tambah Data", fg_color="#326497", hover_color="purple", width=220, command=tombol_click)
    tambah_button.place(x=470, y=400)

def tombol_click():
    global jumlah_lele, masa_panen, harga_jual, biaya_bibit, biaya_pakan, biaya_obat, biaya_perawatan
    jumlah_lele = jumlah_lele_entry.get()
    masa_panen = masa_panen_entry.get()
    harga_jual = harga_jual_entry.get()
    biaya_bibit = biaya_bibit_entry.get()
    biaya_pakan = biaya_pakan_entry.get()
    biaya_obat = biaya_obat_entry.get()
    biaya_perawatan = biaya_perawatan_entry.get()

    if jumlah_lele and masa_panen and harga_jual and biaya_bibit and biaya_pakan and biaya_obat and biaya_perawatan:
        try:
            mycursor.execute("INSERT INTO datalele (jumlah_lele, masa_panen, harga_jual, biaya_bibit, biaya_pakan, biaya_obat, biaya_perawatan) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            (jumlah_lele, masa_panen, harga_jual, biaya_bibit, biaya_pakan, biaya_obat, biaya_perawatan))
            db.commit()
            pesan = f"Berhasil Menambahkan data"
            messagebox.showinfo(title="Berhasil", message=pesan)
            # refresh_data()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            db.rollback()
            pesan = f"Error: {err}"
            messagebox.showerror(title="Error", message=pesan)
    else:
        pesan = "Pastikan input sesuai dengan kriteria yang diminta!"
        messagebox.showerror(title="Error", message=pesan)

tambah_frame=ctk.CTkFrame(master=frame_utama, width=1250, height=680, corner_radius=15, fg_color="white", bg_color="white")
tambah_frame.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)
label_judul=ctk.CTkLabel(master=tambah_frame, text="Tambah Data Lele",font=('Century Gothic',30), text_color="blue")
label_judul.place(x=470, y=40)


jumlah_lele_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Jumlah Lele', border_color="blue")
jumlah_lele_entry.place(x=200, y=165)

masa_panen_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Masa Panen', border_color="blue")
masa_panen_entry.place(x=650, y=165)

harga_jual_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Harga Jual (/kg)', border_color="blue")
harga_jual_entry.place(x=200, y=220)

biaya_bibit_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Bibit (/pcs)', border_color="blue")
biaya_bibit_entry.place(x=650, y=220)

biaya_pakan_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Pakan', border_color="blue")
biaya_pakan_entry.place(x=200, y=275)

biaya_obat_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Obat', border_color="blue")
biaya_obat_entry.place(x=650, y=275)

biaya_perawatan_entry=ctk.CTkEntry(master=tambah_frame, width=350, placeholder_text='Masukkan Biaya Perawatan', border_color="blue")
biaya_perawatan_entry.place(x=200, y=330)


def data_lele():
        # Menampilkan data yang sudah dimasukkan ke dalam Treeview
        data_frame1 = ctk.CTkFrame(master=frame_utama, width=1250, height=680, corner_radius=15, fg_color="white", bg_color="white")
        data_frame1.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)
        data_frame = ctk.CTkFrame(master=frame_utama, width=1250, height=680, corner_radius=15, fg_color="white", bg_color="white")
        data_frame.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)
        label_judul = ctk.CTkLabel(master=data_frame1, text="Data Lele", font=('Century Gothic',30), text_color="blue")
        label_judul.place(x=550, y=40)

        # Create TreeView Lele
        columns = ("jumlah_lele", "masa_panen", "harga_jual", "biaya_bibit", "biaya_pakan", "biaya_obat", "biaya_perawatan")
        tree = Treeview(data_frame, columns=columns, height=20, padding=3)
        tree.pack(padx=5, pady=5)
        tree.column("#0", anchor="center", width=50)
        tree.heading("#0", text="ID")

        # Existing columns
        for col in columns:
            tree.column(col, anchor="w", width=150)
            tree.heading(col, text=col)

        # Ambil data dari database dan masukkan ke dalam Treeview
        mycursor.execute("SELECT * FROM datalele")
        myresult = mycursor.fetchall()

        for i, line in enumerate(myresult):
            tree.insert('', END, iid=i, text=line[0], values=line[1:])

def costs():
    # Buat frame baru untuk menampilkan total biaya
    costs_frame1 = ctk.CTkFrame(master=frame_utama, width=1250, height=680, corner_radius=15, fg_color="white", bg_color="white")
    costs_frame1.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)
    label_judul1 = ctk.CTkLabel(master=costs_frame1, text="Total Biaya", font=('Century Gothic',30), text_color="blue")
    label_judul1.place(x=550, y=40)

    costs_frame = ctk.CTkFrame(master=frame_utama, width=1250, height=680, corner_radius=15, fg_color="white", bg_color="white")
    costs_frame.place(relx=0.5, rely=0.49, anchor=tkinter.CENTER)

    # Create TreeView Costs
    columns = ("ID", "Harga Jual per kg", "Biaya Bibit", "Biaya Pakan", "Biaya Obat", "Biaya Perawatan", "Pendapatan", "Pengeluaran", "Laba/Rugi", "Saran Harga Jual")
    tree = Treeview(costs_frame, columns=columns, height=20, padding=3)
    tree.pack(padx=5, pady=5)
    tree.column("#0", anchor="center", width=50)
    tree.heading("#0", text="ID")

    try:
        # Ambil data dari tabel datalele
        mycursor.execute("SELECT * FROM datalele")
        myresult = mycursor.fetchall()

        # Define existing columns
        for col in columns:
            tree.column(col, anchor="center", width=150)
            tree.heading(col, text=col)

        # Insert data into treeview
        for i, line in enumerate(myresult):
            harga_jual_per_kg = line[3]
            biaya_bibit = line[4]
            biaya_pakan = line[5]
            biaya_obat = line[6]
            biaya_perawatan = line[7]

            pendapatan = harga_jual_per_kg * 0.8 * biaya_bibit
            pengeluaran = biaya_bibit + biaya_pakan + biaya_obat + biaya_perawatan
            laba_rugi = pendapatan - pengeluaran

            if laba_rugi < 0:
                saran_harga_jual = pengeluaran
            else:
                saran_harga_jual = "-"

            tree.insert('', END, iid=i, text=line[0], values=(harga_jual_per_kg, biaya_bibit, biaya_pakan, biaya_obat, biaya_perawatan, pendapatan, pengeluaran, laba_rugi, saran_harga_jual))
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")


# JUDUL DAN BUTTON
judul=ctk.CTkLabel(head, text = 'MyLele', text_color="white",font=("comic sans ms",15,"bold"))
judul.place(x= 50, y= 18)
#HOME
home_button=ctk.CTkButton(head, fg_color="blue", hover_color="dark blue", text = 'HOME', text_color="white",font=("comic sans ms",15, "bold"), width=0, command=home)
home_button.place(x= 350, y= 15)
# TAMBAH
home_button=ctk.CTkButton(head, fg_color="blue", hover_color="dark blue", text = 'ADD', text_color="white",font=("comic sans ms",15, "bold"), width=0, command=tambah)
home_button.place(x= 500, y= 15)
# DATA
home_button=ctk.CTkButton(head, fg_color="blue", hover_color="dark blue", text = 'DATA', text_color="white",font=("comic sans ms",15, "bold"), width=0, command=data_lele)
home_button.place(x= 650, y= 15)
# BIAYA
home_button=ctk.CTkButton(head, fg_color="blue", hover_color="dark blue", text = 'COSTS', text_color="white",font=("comic sans ms",15, "bold"), width=0, command=costs)
home_button.place(x= 800, y= 15)

# HOME DESIGN
frame2=ctk.CTkFrame(master=frame_utama, width=1250, height=680, corner_radius=15)
frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
label2= ctk.CTkLabel(master=frame2, text='')
label2.place(x=0, y= 0)

home()
window.mainloop()
