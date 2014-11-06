use Seeder::Finder;  
    my $finder = Seeder::Finder->new( 
    seed_width    => "6", 
    strand        => "revcom", 
    motif_width   => "12", 
    n_motif       => "10", 
    hd_index_file => "6.index", 
    seq_file      => "/home/yzolotarov/dehydrin_promoters/sequences/promoters/KS_prom.fas",
    bkgd_file     => "all_for_DHN.bkgd", 
    out_file      => "KS.finder", 
); 
$finder->find_motifs;
