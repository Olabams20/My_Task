# Task5: Contact Quick Lookup
names = ('Tolu', 'Mary', 'Esther')
phone_numbers = ('08023456792', '08123456789', '09023871940')
contact_dict = dict(zip(names, phone_numbers))
name_to_lookup = input("Enter a name to lookup: ")
print(contact_dict.get(name_to_lookup, "Name not found in contacts."))
