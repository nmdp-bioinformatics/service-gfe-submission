# service-gfe-submission
RESTful Service getting GFE results from raw sequence data

Further documentation is available at [service-gfe-submission.readthedocs.io](http://service-gfe-submission.readthedocs.io/en/latest/index.html)

## Curl

```bash
    
# Get GFE from sequence data #
curl --header "Content-type: application/json" --request POST 
--data '{"locus":"HLA-A","sequence":"TCCCCAGACGCCGAGGATGGCCGTCATGGCGCCCCGAACCCTCCTCCT
GCTACTCTCGGGGGCCCTGGCCCTGACCCAGACCTGGGCGGGTGAGTGCGGGGTCGGGAGGGAAACCGCCTCTGCGGGGAGAAGC
AAGGGGCCCTCCTGGCGGGGGCGCAGGACCGGGGGAGCCGCGCCGGGACGAGGGTCGGGCAGGTCTCAGCCACTGCTCGCCCCCA
GGCTCCCACTCCATGAGGTATTTCTTCACATCCGTGTCCCGGCCCGGCCGCGGGGAGCCCCGCTTCATCGCCGTGGGCTACGTGG
ACGACACGCAGTTCGTGCGGTTCGACAGCGACGCCGCGAGCCAGAGGATGGAGCCGCGGGCGCCGTGGATAGAGCAGGAGGGGCC
GGAGTATTGGGACCAGGAGACACGGAATGTGAAGGCCCAGTCACAGACTGACCGAGTGGACCTGGGGACCCTGCGCGGCTACTAC
AACCAGAGCGAGGCCGGTGAGTGACCCCGGCCGGGGGCGCAGGTCAGGACCCCTCATCCCCCACGGACGGGCCAGGTCGCCCACA
GTCTCCGGGTCCGAGATCCACCCCGAAGCCGCGGGACCCCGAGACCCTTGCCCCGGGAGAGGCCCAGGCGCCTTTACCCGGTTTC
ATTTTCAGTTTAGGCCAAAAATCCCCCCGGGTTGGTCGGGGCTGGGCGGGGCTCGGGGGACTGGGCTGACCGCGGGGTCGGGGCC
AGGTTCTCACACCATCCAGATAATGTATGGCTGCGACGTGGGGTCGGACGGGCGCTTCCTCCGCGGGTACCGGCAGGACGCCTAC
GACGGCAAGGATTACATCGCCCTGAACGAGGACCTGCGCTCTTGGACCGCGGCGGACATGGCGGCTCAGATCACCAAGCGCAAGT
GGGAGGCGGCCCATGAGGCGGAGCAGTTGAGAGCCTACCTGGATGGCACGTGCGTGGAGTGGCTCCGCAGATACCTGGAGAACGG
GAAGGAGACGCTGCAGCGCACGGGTACCAGGGGCCACGGGGCGCCTCCCTGATCGCCTGTAGATCTCCCGGGCTGGCCTCCCACA
AGGAGGGGAGACAATTGGGACCAACACTAGAATATCACCCTCCCTCTGGTCCTGAGGGAGAGGAATCCTCCTGGGTTCCAGATCC
TGTACCAGAGAGTGACTCTGAGGTTCCGCCCTGCTCTCTGACACAATTAAGGGATAAAATCTCTGAAGGAGTGACGGGAAGACGA
TCCCTCGAATACTGATGAGTGGTTCCCTTTGACACCGGCAGCAGCCTTGGGCCCGTGACTTTTCCTCTCAGGCCTTGTTCTCTGC
TTCACACTCAATGTGTGTGGGGGTCTGAGTCCAGCACTTCTGAGTCCCTCAGCCTCCACTCAGGTCAGGACCAGAAGTCGCTGTT
CCCTTCTCAGGGAATAGAAGATTATCCCAGGTGCCTGTGTCCAGGCTGGTGTCTGGGTTCTGTGCTCTCTTCCCCATCCCGGGTG
TCCTGTCCATTCTCAAGATGGCCACATGCGTGCTGGTGGAGTGTCCCATGACAGATGCAAAATGCCTGAATTTTCTGACTCTTCC
CGTCAGACCCCCCCAAGACACATATGACCCACCACCCCATCTCTGACCATGAGGCCACCCTGAGGTGCTGGGCCCTGGGCTTCTA
CCCTGCGGAGATCACACTGACCTGGCAGCGGGATGGGGAGGACCAGACCCAGGACACGGAGCTCGTGGAGACCAGGCCTGCAGGG
GATGGAACCTTCCAGAAGTGGGCGGCTGTGGTGGTGCCTTCTGGAGAGGAGCAGAGATACACCTGCCATGTGCAGCATGAGGGTC
TGCCCAAGCCCCTCACCCTGAGATGGGGTAAGGAGGGAGATGGGGGTGTCATGTCTCTTAGGGAAAGCAGGAGCCTCTCTGGAGA
CCTTTAGCAGGGTCAGGGCCCCTCACCTTCCCCTCTTTTCCCAGAGCTGTCTTCCCAGCCCACCATCCCCATCGTGGGCATCATT
GCTGGCCTGGTTCTCCTTGGAGCTGTGATCACTGGAGCTGTGGTCGCTGCCGTGATGTGGAGGAGGAAGAGCTCAGGTGGAGAAG
GGGTGAAGGGTGGGGTCTGAGATTTCTTGTCTCACTGAGGGTTCCAAGCCCCAGCTAGAAATGTGCCCTGTCTCATTACTGGGAA
GCACCGTCCACAATCATGGGCCTACCCAGTCTGGGCCCCGTGTGCCAGCACTTACTCTTTTGTAAAGCACCTGTTAAAATGAAGG
ACAGATTTATCACCTTGATTACGGCGGTGATGGGACCTGATCCCAGCAGTCACAAGTCACAGGGGAAGGTCCCTGAGGACAGACC
TCAGGAGGGCTATTGGTCCAGGACCCACACCTGCTTTCTTCATGTTTCCTGATCCCGCCCTGGGTCTGCAGTCACACATTTCTGG
AAACTTCTCTGGGGTCCAAGACTAGGAGGTTCCTCTAGGACCTTAAGGCCCTGGCTCCTTTCTGGTATCTCACAGGACATTTTCT
TCTCACAGATAGAAAAGGAGGGAGTTACACTCAGGCTGCAAGTAAGTATGAAGGAGGCTGATGCCTGAGGTCCTTGGGATATTGT
GTTTGGGAGCCCATGGGGGAGCTCACCCACCTCACAATTCCTCCTCTAGCCACATCTTCTGTGGGATCTGACCAGGTTCTGTTTT
TGTTCTACCCCAGGCAGTGACAGTGCCCAGGGCTCTGATGTGTCCCTCACAGCTTGTAAAGGTGAGAGCTTGGAGGACCTAATGT
GTGTTGGGTGTTGGGCGGAACAGTGGACACAGCTGTGCTATGGGGTTTCTTTGCATTGGATGTATTGAGCATGCGATGGGCTGTT
TAAGGTGTGACCCCTCACTGTGATGGATATGAATTTGTTCATGAATATTTTTTTCTATAGTGTGAGACAGCTGCCTTGTGTGGGA
CTGAG"}'
http://localhost:5000/api/v1/gfe

```

## Perl example

```perl

#!/usr/bin/env perl
=head1 NAME
 
 	seq2gfe.pl
	
=head1 SYNOPSIS
	
	Simple perl script for turning raw sequence data
	into GFE annotation. 
 
=cut
use strict;
use warnings;
use Getopt::Long;
use FindBin;
use lib "$FindBin::Bin/../lib";
use GFE;

our($s_locus,$s_seq,$s_url) = (undef,undef,undef);
&GetOptions('locus|l=s'     => \$s_locus,
			'seq|s=s'       => \$s_seq,
			'url|u=s'       => \$s_url
            );

my $o_gfe = GFE->new();

# Defaults to http://feature.nmdp-bioinformatics.org
$o_gfe->client(url => $s_url) if defined $s_url;

# Does alignment of sequence and submission of aligned
# sequence to the GFE service.
my $rh_gfe = $o_gfe->getGfe($s_locus,$s_seq);

# Print out GFE
print $$rh_gfe{gfe},"\n";

```

### Tools

```bash
./gfe-submission-fasta [--uri] [--fasta] [--verbose] [--help]
    -u/--uri
    -v/--verbose
    -h/--help

gfe-submission-fasta --fasta t/resources/A.test1.fasta -v > test1.gfe.csv

```


## Running

```bash
perl Makefile.PL
make test
make install
plackup -E deployment -s Starman --workers=10 -p 5050 -a bin/app.pl
```

### Required Software

 * Git, http://git.org
 * clustalo, http://www.clustal.org/omega
 * hap1.0, https://github.com/wwang-nmdp/HSA/tree/SeqAnn
 * perl 5.18 or later, http://perl.org

### Perl Modules

 * YAML 
 * Plack 
 * Plack::Handler::Starman 
 * Template 
 * JSON
 * Moose
 * Dancer
 * Getopt::Long 
 * LWP::UserAgent 
 * Test::More Dancer
 * Dancer::Plugin::Swagger

### Related Pages

 * [docker-ars](https://github.com/nmdp-bioinformatics/docker-ars)
 * [dockerhub](https://hub.docker.com/r/nmdpbioinformatics/docker-ars/)


