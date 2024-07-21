import tkinter as tk
from tkinter import filedialog, messagebox
import socket
import threading
import os

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=file_path)
        send_button.config(state=tk.NORMAL)

def send_file():
    file_path = file_label.cget("text")
    if not file_path:
        return

    server_ip = server_ip_entry.get()
    if not server_ip:
        messagebox.showerror("Erreur", "Veuillez entrer l'adresse IP du serveur.")
        return
    
    threading.Thread(target=send_file_thread, args=(file_path, server_ip)).start()

def send_file_thread(file_path, server_ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, 5001))
            s.sendall(os.path.basename(file_path).encode())
            response = s.recv(1024).decode()
            if response == "ACCEPT":
                with open(file_path, "rb") as f:
                    total_size = os.path.getsize(file_path)
                    sent_size = 0
                    while chunk := f.read(4096):
                        s.sendall(chunk)
                        sent_size += len(chunk)
                        progress = (sent_size / total_size) * 100 if total_size > 0 else 100
                        progress_label.config(text=f"Progression : {progress:.2f}%")
                messagebox.showinfo("Succès", "Fichier envoyé avec succès.")
            else:
                messagebox.showinfo("Refusé", "Le destinataire a refusé le fichier.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

root = tk.Tk()
root.title("Expéditeur de fichier")

tk.Label(root, text="Adresse IP du serveur :").pack()
server_ip_entry = tk.Entry(root)
server_ip_entry.pack()

file_label = tk.Label(root, text="Aucun fichier sélectionné")
file_label.pack()

tk.Button(root, text="Sélectionner un fichier", command=select_file).pack()
send_button = tk.Button(root, text="Envoyer le fichier", command=send_file, state=tk.DISABLED)
send_button.pack()

progress_label = tk.Label(root, text="")
progress_label.pack()

root.mainloop()
