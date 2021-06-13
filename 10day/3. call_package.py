import myNums.nums as nums

def main():
    nums.addNum1()
    nums.addNum1()
    nums.addNum2(3)
    nums.addNum2(4)
    nums.printNums()
    idx = nums.search1(1)
    nums.printIdx(idx)
    idx = nums.search2(2)
    nums.printIdx(idx)
    idx = nums.search3()
    nums.printIdx(idx)
    nums.search4()
    nums.delNum1(3)
    nums.printNums()
    nums.delNum2()
    nums.delNum2()
    nums.printNums()

main()