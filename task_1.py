class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def delete_node(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Злиття двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        result = LinkedList()
        result.head = dummy.next
        return result

    # Допоміжна функція для розбиття списку на дві частини
    def split_list(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    # Сортування списку злиттям
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        left, right = self.split_list(self.head)
        left_list = LinkedList()
        right_list = LinkedList()
        left_list.head = left
        right_list.head = right

        left_list.merge_sort()
        right_list.merge_sort()

        sorted_list = LinkedList.merge_sorted_lists(left_list.head, right_list.head)
        self.head = sorted_list.head


# Приклад використання

# Створюємо перший список
llist1 = LinkedList()
llist1.insert_at_end(3)
llist1.insert_at_end(1)
llist1.insert_at_end(4)
llist1.insert_at_end(2)
print("Оригінальний список:")
llist1.print_list()

# Реверсування списку
llist1.reverse()
print("Список після реверсування:")
llist1.print_list()

# Сортування списку
llist1.merge_sort()
print("Відсортований список:")
llist1.print_list()

# Створюємо другий відсортований список
llist2 = LinkedList()
llist2.insert_at_end(6)
llist2.insert_at_end(5)
llist2.insert_at_end(7)
print("Другий відсортований список:")
llist2.print_list()

# Сортуємо другий список
llist2.merge_sort()

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted_lists(llist1.head, llist2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()
