from datetime import datetime

#start_time =datetime.now()
# input("Wait....")
# end_time = datetime.now()

# time_played = end_time - start_time
# print(time_played)

pool_tables = []
class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None
        self.time_played = None
        
    def check_in(self):
        self.is_occupied = True
        self.end_time = None
        self.start_time= datetime.now()
    
    def check_out(self):
        self.end_time = datetime.now()
        self.time_played = self.end_time - self.start_time
        self.is_occupied = False
        with open("test.txt","a") as file_object: 
            file_object.write(f"Pool Table Number: {self.table_number}\n")
            file_object.write(f"Time in: {self.start_time} \n")
            file_object.write(f"Time out: {self.end_time} \n")
            file_object.write(f"time Played: {self.time_played} \n")
        self.start_time = None
        self.end_time = None
        print("checkout complete")
        
for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

while True: 
    print("""
    POOL TABLE MANAGEMENT
    ***********************
    1. Check into Pool Table
    2. Check checkout of Pool Table
    3. View All Tables
    4. q to Quit
    

    ************************
""")
    choice = input("Enter Choice: ")
    if choice ==  "1":
        table_number = int(input("which table number: "))
        pt =  pool_tables[table_number - 1]
        pt.check_in()

    if choice == "2":
        table_number = int(input("Which table you want to checkout: "))
        pt = pool_tables[table_number - 1]
        pt.check_out()
    
    if choice == "3":
        for index in range (0, len(pool_tables)):
            pool_table = pool_tables[index]
            print(pool_table.start_time)

    if choice =="q":
        break
        

        
     


    