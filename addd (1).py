class LinkedList:

    class Item:
        value = None
        next = None

        def init(self, value):
            self.value = value

    head:Item = None
    
    def append_begin(self, value):
        item = LinkedList.Item()
        item.value = value
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item()
            self.head.value = value
            return
        
        while current.next:
            current = current.next
        item = LinkedList.Item()
        item.value = value
        current.next = item
    
    def len_link_list(self):
        cur = self.head
        tot = 1
        while cur.next != None:
            cur = cur.next
            tot += 1
        return tot
    
    def get_all_list(self):
        st = ''
        cur = self.head
        while cur:
            st += f'{cur.value} '
            cur = cur.next
        return st

    def append_by_index(self, value, index):
        '''Метод всавляет значение по указанному индексу,
        оставшиеся элементы сдвигаются'''
        dl = int(self.len_link_list())+1

        if abs(index) > dl:
            raise ValueError(f'Индекс {index} находится вне длины списка')
        
        if index < 0:
            index = abs(index % dl)

        if index == 0:
            self.append_begin(value)
            return
        
        elif index == dl:
            self.append_end(value)
            return

        current = self.head
        for i in range(index-1):
            current = current.next
        
        item = LinkedList.Item()
        item.value = value
        posle = current.next
        current.next = item
        item.next = posle


    def del_first(self):
        cur = self.head
        next = cur.next
        self.head = next
        
    def del_last(self):
        cur = self.head
        if self.len_link_list() == 1:
            self.head = None
            return
        #for _ in range(self.len_link_list()-2):
        while cur.next.next != None:
            cur = cur.next
        cur.next = None
        
    def del_po_ind(self, index):
        dl = int(self.len_link_list())
        
        if abs(index) > dl:
            raise ValueError(f'Индекс {index} находится вне длины списка')
        
        if index < 0:
            index = abs(index % dl)

        if index == 0:
            self.del_first()
            return
        
        elif index == dl:
            self.del_last()
            return      

        cur = self.head
        for _ in range(index-1):
            cur = cur.next
        
        cur.next = cur.next.next
        
    def del_first_zn(self, value):
        if str(value) not in self.get_all_list().split():
            raise ValueError(f'Данного значения ({value}) нет в списке')

        cur = self.head 
        while cur.next.value != value:
            cur = cur.next
        
        cur.next = cur.next.next
        

    def del_last_zn(self, value):

        lst = self.get_all_list().split()
        if str(value) not in lst:
            raise ValueError(f'Данного значения ({value}) нет в списке')      

        tot = len(lst)-1
        while lst[tot] != str(value):
            tot -= 1
        
        self.del_po_ind(tot)


#Формирование списка
my_list = LinkedList()
my_list.append_end(2)
my_list.append_end(3)
my_list.append_end(4)
my_list.append_end(5)
my_list.append_end(6)
my_list.append_end(7)
print(my_list.get_all_list(), end='\n\n')

#Добавление по индексу
my_list.append_by_index(33, -3)
print(my_list.get_all_list(), end='\n\n')

#Удаление первого
my_list.del_first()
print(my_list.get_all_list(), end='\n\n')

#Удаление последнего
my_list.del_last()
print(my_list.get_all_list(), end='\n\n')

#Удаление по индексу
my_list.del_po_ind(-3)
print(my_list.get_all_list(), end='\n\n')

#Удаление первого вхождения
my_list.append_end(4)
print(my_list.get_all_list(), end='\n\n')
my_list.del_first_zn(4)
print(my_list.get_all_list(), end='\n\n')

#Удаление последнего вхождения
my_list.append_end(33)
print(my_list.get_all_list(), end='\n\n')
my_list.del_last_zn(33)
print(my_list.get_all_list(), end='\n\n')
# print(my_list.head.value)
# print(my_list.head.next.value)
# print(my_list.head.next.next.value)
# print(my_list.head.next.next.next.value)
# print(my_list.head.next.next.next.next.value)
# print(my_list.head.next.next.next.next.next.value)
# print(my_list.head.next.next.next.next.next.next.value)