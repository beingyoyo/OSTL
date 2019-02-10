use employee;
print ("Enter employee name:");
$name=<STDIN>;
print ("Enter employee ID:");
$id=<STDIN>;
print ("Enter employee status:");
$s=<STDIN>;
my $object=new employee($name,$id,$s);


c065@comp:~$ perl emp.pl
Enter employee name:Yash 
Enter employee ID:02
Enter employee status:Student
Employee Name: Yash

Employee ID: 02

Employee Status:Student

