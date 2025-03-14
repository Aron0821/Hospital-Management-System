from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Variables
        self.Nameoftablets = StringVar()
        self.Reference_No = StringVar()
        self.Dose = StringVar()
        self.Numbersoftablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.furtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.Patinetid = StringVar()
        self.nhsmumber = StringVar()
        self.patientname = StringVar()
        self.DOB = StringVar()
        self.patientaddress = StringVar()

        # Title
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("poppins", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # Dataframe
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1540, height=400)

        DataFrameLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("poppins", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("poppins", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=500, height=350)

        # Buttons Frame
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1540, height=70)

        # Details Frame
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1540, height=190)

        # ================================ DataFrameLeft =====================================
        lblNameTablet = Label(DataFrameLeft, text="Name of Tablets:", font=("poppins", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataFrameLeft, textvariable=self.Nameoftablets, state="readonly", font=("poppins", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.Reference_No, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.Numbersoftablets, width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("poppins", 13, "bold"), textvariable=self.sideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherLabel = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherLabel.grid(row=0, column=2, sticky=W)
        txtFurtherLabel = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.furtherInformation, width=35)
        txtFurtherLabel.grid(row=0, column=3)

        lblBloodPressure = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.Patinetid, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.nhsmumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.patientname, width=35)
        txtPatientname.grid(row=6, column=3)

        lblDateOfBirth = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.DOB, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataFrameLeft, font=("poppins", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("poppins", 12, "bold"), textvariable=self.patientaddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ============================= DataFrameRight ==================================
        self.txtPrescription = Text(DataFrameRight, font=("poppins", 12, "bold"), width=50, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # =============================== Buttons ================================
        btnPrescription = Button(Buttonframe,command=self.iPrescription, text="Prescription", bg="green", fg="white", font=("poppins", 12, "bold"), width=10, height=1, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0, sticky="ew")

        btnPrescriptionData = Button(Buttonframe, command=self.iPrescriptionData, text="Prescription Data", bg="green", fg="white", font=("poppins", 12, "bold"), width=10, height=1, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1, sticky="ew")

        btnUpdate = Button(Buttonframe, command=self.update_data , text="Update", bg="green", fg="white", font=("poppins", 12, "bold"), width=10, height=1, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2, sticky="ew")

        btnDelete = Button(Buttonframe, command=self.idelete , text="Delete", bg="green", fg="white", font=("poppins", 12, "bold"), width=10, height=1, padx=2, pady=6)
        btnDelete.grid(row=0, column=3, sticky="ew")

        btnClear = Button(Buttonframe, command=self.clear_fields, text="Clear", bg="green", fg="white", font=("poppins", 12, "bold"), width=10, height=1, padx=2, pady=6)
        btnClear.grid(row=0, column=4, sticky="ew")

        btnExit = Button(Buttonframe, command=self.iexit, text="Exit", bg="green", fg="white", font=("poppins", 12, "bold"), width=10, height=1, padx=2, pady=6)
        btnExit.grid(row=0, column=5, sticky="ew")

        # Configure columns to expand equally
        for i in range(6):  # There are 6 columns (0 to 5)
            Buttonframe.columnconfigure(i, weight=1)

        # ========================= Table ============================
        # ========================= Scrollbar =========================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameoftablets", "Reference_No", "dose", "Numbersoftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "nhsmumber", "patientname", "DOB", "patientaddress"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name Of Tablets")
        self.hospital_table.heading("Reference_No", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("Numbersoftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsmumber", text="NHS Number")
        self.hospital_table.heading("patientname", text="Patient Name")
        self.hospital_table.heading("DOB", text="DOB")
        self.hospital_table.heading("patientaddress", text="Patient Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("Reference_No", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("Numbersoftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsmumber", width=100)
        self.hospital_table.column("patientname", width=100)
        self.hospital_table.column("DOB", width=100)
        self.hospital_table.column("patientaddress", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.Reference_No.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Arm@1116", database="Mydata")
                my_cursor = conn.cursor()

                sql_query = """INSERT INTO hospital 
                    (Nameoftablets, Reference_No, dose, Numbersoftablets, lot, issuedate, expdate, dailydose, storage, nhsmumber, patientname, DOB, patientaddress) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                my_cursor.execute(sql_query, (
                    self.Nameoftablets.get(),
                    self.Reference_No.get(),
                    self.Dose.get(),
                    self.Numbersoftablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsmumber.get(),
                    self.patientname.get(),
                    self.DOB.get(),
                    self.patientaddress.get(),
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data inserted successfully")
                self.clear_fields()

            except Exception as e:
                messagebox.showerror("Error", f"Database error: {str(e)}")

    def update_data(self):
        if self.Reference_No.get() == "":
            messagebox.showerror("Error", "Reference No. is required to update data")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Arm@1116", database="Mydata")
                my_cursor = conn.cursor()

                # Update query
                my_cursor.execute("""
                    UPDATE hospital 
                    SET Nameoftablets = %s, dose = %s, Numbersoftablets = %s, lot = %s, issuedate = %s, 
                        expdate = %s, dailydose = %s, storage = %s, nhsmumber = %s, 
                        patientname = %s, DOB = %s, patientaddress = %s 
                    WHERE Reference_No = %s
                """, (
                    self.Nameoftablets.get(),
                    self.Dose.get(),
                    self.Numbersoftablets.get(),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsmumber.get(),
                    self.patientname.get(),
                    self.DOB.get(),
                    self.patientaddress.get(),
                    self.Reference_No.get(),
                ))

                conn.commit()  # Commit the transaction
                conn.close()  # Close the connection

                # Refresh the data in the Treeview
                self.fetch_data()

                # Notify the user
                messagebox.showinfo("Success", "Data updated successfully")

                # Clear input fields (optional)
                self.clear_fields()

            except Exception as e:
                messagebox.showerror("Error", f"Database error: {str(e)}")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Arm@1116", database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        self.Nameoftablets.set(row[0])
        self.Reference_No.set(row[1])
        self.Dose.set(row[2])
        self.Numbersoftablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsmumber.set(row[9])
        self.patientname.set(row[10])
        self.DOB.set(row[11])
        self.patientaddress.set(row[12])

    def clear_fields(self):
        self.Nameoftablets.set("")
        self.Reference_No.set("")
        self.Dose.set("")
        self.Numbersoftablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsmumber.set("")
        self.patientname.set("")
        self.DOB.set("")
        self.patientaddress.set("")

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets: \t\t\t" +self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END, "Reference No: \t\t\t" +self.Reference_No.get()+"\n")
        self.txtPrescription.insert(END, "Dose: \t\t\t" +self.Dose.get()+"\n")
        self.txtPrescription.insert(END, "Number of Tablets: \t\t\t" +self.Numbersoftablets.get()+"\n")
        self.txtPrescription.insert(END, "Lot: \t\t\t" +self.Lot.get()+"\n")
        self.txtPrescription.insert(END, "Issue Date: \t\t\t" +self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END, "Exp Date: \t\t\t" +self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END, "Daily Dose: \t\t\t" +self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END, "Side Effects: \t\t\t" +self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END, "Further Information: \t\t\t" +self.furtherInformation.get()+"\n")
        self.txtPrescription.insert(END, "Storage Advice: \t\t\t" +self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END, "Medicatiom: \t\t\t" +self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END, "PatientID: \t\t\t" +self.Patinetid.get()+"\n")
        self.txtPrescription.insert(END, "NHS Number: \t\t\t" +self.nhsmumber.get()+"\n")
        self.txtPrescription.insert(END, "Patient Name: \t\t\t" +self.patientname.get()+"\n")
        self.txtPrescription.insert(END, "DOB: \t\t\t" +self.DOB.get()+"\n")
        self.txtPrescription.insert(END, "Patient Address: \t\t\t" +self.patientaddress.get()+"\n")


    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="Mydata")
        my_cursor = conn.cursor()
        query = "delete from hospital where Reference_No = %s"
        value = (self.Reference_No.get(),)
        my_cursor.execute(query,value)
    
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient's data has been deleted successfully")


    def iexit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Exit")
        if iExit > 0:
            root.destroy()
            return

root = Tk()
ob = Hospital(root)
root.mainloop()