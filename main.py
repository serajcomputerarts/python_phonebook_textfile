class Test:
    file_name="seraj.txt"
    def add_student(self,name,phone):
        myfile=open(self.file_name,"a")
        myfile.write(f"{name}:{phone}\n")
        myfile.close()
    def show_all_data(self):
        myfile=open(self.file_name,"r")
        data=myfile.read()
        datalist=data.split(" ")
        for row in datalist:
            print(row)
    def find_num_by_name(self,name):
        phone="Not Found"
        myfile=open(self.file_name,"r")
        rows=myfile.readlines()
        myfile.close()
        for row in rows:
            data=row.split(":")
            if data[0]==name:
                phone=data[1]
        return phone
    def delete_data_byname(self,name):
        myfile=open(self.file_name,"r")
        rows=myfile.readlines()
        myfile.close()
        myfile=open(self.file_name,"w")
        for row in rows:
            data=row.split(":")
            if data[0]==name:
                continue
            myfile.write(row)
        myfile.close()
    def update_student_phone_by_name(self,name,phone):
        myfile=open(self.file_name,"r")
        rows=myfile.readlines()
        myfile.close()
        myfile=open(self.file_name,"w")
        for row in rows:
            data=row.split(":")
            if data[0]==name:
                new_data_row=data[0]+":"+phone+"\n"
                myfile.write(new_data_row)
                continue
            myfile.write(row)
        myfile.close()
        
ob=Test()
# use add_student method to add student to file
# Example:
# ob.add_student("Reza","0911")
# show all data in file
# ob.show_all_data()
# you can find phone by name with this method
# print(ob.find_num_by_name("Reza"))
# delete data using method below
# ob.delete_data_byname("Hadi")
# update student phone by using this method
# ob.update_student_phone_by_name("Hadi","011111")
# Thanks for using this practice
