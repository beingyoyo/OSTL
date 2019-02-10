package employee;
sub new
{
    my $class=shift;
    my $self={_employeeName=>shift,_employeeID=>shift,_employeeStat=>shift};
    print "Employee Name: $self->{_employeeName}\n";
    print "Employee ID: $self->{_employeeID}\n";
    print "Employee Status:$self->{_employeeStat}\n";
    bless $self, $class;
    return $self;
}
1
