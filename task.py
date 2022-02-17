import random

   
def ConstrainedInsert(before,after,initial,item):

  min_index= 0
  max_index= len(initial)-1


#Traverse the list backwards looking for items it has to be after.
  if len(after) > 0:
    for y in range(len(initial)-1, -1, -1):
      if initial[y] in after:
        print(y)
        min_index = y
        break

#Traverse the list backwards looking for items it has to be after.
#### improvement - does it need to start at 0 when there is already a min?

  if len(before) > 0:
    for i ,k in enumerate(initial):
      print(k)
      if k in before:
        print("before   " ,i, k)
        max_index = i
        break
        

  #print(max_index, ' ' ,min_index)
  
 # insert the item at the max index it can be. if max is less than min then throw error 
  if max_index < min_index:
    print('ERROR ', item ,' could not be inserted into the list')
  else:
    initial[max_index  :max_index ] = [item]
    return initial





def test2():
    #Use this to test manual test cases

    before = ['donkey']
    after = []
    initial = ['donkey', 'bear', 'Turtle', 'Kitten', 'bear', 'Kitten', 'bear', 'aardvark']
    item = 'SHRIMP'

    print('Result = ',ConstrainedInsert(before,after,initial,item)) 



   






# #method to return the indexes
# def indexes(subarray,array):
#     indexes=[]

#     for i in subarray:
#         for k in range(len(array)):
#             if i == array[k]:
#                 indexes.append(k)
#                 #print(indexes)
               
#     return indexes


# def ConstrainedInsert(before,after,initial,item):
#     min_index= 0
#     max_index= len(initial)-1

# #dervived by getting the indexes of each occurence of before subarray in initial array
# #First check if the before or after arrays are empty
    
#     if len(before) > 0:
#         max_index = min(indexes(before,initial))

# #minimum index would be the max index returned from 'after' sub array
#     if len(after) > 0:
#         min_index = max(indexes(after,initial))
  
#     #check if the minimum is after the max then insert 
#     if max_index < min_index:
#         print('ERROR ', item ,' could not be inserted into the list')
#     else:
#         initial[min_index +1 :min_index +1 ] = [item]
#         return initial








# These methods are for volume testing the solution - without a ground truth algorithm i can only manually check

def gen_data():
    word_bank=["cat",  "dog",  "monkey",  "lion",  "fish",  "aardvark", "lion", "Puppy","Turtle","Rabbit", "parrot","Kitten","mouse","goldfish", 'donkey','tiger','bear']

    # define the size of each array

    num_initial=8
    num_before=2
    num_after = 2


    initial =[]
    before = set()
    after= set()

    while num_initial !=0:
        initial.append(word_bank[random.randint(0,len(word_bank)-1)])
        num_initial -= 1
    
    while num_before !=0:
        before.add(initial[random.randint(0,len(initial)-1)])
        num_before -= 1
    
    #check if word is already in before
    while num_after !=0:
        cand = initial[random.randint(0,len(initial)-1)]
        if cand not in before:
            after.add(cand)
            num_after -= 1
        else:
            continue
    
    return before,after,initial


#this method will use randomly generated arrays and print the results for analysis

def v_test():
    num_tests= 10

    while num_tests !=0:
        before,after,initial = gen_data()
        item = 'SHRIMP'

        print("Before = ",before)
        print("After = ",after)
        print('Initial = ', initial)
        print('Insert == ', item)
        print('Result = ',ConstrainedInsert(before,after,initial,item)) 
        print('============================================')

        num_tests -=1



#test2()
v_test()
