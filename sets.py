# Learning Sets
#var1 = {"monday", "tuesday", "wednesday"}
var1 = {"monday", "tuesday", "wednesday"}
#var1 = set((1, 2,1,2))

# Adding elements into a set
var1.add("thursday")


# Updating sets with other sequence
var1.update(["saturday", "sunday"])

# Removing elements from a set
var1.discard("sat")
print(var1)