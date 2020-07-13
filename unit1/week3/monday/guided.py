UPER = {'U': 'Understand', 'P': 'Plan', 'E': 'Execute', 'R': 'Reflect'}

# Binary Search Algorithm
BST = "When data has some structure, we can search throught it very efficiently"
search: "O(log(n))"
insert: "O(log(n))"
arrayinsert: "O(1)"
arraysearch: "O(n)"

Binary_search_algorithms = ["gets us teh same benefits of BSTs for arrays", "Binary serch requires the array to be sorted"]

# search(24)
sorted_array=[3,8,9,15,18,21,24,26,31]
def search_array(array, target):
    for i, v in enumerate(array):
        if v == target:
            print(True, "at index: ", i)

search_array(sorted_array, 33)
search_array(sorted_array, 21)
        
'''1) Figure out teh midpoint index
    - if theres an even number of elements, round down
2) Compare the target against the midpoint elements
    - if target < midpoint element, then its on the left side
    - if target > midpoint element, then its on the right side
3) Each Iteration were cutting the search space in half.'''

#Recursive binary search

'''1) what are the base cases?
    - we find our element; it returns the index
    - we get down to 1 element and its not what were looking for
2) How do we get closer to a base case?
    - On ech step, we cut the serch space in half, eliminating the half of the search space that the element cant be in    
'''

unsorted = [1,34,67,2,3,77,3,2,222,65,68]
print(sorted(unsorted))

# Sorting == Sorting Output

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    def __str__(self):
        return f"{self.title}"

def insertion_sort_by_book_title(arr_of_books):
    # iterate through the entire array
    # we can skip the first array element since there is nothing to compare it to
    # do we want to iterate over the books themselves or indicies?
    # we do need to have access to the book before the current book
    # we need access to each idex in order to facilitate this
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        # book_index will start at i
        # but we need to update it as we swap
        book_index = i   
        # prev_book = arr_of_books[i - 1]
        # compare curr_book with the previous book
        # what do we compare by?
        while book_index > 0 and curr_book.title < arr_of_books[book_index -1].title:
            # swap them
            arr_of_books[book_index], arr_of_books[book_index - 1] = arr_of_books[book_index -1], arr_of_books[book_index]
            # we need to keep track of our current books changing index
            book_index -= 1
    return

books = [
    Book("Harry Potter and the Sorcerer's Stone", "JK Rowling", "Children's Fantasy" ),
    Book("A Game of Thrones", "George RR Mrtin", "Adult Fantasy"),
    Book("Show Your Work", "Austin Kleon", "Self Help"),
    Book("The Lord of the Rings: The Fellowship of the Ring", "JRR Tolkien", "High Fantasy"),
    Book("Clean Code", "Robert J Martin", "Programming"),
    Book("The Rust Programming Language", "Steve Klabnik and Carol Nichols", "Programming"),
    Book("The Way of Kings", "Brandon Sanderson", "High Fantasy")
]

insertion_sort_by_book_title(books)
for book in books:
    print(book)