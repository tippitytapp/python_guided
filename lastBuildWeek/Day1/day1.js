array1 = [1, 2, 3, 1]
array2 = [1, 2, 3, 4]
array3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
array4 = []
array5 = [2, 14, 18, 22, 22]

function containsDuplicates(nums) { 
    nums.sort()
    if (nums.length === 0) {
        return false
    } else {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === nums[i + 1]) {
                return true
            } else if (nums[i] === nums[-1]) {
                return true
            }
        }
        return false
    }
}

console.log(containsDuplicates(array1)) // should print true
console.log(containsDuplicates(array2)) // should print false
console.log(containsDuplicates(array3)) // should print true
console.log(containsDuplicates(array4)) // should print false
console.log(containsDuplicates(array5)) // should print true