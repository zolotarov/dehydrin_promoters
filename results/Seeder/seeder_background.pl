use Seeder::Background; 
    my $background = Seeder::Background->new( 
    seed_width    => "6", 
    strand        => "revcom", 
    hd_index_file => "../../../Seeder/6.index", 
    seq_file      => "/home/yzolotarov/sequences/promoters/arath_prom_1K_uniq.fas", 
    out_file      => "arath.bkgd", 
);
$background->get_background; 
