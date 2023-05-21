from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title("Learn to code")
root.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\wifi.ico')
root.geometry("400x600")

# Odkaz: https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB&index=2

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')


# Create cursor
c = conn.cursor()

# Create table

# c.execute("""CREATE TABLE addresses (
#        first_name text,
#        last_name text,
#        address text,
#        city text,
#        state text,
#        zipcode integer
#        )
# """)

# Create edit fnct to update a record
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()


    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })
    


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    editor.destroy()




def edit():
    global editor
    editor = Tk()
    editor.title("Edit a Record")
    editor.iconbitmap(r'C:\Users\tomry\GraphicUserInterface\wifi.ico')
    editor.geometry("400x250")

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    #Create Global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    



    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    # Create Text Box Labels
    f_name_lbl = Label(editor, text="First Name")
    f_name_lbl.grid(row=0, column=0, pady=(10, 0))
    l_name_lbl = Label(editor, text="Last Name")
    l_name_lbl.grid(row=1, column=0)
    address_lbl = Label(editor, text="Address")
    address_lbl.grid(row=2, column=0)
    city_lbl = Label(editor, text="City")
    city_lbl.grid(row=3, column=0)
    state_lbl = Label(editor, text="State")
    state_lbl.grid(row=4, column=0)
    zip_lbl = Label(editor, text="ZipCode")
    zip_lbl.grid(row=5, column=0)

    # Loop thru results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create a save btn to save edited record
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=150)


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


# Deleting records
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()



# Create funcion submit database

def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    #Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create Querry Fnc
def querry():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    # Loop Thru Result
    print_records = ''
    for record in records:   # [0, 1, 2 whateever..]:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t\t" + str(record[6]) + "\n"
        # print_records += str(record) + "\n"

    querry_lbl = Label(root, text=print_records)
    querry_lbl.grid(row=12, column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)


# Create Text Box Labels
f_name_lbl = Label(root, text="First Name")
f_name_lbl.grid(row=0, column=0, pady=(10, 0))
l_name_lbl = Label(root, text="Last Name")
l_name_lbl.grid(row=1, column=0)
address_lbl = Label(root, text="Address")
address_lbl.grid(row=2, column=0)
city_lbl = Label(root, text="City")
city_lbl.grid(row=3, column=0)
state_lbl = Label(root, text="State")
state_lbl.grid(row=4, column=0)
zip_lbl = Label(root, text="ZipCode")
zip_lbl.grid(row=5, column=0)

delete_box_lbl = Label(root, text="Select ID")
delete_box_lbl.grid(row=9, column=0)

# Create Submit button
sub_btn = Button(root, text="Add Record to Database", command=submit)
sub_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=111)

# Create a Query Button
querry_btn = Button(root, text="Show Records", command=querry)
querry_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a DELETE Btn
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create an Update btn
update_btn = Button(root, text="Edit Record", command=edit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)




# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()