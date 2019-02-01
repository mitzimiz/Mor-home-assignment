class CsvUtils():

    def create_file(self,file_name):
        F = open(file_name,"w")

    def write_to_file(self,file,data_to_write):
        with open(file) as file:
            file.write(data_to_write)
