sqlite3 dehydrins.db < KS_query.sql| sed 's/\(^.*|.*$\)/>\1/'| sed 's/|/\n/'

's/\(^.*|.*$\)/>\1/' finds a line with '|' and places a '>' in from of that line

Explanation:

(      # Start a capture group
^      # Matches the start of the line 
.*     # Matches anything 
myvar  # Matches the variable, | in this case
.*     # Matches anything
$      # Matches the end of the line
)      # End capture group

So this looks at the whole line and if myvar is found the results in stored in the first capture group, referred to a \1. So we replace the whole line \1 with the whole line preceded by 2 forward slashes //\1 of course the forwardslashes need escaping as not to confused sed so \/\/\1 also note that brackets need escaping unless you use the extended regex option of sed. 
