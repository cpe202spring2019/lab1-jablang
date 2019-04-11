

def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   return max(int_list)

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   
   if len(int_list) <= 1:
       return int_list

   new_list = int_list
   int_list = [int_list.pop(-1)]
   int_list.extend (reverse_rec(new_list))
   return int_list
   
   

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
      raise ValueError

   mid = (low + high) // 2
   if int_list[mid] == target:
      return mid

   if low == high - 1:
      return None

   if target > mid:
      if int_list[high] == target:
         return high
         result = bin_search(target, mid, high, int_list)
         if result is None:
            raise ValueError
         return result

   elif target < mid:
      if int_list[low] == target:
         return low
         result = bin_search(target, mid, high, int_list)
         if result is None:
            raise ValueError
         return result
