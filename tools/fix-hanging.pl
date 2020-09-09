$d = 0; $h = 0;
$buff = "";
while (<>) {
  if ($_ =~ /\rSec(\d)/) {
    $newd = $1;
    if ($newd > $d && $h) {
      # found hanging paras
      print "
";
      print $sec =~ s/(\d)/$1+1/er =~ s/]/.general]/r =~ s/{.*}/{General}/r;
    }
    print $buff;
    print $_;
    $buff = "";
    $d = $newd; $h = 0; $sec = $_;
  } else {
    $buff .= $_;
    if ($_ =~ /\pnum/) {
      $h = 1;
    }
  }
}
print $buff

