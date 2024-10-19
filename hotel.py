from time import time
from sys import getsizeof


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return self.rebalance(root)

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return self.rebalance(root)

    def rebalance(self, root):
        self.update_height(root)
        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            if self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            if self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self.update_height(z)
        self.update_height(y)
        return y

    def get_min_value_node(self, node):
        while node and node.left:
            node = node.left
        return node

    def write_to_file(self, node, file):
        if node is not None:
            self.write_to_file(node.left, file)
            file.write(f"Room number {node.key}: Manual\n")
            self.write_to_file(node.right, file)

    def search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def print_avl_tree(self, node):
        if node is None:
            return []
        return (
            self.print_avl_tree(node.left)
            + [str(node.key)]
            + self.print_avl_tree(node.right)
        )


class Guest:
    def __init__(self):
        self.channal = []
        self.amount = 0


class Controller:
    def __init__(self):
        self.hotel = 0
        # people  #bus    #boat     #fleet
        self.lst = [Guest(), Guest(), Guest(), Guest()]  # type 0-3
        self.man = None
        self.avl_tree = AVLTree()

    def check_hotel(self):
        return (self.hotel - 1) // 4

    def find_max(self):
        return max(guest.amount for guest in self.lst)
        
    def __add_manual(self, room_num):
        if self.avl_tree.search(self.man, room_num):
            return "Room Exist"
        self.man = self.avl_tree.insert(self.man, room_num)
        return "Add Manual Success"

    def add_manual(self, room_num):
        inhotel = self.check_hotel() + 1
        if (inhotel + self.find_max()) * 4 <= room_num:
            return self.__add_manual(room_num)
        return "Room Exist"

    def del_manual(self, room_num):
        if self.man is None:
            return "Not found in manual list"
        if room_num < self.hotel:
            return "Cannot delete: This is a reserved room in the hotel."

        if self.avl_tree.search(self.man, room_num) is None:
            return "Room does not exist in manual list."

        self.man = self.avl_tree.delete(self.man, room_num)
        return "Delete Manual Success"

    def search_room(self, room_num):
        if room_num < 0:
            return "Invalid Room Number"

        if room_num < self.hotel:
            return f"Room Number {room_num}: Hotel, Reserved"

        inhotel = self.check_hotel()
        if (inhotel + 1) * 4 > room_num:
            return f"Room Number {room_num}: Hotel, Free"

        if self.avl_tree.search(self.man, room_num):
            return f"Room Number {room_num}: Manual, Reserved"

        typ = room_num % 4
        room_tranfrom = room_num // 4
        word = ["People", "Bus", "Boat", "Fleet"]

        if room_tranfrom <= inhotel + self.lst[typ].amount:
            return f"Room Number {room_num}: {word[typ]}, Reserved"
        if room_tranfrom <= inhotel + self.find_max():
            return f"Room Number {room_num}: {word[typ]}, Free"

        return "Room doesn't exist."

    def sort_reserved(self):
        for i in range(self.hotel):
            print(f"{i} ", end="")

        inhotel = self.check_hotel()
        for i in range(self.find_max()):
            start_room = (i + inhotel + 1) * 4
            if i < self.lst[0].amount:
                print(f"{start_room} ", end="")
            if i < self.lst[1].amount:
                print(f"{start_room+1} ", end="")
            if i < self.lst[2].amount:
                print(f"{start_room+2} ", end="")
            if i < self.lst[3].amount:
                print(f"{start_room+3} ", end="")

        print("\nManual: ", end="")
        print(" ".join(self.avl_tree.print_avl_tree(self.man)))

    # Checkin Part
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

    def print_guest_count(self):
        print(f"Hotel: {self.hotel}")
        print(f"People: {self.lst[0].amount}")
        print(f"Bus: {self.lst[1].amount}")
        print(f"Boat: {self.lst[2].amount}")
        print(f"Fleet: {self.lst[3].amount}")
        if self.man is None:
            print("Manual: 0")
        else:
            manual_count = self.avl_tree.count_nodes(self.man)
            print(f"Manual: {manual_count}")

    def print_free_room_count(self):
        inhotel = self.check_hotel()
        inhotel_count = (inhotel + 1) * 4 - self.hotel

        mx = self.find_max()
        lst_count = [0, 0, 0, 0]
        for i in range(len(self.lst)):
            lst_count[i] = mx - self.lst[i].amount
        print(f"Hotel: {inhotel_count}")
        print(f"Guests: {sum(lst_count)}")

    def write_file_reserved(self, file_name):
        f = open(f"{file_name}.txt", "w")
        for room in range(self.hotel):
            f.write(f"Room number {room}: Hotel\n")

        inhotel = self.check_hotel()
        people = 0
        bus, bus_channal = [0, 0], self.lst[1].channal
        boat, boat_channal = [0, 0, 0], self.lst[2].channal
        fleet, fleet_channal = [0, 0, 0, 0], self.lst[3].channal
        for i in range(self.find_max()):
            start_room = (i + inhotel + 1) * 4
            # people
            if i < self.lst[0].amount:
                f.write(f"Room number {start_room}: People : no_{people}\n")
                people += 1
            # bus
            if i < self.lst[1].amount:
                f.write(f"Room number {start_room + 1}: Bus : no_{bus[0]}_{bus[1]}\n")
                bus[0] += 1
                if bus[0] == bus_channal[0]:
                    bus[0] = 0
                    bus[1] += 1

            # boat
            if i < self.lst[2].amount:
                f.write(
                    f"Room number {start_room + 2}: Boat : no_{boat[0]}_{boat[1]}_{boat[2]}\n"
                )
                boat[0] += 1
                if boat[0] == boat_channal[0]:
                    boat[0] = 0
                    boat[1] += 1
                    if boat[1] == boat_channal[1]:
                        boat[1] = 1
                        boat[2] += 1
            # fleet
            if i < self.lst[3].amount:
                f.write(
                    f"Room number {start_room + 3}: Fleet : no_{fleet[0]}_{fleet[1]}_{fleet[2]}_{fleet[3]}\n"
                )
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

        self.avl_tree.write_to_file(self.man, f)

        f.close()

    def memory_usage(self):
        return getsizeof(self)


