'''
This is the main file of the IPFS HTTP API Library.
It provides a graphical user interface for users to interact with the library.
'''
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from ipfs_api import IPFSAPI
class IPFSAPILibraryGUI:
    def __init__(self):
        self.ipfs_api = IPFSAPI()
        self.root = tk.Tk()
        self.root.title("IPFS HTTP API Library")
        # Create GUI elements
        self.add_file_button = tk.Button(self.root, text="Add File", command=self.add_file)
        self.add_file_button.pack()
        self.add_folder_button = tk.Button(self.root, text="Add Folder", command=self.add_folder)
        self.add_folder_button.pack()
        self.pin_cid_button = tk.Button(self.root, text="Pin CID", command=self.pin_cid)
        self.pin_cid_button.pack()
        self.pin_cid_recursive_button = tk.Button(self.root, text="Pin CID Recursively", command=self.pin_cid_recursive)
        self.pin_cid_recursive_button.pack()
        self.remove_cid_button = tk.Button(self.root, text="Remove CID", command=self.remove_cid)
        self.remove_cid_button.pack()
        self.get_file_button = tk.Button(self.root, text="Get File", command=self.get_file)
        self.get_file_button.pack()
        self.get_folder_button = tk.Button(self.root, text="Get Folder", command=self.get_folder)
        self.get_folder_button.pack()
        self.download_file_button = tk.Button(self.root, text="Download File", command=self.download_file)
        self.download_file_button.pack()
        self.download_folder_button = tk.Button(self.root, text="Download Folder", command=self.download_folder)
        self.download_folder_button.pack()
        self.read_file_button = tk.Button(self.root, text="Read File", command=self.read_file)
        self.read_file_button.pack()
        # Run the GUI
        self.root.mainloop()
    def add_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.ipfs_api.add_file(file_path)
            messagebox.showinfo("Success", "File added to IPFS network.")
    def add_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.ipfs_api.add_folder(folder_path)
            messagebox.showinfo("Success", "Folder added to IPFS network.")
    def pin_cid(self):
        cid = simpledialog.askstring("Pin CID", "Enter the CID to pin:")
        if cid:
            self.ipfs_api.pin_cid(cid)
            messagebox.showinfo("Success", "CID pinned to local IPFS network.")
    def pin_cid_recursive(self):
        cid = simpledialog.askstring("Pin CID Recursively", "Enter the CID to pin recursively:")
        if cid:
            self.ipfs_api.pin_cid_recursive(cid)
            messagebox.showinfo("Success", "CID pinned recursively to local IPFS network.")
    def remove_cid(self):
        cid = simpledialog.askstring("Remove CID", "Enter the CID to remove:")
        if cid:
            self.ipfs_api.remove_cid(cid)
            messagebox.showinfo("Success", "CID removed.")
    def get_file(self):
        cid = simpledialog.askstring("Get File", "Enter the CID of the file:")
        if cid:
            file_path = self.ipfs_api.get_file(cid)
            if file_path:
                messagebox.showinfo("Success", f"File retrieved from IPFS network. File path: {file_path}")
            else:
                messagebox.showinfo("Error", "Failed to get file from IPFS network.")
    def get_folder(self):
        cid = simpledialog.askstring("Get Folder", "Enter the CID of the folder:")
        if cid:
            folder_path = self.ipfs_api.get_folder(cid)
            if folder_path:
                messagebox.showinfo("Success", f"Folder retrieved from IPFS network. Folder path: {folder_path}")
            else:
                messagebox.showinfo("Error", "Failed to get folder from IPFS network.")
    def download_file(self):
        cid = simpledialog.askstring("Download File", "Enter the CID of the file:")
        if cid:
            save_path = filedialog.asksaveasfilename()
            if save_path:
                self.ipfs_api.download_file(cid, save_path)
                messagebox.showinfo("Success", "File downloaded from IPFS network.")
    def download_folder(self):
        cid = simpledialog.askstring("Download Folder", "Enter the CID of the folder:")
        if cid:
            save_path = filedialog.askdirectory()
            if save_path:
                self.ipfs_api.download_folder(cid, save_path)
                messagebox.showinfo("Success", "Folder downloaded from IPFS network.")
    def read_file(self):
        cid = simpledialog.askstring("Read File", "Enter the CID of the file:")
        if cid:
            content = self.ipfs_api.read_file(cid)
            if content:
                messagebox.showinfo("File Content", content)
            else:
                messagebox.showinfo("Error", "Failed to read file from IPFS network.")
if __name__ == "__main__":
    IPFSAPILibraryGUI()