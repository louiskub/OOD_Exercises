from time import time
from sys import getsizeof
import tracemalloc

class OrderedSet:
    def __init__(self):
        self.data = {}

    def add(self, item):
        self.data[item] = None
    
    def remove(self, item):
        try:
            del self.data[item]
        except:
            return -1

    def containes(self, item):
        return item in self.data
    
    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def memory_usage(self):
        return getsizeof(self.data)
    
class Guest:
    def __init__(self):
        self.channal = []
        self.amount = 0

class Controller:
    def __init__(self):
        self.hotel = 0
                    #people  #bus    #boat     #fleet     
        self.lst = [Guest(), Guest(), Guest(), Guest()] # type 0-3
        self.man = OrderedSet()
    
    def check_hotel(self):
        return ((self.hotel-1) // 4)
    
    def find_max(self):
        return max(guest.amount for guest in self.lst)

    def __add_manual(self, room_num):
        if self.man.containes(room_num):
            return "Room Exist"
        self.man.add(room_num)
        return "Add Manual Success"
        
    def add_manual(self, room_num):
        # สามารถเพิ่มเฉพาะห้องที่ไม่มีอยู่ ก็คือ ถ้าเป็นห้องว่างก็เพิ่มไม่ได้
        inhotel = self.check_hotel() + 1
        if (inhotel+self.find_max())*4  <= room_num:
            return self.__add_manual(room_num)
        return "Room Exist"
        
    def del_manual(self, room_num):
        if self.man.containes(room_num):
            self.man.remove(room_num)
            return "Delete Manual Success"
        return "Not found in manual list"

    def search_room(self, room_num):
        if room_num < 0:
            return "Invalid Room Number"
    
        # hotel part
        if room_num < self.hotel:
            return f"Room Number {room_num}: Hotel, Reserved"
        inhotel = self.check_hotel()
        if (inhotel+1)*4 > room_num:
            return f"Room Number {room_num}: Hotel, Free"
            # return "Hotel", "Free", room_num

        # manual part
        if self.man.containes(room_num):
            return f"Room Number {room_num}: Manual, Reserved"
        
        # lst
        typ = room_num % 4
        room_tranfrom = room_num // 4
        word = ["People", "Bus", "Boat", "Fleet"]
        if room_tranfrom <= inhotel + self.lst[typ].amount:
            return f"Room Number {room_num}: {word[typ]}, Reserved"
        if room_tranfrom <= inhotel + self.find_max():
            return f"Room Number {room_num}: {word[typ]}, Free"
        return "Room doesn't exist."

    def sort_reserved(self):
        # inhotel_count = ""
        for i in range(self.hotel):
            print(f"{i} ",end="")
        
        inhotel = self.check_hotel()
        for i in range(self.find_max()):
            start_room = (i+inhotel+1)*4
            if i < self.lst[0].amount:
                print(f"{start_room} ", end="")
            if i < self.lst[1].amount:
                print(f"{start_room+1} ", end="")
            if i < self.lst[2].amount:
                print(f"{start_room+2} ", end="")
            if i < self.lst[3].amount:
                print(f"{start_room+3} ", end="")

        for room in self.man:
            print(f"{room} ",end="")
        print()
        
    #Checkin Part
    def hotel_check_in(self, num):
        self.hotel = num

    def fleet_check_in(self, people, bus, boat, fleet):
        total = fleet * boat * bus * people
        self.lst[3].amount = total
        self.lst[3].channal = [people, bus, boat, fleet]

    def boat_check_in(self, people, bus, boat):
        total = boat * bus * people
        self.lst[2].amount = total
        self.lst[2].channal = [people, bus, boat]
    
    def bus_check_in(self, people, bus):
        total = bus * people
        self.lst[1].amount = total
        self.lst[1].channal = [people, bus]
    
    def people_check_in(self, people):
        total = people
        self.lst[0].amount = total
        self.lst[0].channal = [people]

    # Service Part
    def print_guest_count(self):
        print(f"Hotel: {self.hotel}")
        print(f"People: {self.lst[0].amount}")
        print(f"Bus: {self.lst[1].amount}")
        print(f"Boat: {self.lst[2].amount}")
        print(f"Fleet: {self.lst[3].amount}")
        print(f"Manual: {len(self.man)}")

    def print_free_room_count(self):
        inhotel = self.check_hotel()
        inhotel_count = (inhotel+1)*4 - self.hotel
                
        mx = self.find_max()
        lst_count = [0,0,0,0]
        for i in range(len(self.lst)):
            lst_count[i] = mx - self.lst[i].amount
        print(f"Hotel: {inhotel_count}")
        print(f"Guests: {sum(lst_count)}")

    def write_file_reserved(self, file_name):
        with open(f"{file_name}.txt", 'w') as f:
            for room in range(self.hotel):
                f.write(f"Room number {room}: Hotel\n")
            
            inhotel = self.check_hotel()
            people = 0
            bus, bus_channal = [0, 0], self.lst[1].channal
            boat, boat_channal = [0, 0, 0], self.lst[2].channal
            fleet, fleet_channal = [0, 0, 0, 0], self.lst[3].channal
            for i in range(self.find_max()):
                start_room = (i+inhotel+1)*4
                #people
                if i < self.lst[0].amount:
                    f.write(f"Room number {start_room}: People\n")
                #bus
                if i < self.lst[1].amount:
                    f.write(f"Room number {start_room + 1}: Bus : no_{bus[0]}_{bus[1]}\n")
                    bus[0] += 1
                    if bus[0] == bus_channal[0]:
                        bus[0] = 0
                        bus[1] += 1

                #boat
                if i < self.lst[2].amount:
                    f.write(f"Room number {start_room + 2}: Boat : no_{boat[0]}_{boat[1]}_{boat[2]}\n")
                    boat[0] += 1
                    if boat[0] == boat_channal[0]:
                        boat[0] = 0
                        boat[1] += 1
                        if boat[1] == boat_channal[1]:
                            boat[1] = 1
                            boat[2] += 1
                #fleet
                if i < self.lst[3].amount:
                    f.write(f"Room number {start_room + 3}: Fleet : no_{fleet[0]}_{fleet[1]}_{fleet[2]}_{fleet[3]}\n")
                    fleet[0] += 1
                    if fleet[0] == fleet_channal[0]:
                        fleet[0] = 0
                        fleet[1] += 1
                        if fleet[1] == fleet_channal[1]:
                            fleet[1] = 0
                            fleet[2] += 1
                            if fleet[2] == fleet_channal[2]:
                                fleet[2] = 0
                                fleet[3] += 1

            for room in self.man:
                f.write(f"Room number {room}: Manual\n")
    
    def memory_usage(self):
        man = self.man.memory_usage()
        lst = sum(getsizeof(e) for e in self.lst)
        return man+lst+getsizeof(self)


def print_menu():
    print("\n=== Hilbert's Hotel Management ===")
    print("1. Display guest counts")
    print("2. Add room manually")
    print("3. Delete room manually")
    print("4. Show sorted room list")
    print("5. Search for a room")
    print("6. Display free room counts")
    print("7. Write reserved rooms to file")
    print("8. Show memory usage")
    print("9. Display commands again")
    print("0. Reset system")
    print("Type 'exit' to quit the program")
    print("===================================\n")

def normal_check_in(con: Controller):
    print("Initial ")
    # In hotel
    while True:
        num = input("Enter Hotel Room: ")
        try:
            time_start = time()
            con.hotel_check_in(int(num))
            break
        except:
            print("Invalid Format!!!")
    time_end = time()
    print(f"time usage: {time_end-time_start}")
    print()

    # People
    print("People check_in. (people)")
    while True:
        inp = input("Enter People check in: ")
        try:
            inp = int(inp)
            time_start = time()
            con.people_check_in(inp)
            break
        except:
            print("Invalid Format!!!")
    time_end = time()
    print(f"time usage: {time_end-time_start}")
    print()

    # Bus
    print("Bus check_in. (bus, people)")
    while True:
        inp = input("Enter Bus check in: ")
        try:
            inp = list(map(int, inp.split(',')))
            time_start = time()
            con.bus_check_in(inp[1], inp[0])
            break
        except:
            print("Invalid Format!!!")
    time_end = time()
    print(f"time usage: {time_end-time_start}")
    print()

    #Boat
    print("Boat check_in. (boat, bus, people)")
    while True:
        inp = input("Enter Boat check in: ")
        try:
            inp = list(map(int, inp.split(',')))
            time_start = time()
            con.boat_check_in(inp[2], inp[1], inp[0])
            break
        except:
            print("Invalid Format!!!")
    time_end = time()
    print(f"time usage: {time_end-time_start}")
    print()

    #Fleet
    print("Fleet check_in. (fleet, boat, bus, people)")
    while True:
        inp = input("Enter Fleet check in: ")
        try:
            inp = list(map(int, inp.split(',')))
            time_start = time()
            con.fleet_check_in(inp[3], inp[2], inp[1], inp[0])
            break
        except:
            print("Invalid Format!!!")
    time_end = time()
    print(f"time usage: {time_end-time_start}")
    print()

def select_service(con: Controller):
    print_menu()
    while True:
        try:
            inp = input("Select Service: ")
            if inp =="1":
                print("All guests from every channals")
                time_start = time()
                con.print_guest_count()

            elif inp == "2":
                inp = int(input("Add Room Manual: "))
                time_start = time()
                result = con.add_manual(inp)
                print(result)

            elif inp == "3":
                inp = int(input("Delete Room Manual: "))
                time_start = time()
                result = con.del_manual(inp)
                print(result)

            elif inp == "4":
                time_start = time()
                print(con.sort_reserved())  # it's already sorted

            elif inp == "5":
                inp = int(input("Search Room: "))
                time_start = time()
                print(con.search_room(inp))

            elif inp == "6":
                print("Show Free Room: ")
                time_start = time()
                con.print_free_room_count()
                
            elif inp == "7":
                inp = input("Write to file name: ")
                time_start = time()
                con.write_file_reserved(inp)
                print("Write Success")

            elif inp == "8":
                time_start = time()
                print(f"Memory usage: {con.memory_usage()} bytes")

            elif inp == "9":
                print_menu()
                continue
            elif inp == "0":
                break
            elif inp == "exit":
                print("End of Program Execution")
                return -1
            else:
                continue

            time_end = time()
            print(f"time usage: {time_end-time_start}")
            print()
        except:
            print("Error\n")

def main3():
    while True:
        con = Controller()
        print("--- Thep Ang Yai Hotel Service ---")
        print("-"*40)
        
        tracemalloc.start()
        normal_check_in(con)
        if select_service(con) == -1:
            tracemalloc.stop()
            return

if __name__ == "__main__":
    main3()