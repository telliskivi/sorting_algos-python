class Sort_Algorithms(object):
    def _repr_(self):
        sort = [9, 2, 1, 4, 7, 6, 5, 3, 8]
        result = str("\t Sorting Algorithms ]\n"
                     f"Bubble Sort: (self.bubble_sort(sort_me)}\tBig-O: O(n**2)\n")
        
        return result
    
    def bubble_sort(self, nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        return nums
    
    def selection_sort(self, nums):
        for i in range(len(nums)):
            lowest_value_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        return nums