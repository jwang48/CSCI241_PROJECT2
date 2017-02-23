class Linked_List:
  
  class _Node:
    
    def __init__(self, val):
      self._val = val
      self._next = None
      self._previous = None
      # declare and initialize the private attributes
      # for objects of the Node class.
      

  def __init__(self):
    self._Header = self._Node(None);
    self._Trailer = self._Node(None)
    self._Header._next = self._Trailer
    self._Trailer._previous = self._Header
    self._size = 0
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    

  def __len__(self):
    return self._size
    # return the number of value-containing nodes in 
    # this list.
    

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    newest = self._Node(val)
    newest._next = self._Trailer
    newest._previous = self._Trailer._previous
    self._Trailer._previous._next = newest
    self._Trailer._previous = newest
    self._size += 1

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    if (index < 0 or index >= self._size):
      raise IndexError
    newest = self._Node(val)
    if (self._size == 0):
      self.append_element(val)
    cur = self._Header
    for i in range(index):
        cur = cur._next
    newest._next = cur._next
    newest._previous = cur
    cur._next._previous = newest
    cur._next = newest
    self._size +=1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    if (index < 0 or index >= self._size):
      raise IndexError

    current = self._Header._next
    pos = 0

    while pos < index:
      current = current._next
      pos += 1
    val = current._val
    current._previous._next = current._next
    current._next._previous = current._previous
    self._size -= 1
    return val 

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.

    if (index < 0 or index >= self._size):
      raise IndexError

    else:

      current = self._Header._next
      pos = 0
      while pos < index:
        current = current._next  
        pos += 1
      return current._val

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    if (self._size <= 1):
      return

    val = self.remove_element_at(0)
    self.append_element(val)
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    linklist = []
    num = self._size 
    while num > 0:
      val = self.get_element_at(num-1)
      linklist.insert(0,val)
      num -= 1
    return str(linklist)



  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self.__iter_index = 0
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
      # if there are no more values left,
    # terminate the iteration. Python does this automatically
    # when it receives the exception generated here.
    if self.__iter_index == self._size:
      raise StopIteration
    # each time a new value is requested (such as
    # a cycle in a for loop), grab the value, up the
    # index to prepare for the next call, and return
    # the value.
    to_return = self.get_element_at(self.__iter_index)
    self.__iter_index = self.__iter_index + 1
    return to_return


    

if __name__ == '__main__':
  pass
  
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests

  #### APPEND TEST ####
  
  # test = Linked_List();
  # test.append_element(3);
  # test.append_element(5);
  # test.append_element(7);
  # test.append_element(10);
  # test.append_element(100);
  # print (test.__str__())

  #### INSERTION TEST ####
  
  # test = Linked_List();
  # test.append_element("A");
  # test.append_element("B");
  # test.append_element("C");
  # print (test.__str__())

  # test.insert_element_at('HELLO',1);
  # print (test.__str__())

  # print (test._size)


  #### ROTATION TEST ####

  # test.rotate_left();
  # print (test.__str__())
  
  # test.rotate_left();
  # print (test.__str__())
  
  # test.rotate_left();
  # print (test.__str__())


  #### ITERATION TEST ####

  # ITER_TEST = Linked_List()
  # ITER_TEST.append_element(5)
  # ITER_TEST.append_element(2)
  # ITER_TEST.append_element(-4)
  # ITER_TEST.append_element(1)

  # print (ITER_TEST.__str__())

  # for val in ITER_TEST:
  #   print(str(val))
