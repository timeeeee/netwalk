# netwalk
Netwalk generator and solver

Some things (like the server) can be more than one tile in size, so it will be awkward to put them in an array. Instead, make a bunch of objects that can rotate themselves, and link them together?
  Having a linking process after the objects are created would make it easy to add edge wrapping.
  In the end you have a list of objects rather than a grid.
  Solving recursively by guessing and checking can happen in any order!
    each tile needs to remember if it's been used yet.