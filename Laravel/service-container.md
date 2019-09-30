# Service Container under the hood
The Laravel service container is a powerful tool for managing class dependencies and performing dependency injection. Dependency injection is a fancy phrase that essentially means this: class dependencies are “injected” into the class via the constructor or, in some cases, “setter” methods.

Simply put, the service container is a container that holds classes you’d like to resolve(instantiate) programmatically later in your application.

We define how an object should be created in one point of the application (the binding) and every time we need to create a new instance, we just ask it to the service container, and it will create it for you, along with the required dependencies For example, instead of creating objects manually with the new keyword:

```
//everytime we need OurClass we should pass the dependency manually
$instance = new OurClass($dependency);
```
Instead, you can register a binding on the Service Container:

```
//add a binding for the class YourClass
App::bind( OurClass::class, function()
{
    //do some preliminary work: create the needed dependencies
    $dependency = new DepClass( config('some.value') );

    //create and return the object with his dependencies
    return new OurClass( $dependency );
});
```
and create an instance through the service container with:
```
//no need to create the OurClass dependencies, the SC will do that for us!
$instance = App::make( OurClass::class );
```
With Laravel automatic dependency injection, when an interface is required in some part of the app (i.e. in a controller's constructor), a concrete class is instantiated automatically by the Service Container. Changing the concrete class on the binding, will change the concrete objects instantiated through all your app:

```
//every time a UserRepositoryInterface is requested, create an EloquentUserRepository
App::bind( UserRepositoryInterface::class, EloquentUserRepository::class );

//from now on, create a TestUserRepository
App::bind( UserRepositoryInterface::class, TestUserRepository::class );
```
**Using the Service Container as a Registry**
You can create and store unique object instances on the container and get them back later: using the App::instance method to make the binding, and thus using the container as a Registry.
```
// Create an instance.
$kevin = new User('Kevin');


// Bind it to the service container.
App::instance('the-user', $kevin);


// ...somewhere and/or in another class...

// Get back the instance
$kevin = App::make('the-user');
```
As a final note, essentially the Service Container -is- the Application object: it extends the Container class, getting all the container's functionalities.
