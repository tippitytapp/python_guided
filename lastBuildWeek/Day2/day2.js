let numsArray = [2, 7, 11, 15]
let numsArray2 = [3, 2, 4]
let numsArray3 = [3,3]
let tgt = 9
let tgt2 = 6 



function twoSum(nums, target) { 
    let answer = []
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                answer.push(i)
                answer.push(j)
            }
        }
    }
     return answer;
        
    }

console.log(twoSum(numsArray, tgt))
console.log(twoSum(numsArray2, tgt2))
console.log(twoSum(numsArray3, tgt2))

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
