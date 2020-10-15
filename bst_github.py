class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE in order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does in-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if cur is None:
            return
            # recursive case for left subtree
        if cur.left:
            self._str_helper(cur.left, values)
            # store value of current node
        values.append(str(cur.value))
        # recursive case for right subtree
        if cur.right:
            self._str_helper(cur.right, values)

    def search(self, value, node):
        """
        Helper function to search for a node in the tree
        """

        # Node not found
        if self.root is None:
            return None
        else:
            if node == None:
                return None
                # Traverse left
            if value < node.value:
                return self.search(value, node.left)
                # Traverse right
            elif value > node.value:
                return self.search(value, node.right)
                # Node found
            else:
                return node

    def add_helper(self, node, value):
        """
        Add helper method function
        """
        if value < node.value:  # Value is less than current node, go left
            if node.left is None:
                node.left = TreeNode(value)  # if none, node.left is value
            else:
                self.add_helper(node.left, value)

        else:
            if node.right is None:  # Value is greater than current node, go right
                node.right = TreeNode(value)  # if none, node right is value
            else:
                self.add_helper(node.right, value)

    def add(self, value: object) -> None:
        """
        Add a node to the tree
        """

        if self.root == None:
            self.root = TreeNode(value)
        else:
            self.add_helper(self.root, value)

    def contains_helper(self, node, value) -> int:
        """
        contains helper
        """

        if (node is None):  # establish base case
            return False

        if (node.value == value):
            return True
        elif (value < node.value):  # Value is less than current node, traverse left
            return self.contains_helper(node.left, value)
        elif (value > node.value):  # Value is greater than current node, traverse right
            return self.contains_helper(node.right, value)

        return False

    def contains(self, value: object) -> bool:
        """
        Checks if a value is present in the tree
        """
        if self.root == None:
            return False
        else:
            return self.contains_helper(self.root, value)

    def get_first(self) -> object:
        """
        Gets the first element of the tree aka root
        """
        if (self.root == None):
            return None
        else:
            return self.root.value

    def remove_first(self) -> bool:
        """
        Remove the first value
        """
        if self.root is None:  # establish base case
            return False

        else:
            if (self.root.left is None and self.root.right is None):  # if the root has 0 children
                self.root = None
                return True

            elif (self.root.right is None):  # if the node has 1 child on left
                self.root = self.root.left
                return True

            else:
                previous = None  # keep position of previous node
                temp = self.root.right
                if temp.left is None:
                    # check if we swap the left node
                    temp.left = self.root.left
                    self.root = temp
                    return True
                while temp.left is not None:
                    # if not keep looping
                    previous = temp
                    temp = temp.left
                previous.left = temp.right  # remove temp node since previous.left is nowtemp.right
                temp.left = self.root.left
                temp.right = self.root.right  # do same thing to left
                self.root = temp  # assign new root position

                return True

    def find_min(self, node):
        """
        find min hlper function to find deepest node of tree
        """

        if (node.left is None):
            return node
        else:
            return self.find_min(node.left)

    def remove_helper(self, node, parent_node, value):
        """
        remove helper
        """
        # global remove_node, parent_node

        if node is None:  # if node is none, return none
            return None

        if self.contains(value) == False:  # if it doesnt contain the value, return false
            return None

        #dont need this part
        #if node.left is not None and value == node.left.value:
            ## check value on left side
            #parent_node = node
            #remove_node = node.left

        #dont need this part
        #elif (node.right is not None and value == node.right.value):
            ## check value on right side
            #parent_node = node
            #remove_node = node.right

        elif (value < node.value and node.left is not None):
            return self.remove_helper(node.left, node, value)  # determine side for recurrsion

        elif (value > node.value and node.right is not None):
            return self.remove_helper(node.right, node, value)  # determine side for recurrsion

        elif value == node.value:
            remove_node = node
        #dont need this part
        #else:  # case when value == node.value
            #remove_node = node

        # establish cases for removal
        # if the node to removed is has zero children
        if remove_node.left is None and remove_node.right is None:
            if parent_node is None:
                self.root = None
            elif parent_node.left == remove_node:
                parent_node.left = None
            elif parent_node.right == remove_node:
                parent_node.right = None

        # if node to be removed has 1 child
        elif remove_node.left is None:
            if parent_node is None:  # if the remove is the root node
                self.root = remove_node.right
            elif parent_node.left == remove_node: #if the remove is on the left
                parent_node.left = remove_node.right
            elif parent_node.right == remove_node: #if the remove is on the right
                parent_node.right = remove_node.right

        elif remove_node.right is None:
            if parent_node is None:
                self.root = remove_node.left
            elif parent_node.left == remove_node:
                parent_node.left = remove_node.left
            elif parent_node.right == remove_node:
                parent_node.right = remove_node.left


        else:
            # find the value to replace and replace it
            replace_node = self.find_min(remove_node.right)  # find the minimum of with helper function
            replace_value = replace_node.value  # to replace with

            if replace_value < remove_node.value:
                # if the value is less than  the replacement value
                self.remove_helper(remove_node.left, remove_node, replace_value)
                remove_node.value = replace_value  # replace the value

            elif replace_value > remove_node.value:
                # if the value greater than the remove_value
                self.remove_helper(remove_node.right, remove_node, replace_value)
                remove_node.value = replace_value  # replace the value

        return remove_node

    def remove(self, value) -> bool:
        """
        removes given node from tree
        """
        if self.root == None:  # check if tree is empty
            return False

        else:
            node_removed = self.remove_helper(self.root, None, value)  # send parent as none
            if node_removed is None:  # if node is empty, return false
                return False
            else:
                return True

    def preorder_helper(self, node, preoTrav):
        """
        Helper function for Preorder traversal
        """

        if (node is not None):
            preoTrav.enqueue(node.value)  # visit
            self.preorder_helper(node.left, preoTrav)  # left
            self.preorder_helper(node.right, preoTrav)  # right

    def pre_order_traversal(self) -> Queue:
        """
        Preorder Traversal VLO
        """

        if (self.root == None):
            return Queue()

        preoTrav = Queue()
        current_node = self.root

        self.preorder_helper(current_node, preoTrav)

        return preoTrav

    def inorder_helper(self, node, ioTrav):
        """
        In order Trav Helper
        """

        if node is not None:
            self.inorder_helper(node.left, ioTrav)  # left
            ioTrav.enqueue(node.value)  # visit
            self.inorder_helper(node.right, ioTrav)  # right

    def in_order_traversal(self) -> Queue:
        """
        In order Traversal LVO
        """
        if self.root == None:
            return Queue()

        ioTrav = Queue() #set queue object
        current_node = self.root #set the current node to the root
        self.inorder_helper(current_node, ioTrav)

        return ioTrav

    def post_order_helper(self, node, poTrav):
        """
        Post order Trav helper
        """

        if node is not None:
            self.post_order_helper(node.left, poTrav)  # left
            self.post_order_helper(node.right, poTrav)  # right
            poTrav.enqueue(node.value)  # visit

    def post_order_traversal(self) -> Queue:
        """
        Process all levels post orderly LRV
        """
        if self.root == None:
            return Queue()  # create queue object

        poTrav = Queue()
        current_node = self.root

        self.post_order_helper(current_node, poTrav)

        return poTrav

    def by_level_traversal(self) -> Queue:
        """
        Process all levels of the tree starting at the root then
        the children of the root
        """

        if self.root is None:
            return Queue()  # return a Queue object is None as base case

        blTrav = Queue()  # node tracker queue
        blTrav.enqueue(self.root)
        tree_queue = Queue()  # queue containing the result of traversal

        while (not blTrav.is_empty()):
            current_node = blTrav.dequeue() #the current node we are one
            tree_queue.enqueue(current_node) #add the current node to the queue
            if current_node.left is not None:  # traverse left side
                blTrav.enqueue(current_node.left)

            if current_node.right is not None:  # traverse right side
                blTrav.enqueue(current_node.right)

        return tree_queue

        #############This method works but implements append method####################
        # blTrav = [self.root]
        # index = 0 #set level we are traversing
        # tree_queue = Queue() #create Queue object for levels

        # while True:
        #     try:
        #         current_node = blTrav[index] #set current node by index 0

        #         if current_node.left is not None: #traverse left side
        #             blTrav.append(current_node.left)

        #         if current_node.right is not None: #traverse right side
        #             blTrav.append(current_node.right)

        #         index += 1
        #     except:
        #         break

        # for node in blTrav: #for each node, enqueue
        #     tree_queue.enqueue(node)

        #return tree_queue

    def is_full_helper(self, node) -> bool:
        """
        Helper for is_full
        """
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            return False  # if not full return False

        if node.left is not None:
            full_left = self.is_full_helper(node.left)  # if left node isn't empty

        if node.right is not None:
            full_right = self.is_full_helper(node.right)  # if right node isn't empty

        if node.left is None and node.right is None:  # if there are no nodes, return True
            return True

        else:
            return full_left and full_right

    def is_full(self) -> bool:
        """
        Check to see if a tree is full. Empty tree is considered full. Full tree
        has all interior nodes with two children
        """

        if self.root is None:  # empty tree
            return True
        if self.root.left is None and self.root.right is None:  # Tree with only one node
            return True

        else:
            return self.is_full_helper(self.root)

    def is_complete_helper(self, node, index, number_of_nodes) -> bool:
        """
        Helper for is complete
        """

        if node is None:  # establish base case
            return True

        if index >= number_of_nodes:  # if index is greater than the number of nodes, return false
            return False
        else:
            # else hit recursion, and just to next index and size for left and right
            return (self.is_complete_helper(node.left, 2 * index + 1, number_of_nodes)) and (
                self.is_complete_helper(node.right, 2 * index + 2, number_of_nodes))

    def is_complete(self) -> bool:
        """
        Checks if a list is complete. A complete list is perfect except for the deepest level.
        """

        # Empty tree or tree with one node is complete
        if (self.root is None or (self.root.left is None and self.root.right is None)):
            return True
        else:
            index = 0  # establish base index for traversal
            node_count = self.size()  # size
            return self.is_complete_helper(self.root, index, node_count)

    def is_perfect(self) -> bool:
        """
        Determines if a tree is perfect. Perfect Tree has 2h leaves and 2^(h-1)-1
        total nodes
        """
        count = self.size()
        if count == 0:
            return True
        perfect = 1
        while count > 0:
            count -= perfect  # subtract the nodes (2^h-1)-1
            perfect *= 2  # multiply by two for counting the leaves
            if count == 0 and self.is_full():  # if count is zero, tree is full
                return True
        return False

    def size_helper(self, root):
        """
        Size helper
        """
        if root is None:  # set base case
            return 0
        size = 1  # initialize count at 1
        if root.left is not None:  # if not none, add to count
            size += self.size_helper(root.left)

        if root.right is not None:  # if not none, add to count
            size += self.size_helper(root.right)

        return size

    def size(self) -> int:
        """
        Return the size of the tree
        """
        return self.size_helper(self.root)

    def height_helper(self, root):
        """
        Helper function for height
        """
        if root is None:
            return -1  # if empty, height is -1
        heightLeft = self.height_helper(root.left)
        heightRight = self.height_helper(root.right)
        return max(heightLeft, heightRight) + 1  # return the greater of the two sides and adjust height

    def height(self) -> int:
        """
        Returns the height(depth) of the tree
        """
        return self.height_helper(self.root)

    def count_leaves_helper(self, root):
        """
        Helper function for count_leaves
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.count_leaves_helper(root.left) + self.count_leaves_helper(root.right)

    def count_leaves(self) -> int:
        """
        Counts the leaves
        """
        return self.count_leaves_helper(self.root)

    def count_unique_helper(self, root, uniqueList):
        """
        Count Unique Helper
        """
        if root is None:  # set base case
            return 0

        if root.value in uniqueList:  # if root value is in the list, check next values on both sides
            return self.count_unique_helper(root.left, uniqueList) + self.count_unique_helper(root.right, uniqueList)
        else:
            uniqueList.append(root.value)  # else append unique value to list so we know it's new
            return self.count_unique_helper(root.left, uniqueList) + self.count_unique_helper(root.right,
                                                                                              uniqueList) + 1

    def count_unique(self) -> int:
        """
        Count the unique (non-duplicate values) in the tree
        """
        uniqueList = [] #create list object to keep track of values
        return self.count_unique_helper(self.root, uniqueList)

        # BASIC TESTING - PDF EXAMPLES


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    """ add() example #1 """
    print("\nPDF - method add() example 1")
    print("----------------------------")
    tree = BST()
    print(tree)
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree)
    tree.add(15)
    tree.add(15)
    print(tree)
    tree.add(5)
    print(tree)

    """ add() example 2 """
    print("\nPDF - method add() example 2")
    print("----------------------------")
    tree = BST()
    tree.add(10)
    tree.add(10)
    print(tree)
    tree.add(-1)
    print(tree)
    tree.add(5)
    print(tree)
    tree.add(-1)
    print(tree)

    """ contains() example 1 """
    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    """ contains() example 2 """
    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    """ get_first() example 1 """
    print("\nPDF - method get_first() example 1")
    print("----------------------------------")
    tree = BST()
    print(tree.get_first())
    tree.add(10)
    tree.add(15)
    tree.add(5)
    print(tree.get_first())
    print(tree)

    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    #tree = BST([54, 32, 21, 49, 63, 70, 68])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([10, 15, 5])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)

    """ Traversal methods example 1 """
    print("\nPDF - traversal methods example 1")
    print("---------------------------------")
    #tree = BST([10, 20, 5, 15, 17, 7, 12])
    tree = BST([54, 32, 21, 49, 63, 70, 68])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Traversal methods example 2 """
    print("\nPDF - traversal methods example 2")
    print("---------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = BST()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')








