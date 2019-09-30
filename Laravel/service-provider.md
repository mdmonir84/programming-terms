# Service Provider under the hood

Service providers are the central place of all Laravel application bootstrapping. our own application, as well as all of Laravel's core services are bootstrapped via service providers.


Service containers allow us to define bindings and inject dependencies, the service provider is where the action takes place. If you open the config/app.php file included with Laravel, you will see a  **providers array**. These are all of the service provider classes that will be loaded for our application. Of course, many of these are “deferred” providers, meaning they will not be loaded on every request, but only when the services they provide are actually needed.

In simple terms, a Service Provider is used to register classes into the service container.

## Writing Service Providers

All service providers extend the **Illuminate/Support/ServiceProvider** class. Most service providers contain a register and a boot method. Within the register method. You should only blind things into the service container. You should never attempt to register any event listeners, routes, or any other piece of functionality within the register method.

The Artisan CLI can generate a new provider through the ***make::provider*** command.

> php artisan make:provider RiakServiceProvider

### The Register Method

Within the register method, you should only blind thing into the service container. You should never attempt to register any event listeners, routes, or any other piece of functionality within the register method. Otherwise, you may accidentally use a service that is provided by a service provider which has not loaded yet. Let's look at this code sample

```
<?php
namespace App\Providers;
use Riak\Connection;
use Illuminate\Support\ServiceProvider;

class RiakServiceProvider extends ServiceProvider
{
    public function register()
    {
        $this->app->singleton(Connection::class, function ($app)
        {
            return new Connection(config('riak'));
        });
    }
}
```
This service provider only defines a register method, and uses that method to define an implementation of Riak//Connection in the service container.

### The Boot Method
So, what if we need to register a view composer within our service provider? This should be done within the boot method. This method called after all other service providers have been registered.

**Let's look at a simple example.**
```
<?php
namespace App\Providers;
use Illuminate\Support\ServiceProvider;
class ComposerServiceProvider extends ServiceProvider
{
    public function boot()
    {
        view()->composer('view', function () {
            //
        });
    }
}
```
### Boot Method Dependency Injection
You may type-hint dependencies for your service provider's boot method. The service container will automatically inject any dependencies you need.

**Let's look at a simple example.**
```
use Illuminate\Contracts\Routing\ResponseFactory;
public function boot(ResponseFactory $response)
{
    $response->macro('caps', function ($value) {
        //
    });
}
```

## Registering Providers
All service providers are registered in the config/app.php configuration file. This file contains a providers array where you can list the class names of your service providers. By default, a set of Laravel core service providers are listed in this array. These providers bootstrap the core Laravel components, such as the mailer, queue, cache, and others.

To register your provider, simply add it to the array.
```
'providers' => [
 // Other Service Providers
 App\Providers\ComposerServiceProvider::class,
],
```
## Deferred Providers
If your provider is only registering bindings in the service container, you may choose to defer its registration until one of the registered bindings is actually needed. Deferring the loading of such a provider will improve the performance of your application since it is not loaded from the file system on every request. Laravel compiles and stores a list of all of the services supplied by deferred service providers, along with the name of its service provider class. Then, only when you attempt to resolve one of these services does Laravel load the service provider.

To defer the loading of a provider, set the defer property to true and define a provides method. The provides method should return the service container bindings registered by the provider.

Let's look at a simple example.
```
<?php

namespace App\Providers;

use Riak\Connection;
use Illuminate\Support\ServiceProvider;
class RiakServiceProvider extends ServiceProvider
{
    protected $defer = true;
    public function register()
    {
        $this->app->singleton(Connection::class, function ($app) {
            return new Connection($app['config']['riak']);
        });
    }
    public function provides()
    {
        return [Connection::class];
    }
}
```
