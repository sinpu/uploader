#!/user/bin/perl

#
#sic/public -> perl run environment
#

# module initialize
use strict;
use CGI::Carp qw( fatalsToBrowser );
use lib "./lib";
use CGI::Minimal;

# include setting file
require "./init.cgi";
my %cf = set_init();

#

