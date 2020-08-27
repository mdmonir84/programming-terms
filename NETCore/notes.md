# .NET/C# Basic 


## .NET Basic 


## C# Bassic 

### virtual vs abstract method 

Virtual methods have an implementation and provide the derived classes with the option of overriding it. 

Abstract methods do not provide an implementation and force the derived classes to override the method.

So, abstract methods have no actual code in them, and subclasses HAVE TO override the method. Virtual methods can have code, which is usually a default implementation of something, and any subclasses CAN override the method using the override modifier and provide a custom implementation.

```
public abstract class E
{
    public abstract void AbstractMethod(int i);

    public virtual void VirtualMethod(int i)
    {
        // Default implementation which can be overridden by subclasses.
    }
}

public class D : E
{
    public override void AbstractMethod(int i)
    {
        // You HAVE to override this method
    }
    public override void VirtualMethod(int i)
    {
        // You are allowed to override this method.
    }
}

```

First of all you should know the difference between a virtual and abstract method.

- Abstract Method
  - Abstract Method resides in abstract class and it has no body
  - Abstract Method must be overridden in non-abstract child class.
  - If an abstract method is defined in a class, then the class should declare as an abstract class.
  - An abstract method should contain only method definition, should not Contain the method body/implementation.
  - An abstract method must be over ride in the derived class.
- Virtual Method
  - Virtual Method can reside in abstract and non-abstract class.
  - It is not necessary to override virtual method in derived but it can be.
  - Virtual method must have body ....can be overridden by "override keyword".....
  - Virtual methods can be over ride in the derived class but not mandatory.
  - Virtual methods must have the method body/implementation along with the definition.

```
Example:

public abstract class baseclass
{
    public abstract decimal getarea(decimal Radius);

    public virtual decimal interestpermonth(decimal amount)

    {
        return amount*12/100;
    }
    public virtual decimal totalamount(decimal Amount,decimal principleAmount)
    {
        return Amount + principleAmount;
    }

}

public class derivedclass:baseclass
{
    public override decimal getarea(decimal Radius)
    {
        return 2 * (22 / 7) * Radius;
    }
    public override decimal interestpermonth(decimal amount)
    {
        return amount * 14 / 100;
    }

}

```

### Base 

The base keyword is used to access members of the base class from within a derived class:

- Call a method on the base class that has been overridden by another method.

-  Specify which base-class constructor should be called when creating instances of the derived class.

A base class access is permitted only in a constructor, an instance method, or an instance property accessor.

It is an error to use the base keyword from within a static method.

The base class that is accessed is the base class specified in the class declaration. For example, if you specify class ClassB : ClassA, the members of ClassA are accessed from ClassB, regardless of the base class of ClassA.


Example

In this example, both the base class, Person, and the derived class, Employee, have a method named Getinfo. By using the base keyword, it is possible to call the Getinfo method on the base class, from within the derived class.

```
public class Person
{
    protected string ssn = "444-55-6666";
    protected string name = "John L. Malgraine";

    public virtual void GetInfo()
    {
        Console.WriteLine("Name: {0}", name);
        Console.WriteLine("SSN: {0}", ssn);
    }
}
class Employee : Person
{
    public string id = "ABC567EFG";
    public override void GetInfo()
    {
        // Calling the base class GetInfo method:
        base.GetInfo();
        Console.WriteLine("Employee ID: {0}", id);
    }
}

class TestClass
{
    static void Main()
    {
        Employee E = new Employee();
        E.GetInfo();
    }
}
/*
Output
Name: John L. Malgraine
SSN: 444-55-6666
Employee ID: ABC567EFG
*/
```

Example

This example shows how to specify the base-class constructor called when creating instances of a derived class.

```
public class BaseClass
{
    int num;

    public BaseClass()
    {
        Console.WriteLine("in BaseClass()");
    }

    public BaseClass(int i)
    {
        num = i;
        Console.WriteLine("in BaseClass(int i)");
    }

    public int GetNum()
    {
        return num;
    }
}

public class DerivedClass : BaseClass
{
    // This constructor will call BaseClass.BaseClass()
    public DerivedClass() : base()
    {
    }

    // This constructor will call BaseClass.BaseClass(int i)
    public DerivedClass(int i) : base(i)
    {
    }

    static void Main()
    {
        DerivedClass md = new DerivedClass();
        DerivedClass md1 = new DerivedClass(1);
    }
}
/*
Output:
in BaseClass()
in BaseClass(int i)
*/

```

## Extension Method

- An extension method is one that is used to extend the functionality of existing types by adding methods . 
- We don't need to create subclasses of existing classes or recompile or modify your existing classes to work with extension methods. 
- Extension methods improve the readability of your code while at the same time allowing you to extend functionality of existing types.


- The common extension methods in .Net include the LINQ standard query operators that adds additional query capabilities to the `System.Collections.IEnumerable` and `System.Collections.Generic.IEnumerable<T>` types. 
- Note that you can take advantage of extension methods to extend a class or an interface but you cannot override their methods. 


```
Examaple-01
------------------------
// Building extension method of string class 
public static class StringExtensions
{
    public static bool IsNumeric(this string str)
    {
        double output;
        return double.TryParse(str, out output);
    }

}

// Usage of above extension method 
static void Main(string[] args)
    {
        string str = "20";
        if (str.IsNumeric())
            Console.WriteLine("The string object contains numeric value.");
        Console.Read();
    }


Examaple-02
--------------------
// Building extension method of integer class 
public static class IntegerExtensions
{
    public static bool IsOdd(this int i)
    {
        return ((i % 2) != 0);
    }
}

// Usage of above extension method 
static void Main(string[] args)
{
    int n = 25;
    if(n.IsOdd())
    Console.WriteLine("The value of the integer is odd.");
}

```