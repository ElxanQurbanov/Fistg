class Solution:
    def threeSum(self, nums):
        nums.sort()  # İlk olaraq siyahını sıralayırıq
        result = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # Eyni dəyəri atlayırıq

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = a + nums[left] + nums[right]

                if total < 0:
                    left += 1  # Cəm sıfırdan kiçikdirsə, soldan irəliləyirik
                elif total > 0:
                    right -= 1  # Cəm sıfırdan böyükdürsə, sağdan geri çəkilirik
                else:
                    # Cəm sıfırdır, nəticəyə əlavə edirik
                    result.append([a, nums[left], nums[right]])

                    # Eyni dəyərləri atlayırıq
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


# Nümunə istifadə
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
