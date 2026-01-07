use strict;
use warnings;

use Bio::SeqIO;
use Bio::SeqIO::genbank;
use Bio::DB::Query::GenBank;
use Bio::DB::GenBank;
use Bio::Seq::RichSeq;
use Bio::Annotation::DBLink;
use Bio::Annotation::Reference;
use Bio::Annotation::Comment;
use Bio::Annotation::SimpleValue;

my $query = 'Prevotella[Title] 16S[Title]';   #replace Taxon


my $query_obj = Bio::DB::Query::GenBank->new(-db    => 'nucleotide', 
											-query => $query );

my $conteo = $query_obj->count;
print "$conteo SEQUENCES FOUND\n\n";

my $gb = Bio::DB::GenBank->new();



my $stream = $gb->get_Stream_by_query($query_obj);

#my $outseq= Bio::SeqIO->new(-file => '>$query.gbk', -format => 'genbank' );


my $output = "Sequences_found";

open (FILEF, ">$output\.fasta") or die; ### FASTA
open (FILEL, ">$output\.list") or die; ### Lista

print FILEL "###ID\tDESCRIPTION\tSEQUENCE LENGTH\n";



while (my $seq = $stream->next_seq) {
  
	my $seqId = $seq->id;
	my $seqDs = $seq->desc;
	my $seqSeq = $seq->seq;
	my $seqSeqLeng = length($seqSeq);
	my @dates = $seq->get_dates;
	
	
	
	my $outseq= Bio::SeqIO->new(-file => ">".$seqId.".gbk", -format => 'genbank' );
	$outseq->write_seq($seq);	

	

#	print FILEF "\>$seqId $seqDs\n$seqSeq\n";
#	print FILEL "$seqId\t$seqDs\t$seqSeqLeng\t@dates\n";
	
}

 #close FILEF;
 #close FILEL;
 