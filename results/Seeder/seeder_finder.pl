use Seeder::Finder;  
    my $finder = Seeder::Finder->new( 
    seed_width    => "6", 
    strand        => "revcom", 
    motif_width   => "12", 
    n_motif       => "10", 
    hd_index_file => "../../../Seeder/6.index", 
    seq_file      => "/home/yzolotarov/dehydrin_promoters/coexpression/arath_KSdeh_NASCArrays.fas", 
    bkgd_file     => "arath.bkgd", 
    out_file      => "arath_KSdeh_NASCArrays.finder", 
); 
$finder->find_motifs;
