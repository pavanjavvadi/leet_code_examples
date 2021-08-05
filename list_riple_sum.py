from typing import List, Tuple

def triple_sum(nums: List[int]) -> List[Tuple[int]]:

    result = set()

    for i in range(len(nums)):

        dic = {}

        for j in range(i+1, len(nums)):

            diff = 0 - (nums[j] + nums[i])

            if diff in dic:
                result.add((tuple(sorted((nums[j], nums[i], diff)))))
                print(f"result========{result}")

            dic[nums[j]] = (nums[j], diff)
            print(dic)

    return list(result)

print(triple_sum([-1,0,1,2,-1,-2]))