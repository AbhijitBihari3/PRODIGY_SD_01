import json
class Contact:
 def __init__(self, name, phone, email):
  self.name=name
  self.phone=phone
  self.email=email

 def to_dict(self):
  return {"name" : self.name, "phone":self.phone, "email":self.email}

def add_contact(all_contacts):
 name=input("enter name: ")
 phone=input("enter phone: ")
 email=input("enter email: ")
 new_contact=Contact(name,phone,email)
 all_contacts.append(new_contact)
 print("New Contact Added")

def view_contacts(all_contacts):
 if not all_contacts:
  print("No Contacts Found")
  return
 for i,contact in enumerate(all_contacts):
  print(f"{i + 1}.  NAME:{contact.name}, PHONE:{contact.phone}, EMAIL:{contact.email} ")
  
def edit_contacts(all_contacts):
 view_contacts(all_contacts)
 if not all_contacts:
  return
 to_edit_index=int(input("enter the number of conatct to edit: "))-1
 if 0<= to_edit_index <len(all_contacts):
  contact=all_contacts[to_edit_index]
  contact.name= input(f"enter new name (current: {contact.name})")
  contact.phone=input(f"enter new phone (current: {contact.phone})")
  contact.email=input(f"enter new email (current: {contact.email})")
  print("contact updated")
 else:
  print("invalid input")

def delete_contact(all_contacts):
 view_contacts(all_contacts)
 if not all_contacts:
  return
 to_delete_index=int(input("enter the number of the contact to delete: "))-1
 if 0<=  to_delete_index < len(all_contacts):
  all_contacts.pop(to_delete_index)
  print("contact deleted")
 else:
  print("invalid input")

def contact_load(filenm):
 try:
  with open(filenm, 'r') as file:
   contact_data=json.load(file)
   return [Contact(**data) for data in contact_data]
 except FileNotFoundError:
  return[]
 except json.JSONDecodeError:
  return[]
 
def save_contacts(filenm,all_contacts):
 with open(filenm , 'w') as file:
  json.dump([vars(contact) for contact in all_contacts], file, indent=4)

def main():
 filenm="all_contacts.json"
 all_contacts=contact_load(filenm)

 while True:
  print("\n The Conatct Management System ")
  print("1. Add a contact")
  print("2. View all contacts")
  print("3. Edit a contact")
  print("4. Delete a contact")
  print("5. Exit")
  choice=input("enter your choice: ")
  if choice=='1':
   add_contact(all_contacts)
  elif choice=='2':
   view_contacts(all_contacts)
  elif choice=='3':
   edit_contacts(all_contacts)
  elif choice=='4':
   delete_contact(all_contacts)
  elif choice=='5':
   save_contacts(filenm, all_contacts)
   print("contact saved")
   break
  else:
   print("invalid input")

if __name__=="__main__":
 main()



