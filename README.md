# Project 3

Superuser login
username: admin
password: password#1

Pinocchio's Order App Description
user must first register (handled by signup function) and then login (handled by login function)
to see the menu. User can add items from the menu (menu.html render) to their order and then checkout, which redirects them to a checkout page
(checkout.html rendered). In checkout, user can see status of their order, which can be changed by staff in the confirmed_final_order
function (rendered in confirmed_order.html), which then causes the order to marked as "done" for the user.

Models Description

Pizza_Toppings: pizza toppings
Pizza_Size: pizza sizes
Pizza_Type: pizza types
Platter: Dinner platters
Dinner_Platter size: Dinner platter sizes
Salad: salads
Pasta: pastas
Order: "holding" area for orders, which are deleted and moved to Confirmed Order when the "checkout" function is ran
Confirmed Order: items from Order are moved here when a user confirms their order; Boolean value "finished" marked as True when order
                    is completed by the staff.


Additional Commentary

My additional feature is a Confirmed Orders page/function that lets a staff member switch an order to finished (which removes the
order from that page and switches it to "Done" in the orderer's checkout page).

My special pizza order is a pizza with five random ingreidents.

There were two things I could not figure out, one small and one large. The small thing I could not figure out was adding a message
to my menu page to let the user know they can't enter more than three ingredients for their pizza (using a message
with HttpResponseRedirect) -- this feels like it should be straight forward and I tried to follow the Django documentation for it,
but I am clearly missing something subtle (I am not getting any errors when I try to put it in, so I am not sure where
to trace my error back from).

The large thing I could not figure out was "The Case of the Mysterious Disappearing Sub":

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

