import requests
import tkinter as tk
from tkinter import ttk

# Function to get IP information using ipapi.co
def get_ip_info():
    try:
        # Send a request to ipapi.co to get the IP information
        response = requests.get("https://ipapi.co/json/")
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Format the information to display in the GUI
            return [
                data.get('ip', 'N/A'),          
                data.get('ip6', 'N/A'),         
                data.get('city', 'N/A'),        
                data.get('region', 'N/A'),      
                data.get('country_name', 'N/A'),
                data.get('org', 'N/A'),         
                data.get('asn', 'N/A'),         
                data.get('latitude', 'N/A'),    
                data.get('longitude', 'N/A')    
            ]
        else:
            # Return a placeholder if IP information could not be retrieved
            return ["Failed to retrieve information."] * 9
    
    # Catch any exceptions related to the HTTP request
    except requests.RequestException as e:
        return [f"An error occurred: {e}"] * 9

# Function to display IP information in the GUI
def show_ip_info():
    ip_info = get_ip_info()
    if not table_shown:
        create_table(ip_info)
    else:
        for i, info in enumerate(ip_info):
            data_labels[i].config(text=info)

# Function to create a table for displaying IP information
def create_table(ip_info):
    global data_labels, table_shown
    table_shown = True 

    # Create a container for the table
    table_frame = tk.Frame(root, bg='#779ECB')
    table_frame.pack(pady=10)

    # Create table with two columns: Headers and Data
    headers = ["Public IPv4 Address", "Public IPv6 Address", "City", "Region", "Country", "ISP", "ASN", "Latitude", "Longitude"]

    # Create a row for each header and corresponding data
    for i, header in enumerate(headers):
        row_frame = tk.Frame(table_frame, bg='#779ECB')
        row_frame.pack(fill="x", padx=10, pady=5)

        header_label = tk.Label(row_frame, text=header, font=("Helvetica", 10, "bold"), width=20, anchor="w", bg='#779ECB', fg="white")
        header_label.pack(side="left")

        data_label = tk.Label(row_frame, text=ip_info[i], font=("Helvetica", 10), anchor="w", bg='#779ECB', fg="white")
        data_label.pack(side="left")

        data_labels.append(data_label)

# Set up the main window
root = tk.Tk()
root.title("NetTrace")
root.geometry("600x500")
root.configure(bg='#779ECB')

# Frame for the title and icon
title_frame = tk.Frame(root, bg='#779ECB')
title_frame.pack(pady=20)

# Title
title_label = tk.Label(title_frame, text="NetTrace", font=("Helvetica", 20, "bold"), bg='#779ECB', fg="white")
title_label.pack(side="left")

globe_label = tk.Label(title_frame, text="🌐", font=("Helvetica", 20), bg='#779ECB', fg="white")  # Unicode for globe symbol
globe_label.pack(side="left", padx=10)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, relief="flat")

btn_get_ip = ttk.Button(root, text="Trace", command=show_ip_info, style="TButton")
btn_get_ip.pack(pady=20)

# Track whether the table has been created
table_shown = False
data_labels = []  # List to store the labels for the data column

# Add a frame for padding/margin at the bottom
bottom_frame = tk.Frame(root, height=20, bg='#779ECB') 
bottom_frame.pack(side="bottom")

# Start the application main loop
root.mainloop()
