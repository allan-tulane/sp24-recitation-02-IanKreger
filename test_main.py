from main import *

def test_simple_work():
  assert simple_work_calc(10,2,2)==36
  assert simple_work_calc(20,3,2)==230
  assert simple_work_calc(30,4,2)==650

  assert simple_work_calc(5,2,2) == 13
  assert simple_work_calc(10,3,4) == 16
  assert simple_work_calc(20,5,2)==1070



def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300

  assert work_calc(5, 2, 2,lambda n: 1) == 7
  assert work_calc(20, 3, 2, lambda n: n*n) == 746
  assert work_calc(20, 4, 2, lambda n: n) == 524
 `  

def test_compare_work():

  def work_fn1(n):
    a = 10
    b = 2
    c = 2
    f = lambda n: n**c
    return work_calc(n,a,b,f)

  def work_fn2(n):
    a = 5
    b = 3
    c = 2
    f = lambda n: n**c
    return work_calc(n,a,b,f)

  res = compare_work(work_fn1, work_fn2)
  print(res)

	
def test_compare_span():
  def span_function1(n):
    a = 5
    b = 2
    f = lambda n:n
    return span_calc(n,a,b,f)
  def span_function2(n):
    a = 5
    b = 4
    f = lambda n:1
    return span_calc(n,a,b,f)
  res = compare_span(span_function1,span_function2)
