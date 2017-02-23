from Linked_List import Linked_List

def Josephus(ll):
  # solve the Josephus problem following the following algorithm:
  # rotate the list to the left by one position circularly, 
  # and then delete the first element; 
  # repeat it until there is only one element left in the list.
  # print the sequence of survivors after each death, 
  # and finally print the survivor’s number.
  while (ll._size > 1):
    ll.rotate_left();
    ll.remove_element_at(0);
    print (ll.__str__())

  print ("The survivor is " + str(ll.get_element_at(0)) + ".")
  

if __name__ == '__main__':
  pass
  # create a new doubly linked list object called ll
  # with 41 elements named 1 to 41.

  ### REBEL TEST ###
  # rebel = Linked_List()

  # for i in range(21):
  #   rebel.append_element(i+1)

  # print("Initial order:", rebel)
  # Josephus(rebel)


  ### JOSEPHUS TEST###

  # ll = Linked_List()

  # for i in range(41):
  #   ll.append_element(i+1)

  # print("Initial order:", ll)
  # Josephus(ll)