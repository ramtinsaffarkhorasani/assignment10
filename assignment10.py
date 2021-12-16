class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def sum(self,t2):
        h_res=self.h+t2.h
        m_res=self.m+t2.m
        s_res=self.s+t2.s
        if s_res>60:
            s_res-=60
            m_res+=1
        if m_res>60:
            m_res-=60
            h_res+=1
        return h_res,m_res,s_res
    def minus(self,t2):
        if self.s<t2.s:
            self.m-=1
            self.s+=60
        if self.m<t2.s:
            self.h-=1
            self.m+=60
        ht_res=self.h-t2.h
        mt_res=self.m-t2.m
        st_res=self.s-t2.s
        return ht_res,mt_res,st_res
t1=Time(int(input("enter hour time1 ")),int(input("enter minaute time1 ")),int(input("enter second time 1 ")))
t2=Time(int(input("enter hour time2 ")),int(input("enter minaute time2 ")),int(input("enter second time 2 ")))
f=input("what you want i do for you + or -")
if f=="+":
    print(t1.sum(t2))
if f=="-":
    print(t1.minus(t2))  


