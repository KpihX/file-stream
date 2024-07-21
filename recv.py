import tkinter as tk
from tkinter import filedialog, messagebox
import socket
import threading
import os

def start_server():
    threading.Thread(target=server_thread).start()

def server_thread():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 5001))
        s.listen(5)
        while True:
            client_socket, addr = s.accept()
            threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    try:
        file_name = client_socket.recv(1024).decode()
        if not file_name:
            return

        if messagebox.askyesno("Demande de fichier", f"Voulez-vous accepter le fichier '{file_name}' ?"):
            client_socket.sendall(b"ACCEPT")
            save_path = filedialog.asksaveasfilename(initialfile=file_name)
            if save_path:
                with open(save_path, "wb") as f:
                    total_size = 0
                    while chunk := client_socket.recv(4096):
                        f.write(chunk)
                        total_size += len(chunk)
                        progress = (total_size / os.path.getsize(save_path)) * 100 if os.path.getsize(save_path) > 0 else 100
                        progress_label.config(text=f"Progression : {progress:.2f}%")
                messagebox.showinfo("Succès", "Fichier reçu avec succès.")
        else:
            client_socket.sendall(b"REFUSE")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
    finally:
        client_socket.close()

root = tk.Tk()
root.title("Récepteur de fichier")

tk.Button(root, text="Démarrer le serveur", command=start_server).pack()
progress_label = tk.Label(root, text="")
progress_label.pack()

root.mainloop()
