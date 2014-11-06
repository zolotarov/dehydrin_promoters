use Seeder::Background; 
    my $background = Seeder::Background->new( 
    seed_width    => "6", 
    strand        => "revcomp", 
    hd_index_file => "../../../Seeder/6.index", 
    seq_file      => "/home/yzolotarov/Public/sequences/promoters/arath_prom_1K_uniq.fas", 
    out_file      => "arath_revcomp.bkgd", 
);
$background->get_background; 
