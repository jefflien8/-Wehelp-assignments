#1
def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    result=(min+max)/2*(max-min+1)
    print(result)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

#2
def avg(data):
    # 請用你的程式補完這個函式的區塊
    num=data['count']
    sum=0
    i=0
    for i in range (data['employees'][i]['salary']):
        if i==num:
            print(sum/num)
        if (i<num):
            sum=sum+data['employees'][i]['salary']

avg({
    "count":3,
    "employees":[
     {
        "name":"John",
        "salary":30000
    },
    {
        "name":"Bob",
        "salary":60000
    },
    {
        "name":"Jenny",
        "salary":50000
    }
    ]
}) # 呼叫 avg 函式

#3
def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    m1=max(nums)
    if m1==0:
        n1=min(nums)
        nums.remove(n1)
        n2=min(nums)
        print(n1*n2)
    if m1>0:
        nums.remove(m1)
        m2=max(nums)
        print(m1*m2)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

#4
def twoSum(nums, target):
    # your code here
    for a in nums:
        for b in nums:
            if a+b==target:
                result=[nums.index(a),nums.index(b)]
                return result
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#5
def maxZeros(nums):
    #請用你的程式補完這個函式的區塊
    i=0
    a=0
    b=0
    for i in range (len(nums)):
        if 0!=nums[i]:
            a=0    
        else:
            a+=1
        if a>b:
            b=a
    print(b)            
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3

