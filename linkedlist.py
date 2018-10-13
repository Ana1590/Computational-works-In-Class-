class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

	def __init__(self,data):
		self.head = Node(data)
		self.size = 1

	def add(self,data):
		current = self.head
		while current.next is not None:
			current = current.next
		current.next = Node(data)
		self.size += 1

	def set(self,index,data):
		node = Linkedlist._get_node_at(self,index)
		if node is not None:
			node.data = data
			return True
		return False

	def delete(self,index):

		if self.size == 0:
			return False
		previous_node = Linkedlist._get_node_at(self,index-1)
		node = Linkedlist._get_node_at(self,index)
		if node is None:
			return False
		if previous_node is None:
			self.head = node.next
			self.size -= 1
			return True
		previous_node.next = node.next
		self.size -= 1
		return True

	def get(self,index):
		
		node = Linkedlist._get_node_at(self,index)
		if node is not None:
			return node.data
		return None

	def _get_node_at(self,index):

		if index > self.size or index < 0:
			return None
		current = self.head
		for i in range(index):
			current = current.next
		return current


	def __len__(self):
		return self.size

	def __str__(self):

		data = ''
		current = self.head
		while current is not None:
			data = data + current.data + "\n"
			current = current.next
		return data[:-1]


my_list = Linkedlist("first")
my_list.add("secon") 
my_list.add("third")
my_list.set(1,'second')

 
print(my_list)
print(len(my_list))
print(my_list.get(1))

my_list.delete(0)
print('after delete')
print(my_list)

my_list.delete(1)
print('after second delete')
print(my_list)

my_list.delete(2)
print('after third delete')
print(my_list)
print(len(my_list))
