"""
A quick heads up! In the next lecture we will create the insert() method.
For those astute programmers, you may notice that the solution has a bug
if index === 0. In this case, all you need to do is to insert into the
code a condition:

if (index === 0) {
  this.prepend(value);
  return this.printList();
}

"""