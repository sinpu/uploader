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

# Main process 1 : data accept
CGI::Minimal::max_read_size( $cf{ maxdata } );
my $cgi = CGI::Minimal->new;
error( 'over capacity' ) if ( $cgi -> truncated );
my %in = parse_form( $cgi );


foreach my $key ( $cgi -> param() ){
	print "$key";
}