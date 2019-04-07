#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()