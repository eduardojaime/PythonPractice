# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15

@author: Eduardo Jaime

Objective: 
    Demonstrate use of classes, and object serialization/deserialization using the pickle module
    This small application allows you to manage a list of contacts to save name-phone-email
    No delete functionality implemented yet
"""
# to serialize/deserialize data structures to binary file
import pickle

# empy list to save contacts
contacts=[]

contacts_filename = 'contacts.pickle'

str_contact = '{0} - Phone Nbr {1} and Email Address {2}'

msg_input_name = 'Enter full name, or enter * to leave empty/unchanged: '
msg_input_phone = 'Enter phone number, or enter * to leave empty/unchanged: '
msg_input_email = 'Enter email address, or enter * to leave empty/unchanged: '

# represents a contact that I can save info about
# a contact will have the following data attributes: name phone and email
# class with initializer
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

def add_contact():
    name = input(msg_input_name)
    if name == '*':
        name = ''
    phone = input(msg_input_phone)
    if phone == '*':
        phone = ''
    email = input(msg_input_email)
    if email == '*':
        email = ''
        
    contact = Contact(name, phone, email)    
    contacts.append(contact)
    print('Contact {0} was added successfully.'.format(name))

def update_contact():
    name = input('Enter name to update: ')
    results = find_contact(name)
    if len(results) == 0: 
        print('No contacts found with name {0}'.format(name))
    elif len(results) == 1:
        contact = results[0] 
        name = input(msg_input_name)
        if name != '*':
            contact.name = name
        phone = input(msg_input_phone)
        if phone != '*':
            contact.phone = phone
        email = input(msg_input_email)
        if email != '*':
            contact.email = email
    else:
        print('More than one contact found. Please verify name.')
        for r in results:
            print('{0} - Phone Nbr {1} and Email Address {2}'.format(r.name, r.phone, r.email))

def search_contact():
    name = input('Enter name to search: ')
    results = find_contact(name)
    if len(results) == 0: 
        print('No contacts found with name {0}'.format(name))
    else:
        for r in results:
            print(str_contact.format(r.name, r.phone, r.email))

def print_contacts():    
    print(str(len(contacts)) + ' contacts in the list.')
    for c in contacts:
        print(str_contact.format(c.name, c.phone, c.email))

def find_contact(name):
    results=[]
    name = name.strip().lower()
    for c in contacts:
        if name in c.name.strip().lower():
            results.append(c)
    return results    

def save_contacts():
    try:
        # wb is write binary
        with open(contacts_filename, 'wb') as output_file:
            pickle.dump(contacts, output_file)
            print('Contact list saved to disk!')
    except:
        print('An error occurred while saving to disk. Please try again.')

def load_contacts():
    # make this global in order to access the contacts list object created in the beginning of this file
    global contacts
    # rb is read binary
    with open(contacts_filename, 'rb') as input_file:
        contacts = pickle.load(input_file)
        print('Contact list loaded from disk!')
        
## MAIN PROGRAM
load_contacts()

run_again = True
while run_again:
    option = input('''Select an option from the list below:
            1. Add a new Contact
            2. Search a Contact by name
            3. Update a Contact by name
            7. Print Contact List
            8. Save and Exit
            ''')
    option = option.strip()
    if option == '1':
        add_contact()
    elif option == '2':
        search_contact()
    elif option == '3':
        update_contact()
    elif option == '7':
        print_contacts()
    elif option == '8':
        save_contacts()
        run_again = False
    else:
        print('Invalid option')
        
print('Thank you for using this program!')