def print_menu():
    print("\n=== Thep Ang Yai Hotel Service ===")
    print("1. จำนวนแขกที่มาในแต่ละช่องทาง")
    print("2. เพิ่มหมายเลขห้องแบบ Manual")
    print("3. ลบหมายเลขห้องแบบ Manual")
    print("4. การจัดเรียงลำดับหมายเลขห้อง")
    print("5. ค้นหาหมายเลขห้อง")
    print("6. แสดงจำนวนห้องที่ว่าง")
    print("7. เขียนผลลัพธ์ลงไฟล์")
    print("8. แสดงหน่วยความจำที่ใช้")
    print("9. แสดงคำสั่งใหม่")
    print("0. เริ่มระบบใหม่")
    print("พิมพ์ exit เพื่อออกจากโปรแกรม")
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
            inp = list(map(int, inp.split(",")))
            if len(inp) != 2:
                print("Invalid Format!!!")
                continue
            time_start = time()
            con.bus_check_in(inp[1], inp[0])
            break
        except:
            print("Invalid Format!!!")
    time_end = time()
    print(f"time usage: {time_end-time_start}")
    print()

    # Boat
    print("Boat check_in. (boat, bus, people)")
    while True:
        inp = input("Enter Boat check in: ")
        try:
            inp = list(map(int, inp.split(",")))
            if len(inp) != 3:
                print("Invalid Format!!!")
                continue
            time_start = time()
            con.boat_check_in(inp[2], inp[1], inp[0])
            break
        except:
            print("Invalid Format!!!")
    time_end = time()
    print(f"time usage: {time_end-time_start}")
    print()

    # Fleet
    print("Fleet check_in. (fleet, boat, bus, people)")
    while True:
        inp = input("Enter Fleet check in: ")
        try:
            inp = list(map(int, inp.split(",")))
            if len(inp) != 4:
                print("Invalid Format!!!")
                continue
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
            if inp == "1":
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
                con.sort_reserved()

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
            print("Error")


def main3():
    while True:
        con = Controller()
        print("--- Thep Ang Yai Hotel Service ---")
        print("-" * 34)

        normal_check_in(con)
        if select_service(con) == -1:
            return


if __name__ == "__main__":
    main3()
