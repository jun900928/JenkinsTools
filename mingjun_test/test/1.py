def fourSum(nums, target):
        nums.sort()
        if len(nums)<4:
            return []
        result=[]
        i=0
        while i<len(nums)-3:
            ntarget=0-nums[i]
            j=i+1
            while j<len(nums)-2:
                nntarget=ntarget-nums[j]
                print nntarget
		low=j+1
                high=len(nums)-1
                while low < high:
                    if nums[low]+nums[high]==nntarget and [nums[i],nums[j],nums[low],nums[high]] not in result:
			print [nums[i],nums[j],nums[low],nums[high]]
                        result.append([nums[i],nums[j],nums[low],nums[high]])
                        low+=1
                        high-=1
                    elif nums[low]+nums[high]<nntarget:
			print nums[low], nums[high],nntarget
                        low+=1
                    elif nums[low]+nums[high]>nntarget:
			print nums[low], nums[high],nntarget
                        high-=1
		    else:
			low+=1
                        high-=1
		j+=1
	    i+=1
        return result

nums=[0,0,0,0]
print fourSum(nums,0)
