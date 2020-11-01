# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

def findMedianSortedArrays(self, nums1, nums2):

        newNums = []
        totalLen = len(nums1) + len(nums2)
        p1 = 0
        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                newNums.append(nums1[p1])
                p1 += 1
            else:
                newNums.append(nums2[p2])
                p2 += 1
        newNums.extend(nums1[p1:])
        newNums.extend(nums2[p2:])
        if len(newNums)%2 == 0:
            return (float(newNums[(len(newNums)//2)] + newNums[(len(newNums)//2)-1]))/2
        else:
            return(newNums[len(newNums)//2])
