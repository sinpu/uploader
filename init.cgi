# setting file
# module / variable initialize

use strict;
my %cf;
# % : hash var
# my : scorp var


# base setting
# version manage
$cf{ version } = 'UPLOADER v1.01';

# manage pass
$cf{ password } = 'yuki5486';

# ' : static literal
# " : dynamic literal

# appropriate extension
$cf{ ap_text } = 1; #TEXT
$cf{ ap_c } = 1;    #C Program
$cf{ ap_o } = 1;    #Program binary
$cf{ ap_pdf } = 1;  #PDF
$cf{ ap_jpeg } = 0; #JPEG

# set max data size
$cf{ maxdata } = 5242880; #5MB

