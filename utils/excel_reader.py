import openpyxl

def get_contacts_from_excel(file_path):
    workbook = openpyxl.load_workbook(r"C:\Users\rajam\PycharmProjects\PythonProject\AndroidDialerApp\Excel\testdata.xlsx"
)
    sheet = workbook.active
    contacts = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        contacts.append(row)

    return contacts
