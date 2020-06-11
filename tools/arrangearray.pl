#!/usr/bin/perl
use strict;

chomp(my $columns = <STDIN>);
chomp(my @entries = <STDIN>);

my $rows = int((@entries + $columns - 1) / $columns);
my $full_rows = @entries - $rows * $columns + $rows;
my $col;
my $row;

# Show full rows:
for ($row = 0; $row < $full_rows; ++$row) {
  for ($col = 0; $col < $columns; ++$col) {
    my $entry = $row + $rows * $col;
    print "@entries[$entry]\n";
  }
  print "\n";
}
# Show the rest of the rows:
for ( ; $row < $rows; ++$row) {
  for ($col = 0; $col < $columns - 1; ++$col) {
    my $entry = $row + $rows * $col;
    print "@entries[$entry]\n";
  }
  print "\n";
}
