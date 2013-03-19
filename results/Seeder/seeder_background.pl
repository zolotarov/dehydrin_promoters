use Seeder::Background; 
    my $background = Seeder::Background->new( 
    seed_width    => "6", 
    strand        => "revcom", 
    hd_index_file => "6.index", 
    seq_file      => "../../../sequences/promoters/monocots_oneline.fas", 
    out_file      => "monocots.bkgd", 
);
$background->get_background; 
