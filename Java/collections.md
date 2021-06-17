# Java Collections 

## ArrayList 
The **ArrayList** class is a resizable array, which can be found in the **java.util** package.

The difference between a built-in array and an **ArrayList** in Java, is that the size of an array cannot be modified (if you want to add or remove elements to/from an array, you have to create a new one). While elements can be added and removed from an ArrayList whenever you want. The syntax is also slightly different:

```
import java.util.ArrayList; // import the ArrayList class

ArrayList<String> cars = new ArrayList<String>(); // Create an ArrayList object

```
### ArrayList Method
  - addition 
    - add(item)
    - set(index, item)
  - Access 
    - get(index)
  - Remove 
    - remove(index)
    - clear()       // Whole ArrayList  
  - length 
    - size()

### ArrayList Iteration
  - for
  - for-each

```
  // ArrayList construction 
  ArrayList<String> cars = new ArrayList<String>();
    
    // Appending item 
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");

    // Sort Operation 
    Collections.sort(cars);  // Sort cars

    // Looping based on index     
    for (int i = 0; i < cars.size(); i++) {
      System.out.println(cars.get(i));
    }

    // Looping based on item 
    for (String i : cars) {
      System.out.println(i);
    }
```

## LinkedList 
The **LinkedList** class is almost identical to the ArrayList

### ArrayList vs. LinkedList
The **LinkedList** class is a collection which can contain many objects of the same type, just like the ArrayList.

The **LinkedList** class has all of the same methods as the **ArrayList** class because they both implement the List interface. This means that you can add items, change items, remove items and clear the list in the same way.

However, while the **ArrayList** class and the **LinkedList** class can be used in the same way, they are built very differently.

### How the ArrayList works
The **ArrayList** class has a regular array inside it. When an element is added, it is placed into the array. If the array is not big enough, a new, larger array is created to replace the old one and the old one is removed.

### How the LinkedList works
The **LinkedList** stores its items in "containers." The list has a link to the first container and each container has a link to the next container in the list. To add an element to the list, the element is placed into a new container and that container is linked to one of the other containers in the list.

### When To Use
It is best to use an **ArrayList** when:
- You want to access random items frequently
- You only need to add or remove elements at the end of the list

It is best to use a **LinkedList** when:

- You only use the list by looping through it instead of accessing random items
- You frequently need to add and remove items from the beginning, middle or end of the
list
### LinkedList Method
  - addition
    - addFirst()	Adds an item to the beginning of the list.	
    - addLast()	Add an item to the end of the list	
  - Remove
    - removeFirst()	Remove an item from the beginning of the list.	
    - removeLast()	Remove an item from the end of the list	
  - Extract 
    - getFirst()	Get the item at the beginning of the list	
    - getLast()	Get the item at the end of the list
  
## HashMap
A **HashMap** store items in "key/value" pairs, and you can access them by an index of another type (e.g. a String).

One object is used as a key (index) to another object (value). It can store different types: String keys and Integer values, or the same type, like: String keys and String values:

```
import java.util.HashMap; // import the HashMap class

HashMap<String, String> capitalCities = new HashMap<String, String>();

```
### HashMap Method
  - addition 
    - put(key, value)
  - Access 
    - get(key)
  - Remove 
    - remove(key)
    - clear()       // Whole HashMap  
  - length 
    - size()
  - Extract 
    - keySet()
    - values()

### HashMap Iteration
  - for
  - for-each

```
// Print keys and values
for (String i : capitalCities.keySet()) {
  System.out.println("key: " + i + " value: " + capitalCities.get(i));
}
```

## HashSet 
A HashSet is a collection of items where every item is unique, and it is found in the java.util package:
```
import java.util.HashSet; // Import the HashSet class

HashSet<String> cars = new HashSet<String>();
```
### HashSet Method
  - addition 
    - add(item)
  - Check  
    - contains(item)
  - Remove 
    - remove(key)
    - clear()       // Whole HashMap  
  - length 
    - size()
 
## 