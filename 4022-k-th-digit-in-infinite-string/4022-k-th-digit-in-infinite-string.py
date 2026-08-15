class Solution:
    def kthDigit(self, k: int) -> int:
        x=k
        if k<=9:
            return k
        k-=9
        d=2
        b=1
        while True:
            blocks=9*(10**(d-2))
            size=blocks*10*d
            if k>size:
                k-=size
                b+=blocks
                d+=1
            else:
                block=(k-1)//(10*d)
                pos=(k-1)%(10*d)
                b+=block
                start=10*b
                num=start+pos//d if b%2==0 else start+9-pos//d
                return int(str(num)[pos%d])