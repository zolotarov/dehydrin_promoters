use Seeder::Index;  
    my $index = Seeder::Index->new( 
    seed_width => "8", 
    out_file   => "8.index", 
); 
$index->get_index; 
