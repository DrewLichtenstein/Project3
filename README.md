# Project 3

The Case of the Mysterious Disappearing Sub:

I've done something... wrong. When I originally made my Sub Class, I also made a Sub_Size and Sub_Add_On class since I thought that
was how I wanted my table to work; as I started working, I realized having to dynamically define the subs based on their size would
be too tedious (Unlike pizzas, subs are not consistently the same price across the types, so I thought it would be
better to define "Large Italian" and "Small Italian" as different things than "Italian" with small and large options).

So, I went to delete the Sub_Size and Sub_Add_On classes, but then my Sub Class wouldn't work in Admin view anymore because
it said I was missing the necewssary Add_On class (this was after I removed those fields and re-migrated... several times...). So, I figured,
OK, whatever, let's delete Sub and make a new Class called Sandwich. But, as I have found out, whenever I make *any* new class
and migrate, I am getting thrown a "no such table: orders_sub_sandwich" even though such a table
clearly does exists and can be seen in my admin view. I've spent nearly two hours banging my head against this problem and
while I could just start completely fresh, I've chosen not to since I had implemented most feature up to this point...

I've left the current Sub_Sandwich class in there so you can see where I am stuck; additionally, if you are so curious, my GitHub
commit from July 28 (https://github.com/DrewLichtenstein/Project3) has the original, non-functioning Sub class.

I'd love to know what happened and why I am effectively "locked out" from making new tables! Thanks!

username: admin
password: password#1