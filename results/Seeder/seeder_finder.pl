use Seeder::Finder;  
    my $finder = Seeder::Finder->new( 
    seed_width    => "6", 
    strand        => "revcom", 
    motif_width   => "12", 
    n_motif       => "10", 
    hd_index_file => "../../../Seeder/6.index", 
    seq_file      => "/home/yzolotarov/dehydrin_promoters/sequences/promoters/KS_with_oxytropis.fas", 
    bkgd_file     => "used_plants.bkgd", 
    out_file      => "KS_with_oxytropis.finder", 
); 
$finder->find_motifs;
