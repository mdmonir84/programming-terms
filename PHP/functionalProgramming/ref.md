# PHP method chaining

## regular class:

```
class a_class
{

    public function method_a()
    {
        echo 'method a';
    }

    public function method_b()
    {
        echo ' - method b';
    }

}
```
You'd call those like this:

> $class = new a_class();

> $class->method_a();
>
> $class->method_b();

Which would echo 'method a - method b'.

## Now to chain them, you'd return the object in the methods:

```
class a_class
{

    public function method_a()
    {
        echo 'method a';
        return $this;
    }

    public function method_b()
    {
        echo ' - method b';
        return $this;
    }

}
```
You'd call those like this:

> $class = new a_class();

> $class->method_a()->method_b();

Which would also echo 'method a - method b'.


## Basic Prototype

Coniser an object:

> $obj = new ObjectWithChainableMethods();

Call a method that effectively does a return ```$this```; at the end:

> $obj->doSomething();

Since it returns the same object, or rather, a reference to the same object, you can continue calling methods of the same class off the return value, like so:

> $obj->doSomething()->doSomethingElse();

That's it, really. Two important things:

- As you note, it's PHP 5 only. It won't work properly in PHP 4 because it returns objects by value and that means you're calling methods on different copies of an object, which would break your code.

- Again, you need to return the object in your chainable methods:

```
public function doSomething() {
    // Do stuff
    return $this;
}

public function doSomethingElse() {
    // Do more stuff
    return $this;
}
```
