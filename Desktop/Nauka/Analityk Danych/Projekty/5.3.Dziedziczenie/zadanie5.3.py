from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, name, surname, private_phone, email_address):
        self.name = name
        self.surname = surname
        self.private_phone = private_phone
        self.email_address = email_address

    def __str__(self):
        return f"{self.name} {self.surname} - {self.email_address}"

    def contact(self):
        print(f"Wybieram numer {self.private_phone} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return len(f"{self.name} {self.surname}")

class BusinessContact(BaseContact):
    def __init__(self, name, surname, private_phone, email_address, company_name, position, business_phone):
        super().__init__(name, surname, private_phone, email_address)
        self.company_name = company_name
        self.position = position
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.surname}")

def create_contacts(kind='base', number=5):
    contacts = []
    for _ in range(number):
        name = fake.first_name()
        surname = fake.last_name()
        email = fake.email()
        private_phone = fake.phone_number()

        if kind == 'business':
            company = fake.company()
            position = fake.job()
            business_phone = fake.phone_number()
            contact = BusinessContact(name, surname, private_phone, email, company, position, business_phone)
        else:
            contact = BaseContact(name, surname, private_phone, email)
        
        contacts.append(contact)

    return contacts

base_contacts = create_contacts(kind='base', number=3)
business_contacts = create_contacts(kind='business', number=2)

print("Wizytówki prywatne:")
for c in base_contacts:
    print(c)
    c.contact()
    print("Długość etykiety:", c.label_length)
    print()

print("Wizytówki firmowe:")
for c in business_contacts:
    print(c)
    c.contact()
    print("Długość etykiety:", c.label_length)
    print()