"""
regex

regular expressions

regular searching: determine if a substring
exists in a string

advanced searching: find words that begin
with a letter; find only numbers 0-9

position
^   search at start of string
$   search at end of string
    examples: "^hello" => hello at start of string
              "goodbye$"=> goodbye at end of string

grouping
()  =>  group this item
[]  => all characters in brackets
[a-z] => all characters from a to z
[0-9] all numbers
[^a-z]=> all character EXCEPT a-z
[^0-9] all non-numerical character

shortcuts
\s      whitespace      [\s\t\r\n ]
\S      non-whitespace  [^\s\t\r\n ]
\d      digit           [0-9]
\D      non-digit       [^0-9]
\w     word             [a-zA-Z0-9_]
\W      non-word        [^a-zA-Z0-9_]

Character Matching
.       match any character

Repetitive Character
?   match zero or 1 time aka optional
+   match one or many times
*   match zero or many times
{N} eg {3} or {4}   match EXACTLY N times
{N,M}   match between N and M times
{N,} match at least N times

|       either or
cool|beans


[a-zA-Z0-9\.]+@[a-zA-Z\d]+\.[a-z]{2,}


\d{10,}|\(?\d{3}\)?(-|\s){1}\d{3}(-|\s){1}\d{4}

"""
