class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        This method sorts an array of integers in-place using the selection sort algorithm.
        It iterates over the array, repeatedly finding the minimum element from the unsorted
        part and moving it to the beginning.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Args:
        nums (List[int]): The list of integers to be sorted.

        Returns:
        None: This method modifies the list in-place.
        """
        
        n = len(nums)  # Get the number of elements in the list

        def swap(x, y):
            """
            Swap the elements at indices x and y in the list.

            Args:
            x (int): The index of the first element.
            y (int): The index of the second element.
            """
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp

        for i in range(n):
            # Start with the assumption that the first element of the unsorted segment is the smallest.
            smallest = i

            # Iterate over the unsorted segment of the array to find the actual smallest element.
            for j in range(i + 1, n):
                # If a smaller element is found, update 'smallest' to the new index.
                if nums[j] < nums[smallest]:
                    smallest = j

            # After finding the smallest element in the unsorted segment,
            # swap it with the first element of the unsorted segment.
            swap(i, smallest)

        # The array is sorted in ascending order at this point.

"""
Time Complexity Calculation:
- The outer loop runs n times where n is the length of the list.
- The inner loop runs decreasingly: n-1, n-2, ..., 1 times.
- Total comparisons: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n^2)

Space Complexity Calculation:
- The space complexity is O(1) because the sorting is done in-place, using only a constant amount of additional space for variables.
"""
