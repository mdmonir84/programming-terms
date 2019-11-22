# Service Container

A modern PHP application is full of objects. One object may facilitate the delivery of email messages while another may allow we to persist information into a database. In wer application, we may create an object that manages wer product inventory, or another object that processes data from a third-party API. The point is that a modern application does many things and is organized into many objects that handle each task.

This chapter is about a special PHP object in Symfony2 that helps us instantiate, organize and retrieve the many objects of our application.

This object, called a **service container** will help us in the following aspects
  - standardize &
  - centralize the way objects are constructed in application.
  - the container makes life easier as it is super fast, and
  - emphasizes an architecture that promotes reusable and decoupled code.

Since all core Symfony2 classes use the container, we'll learn how to extend, configure and use any object in Symfony2. In large part, the service container is the biggest contributor to the speed and extensibility of Symfony2.


## What is Service

Put simply, a Service is any PHP object that performs some sort of "global" task. It's a purposefully-generic name used in computer science to describe an object that's created for a specific purpose (e.g. delivering emails). Each service is used throughout our application whenever we need the specific functionality it provides. We don't have to do anything special to make a service: simply write a PHP class with some code that accomplishes a specific task. Congratulations, we've just created a service!

So what's the big deal then? The advantage of thinking about "services" is that we begin to think about separating each piece of functionality in our application into a series of services. Since each service does just one job, we can easily access each service and use its functionality wherever we need it. Each service can also be more easily tested and configured since it's separated from the other functionality in our application. This idea is called service-oriented architecture and is not unique to Symfony2 or even PHP. Structuring our application around a set of independent service classes is a well-known and trusted object-oriented best-practice. These skills are key to being a good developer in almost any language.

> As a rule, a PHP object is a service if it is used globally in your application. A single Mailer service is used globally to send email messages whereas the many Message objects that it delivers are not services. Similarly, a Product object is not a service, but an object that persists Product objects to a database is a service.

## What is a Service Container?

A Service Container (or dependency injection container) is simply a PHP object that manages the instantiation of services (i.e. objects).

For example, suppose you have a simple PHP class that delivers email messages. Without a service container, you must manually create the object whenever you need it:

```
use Acme\HelloBundle\Mailer;

$mailer = new Mailer('sendmail');
$mailer->send('ryan@foobar.net', ...);
```
This is easy enough. The imaginary Mailer class allows you to configure the method used to deliver the email messages (e.g. sendmail, smtp, etc). But what if you wanted to use the mailer service somewhere else? You certainly don't want to repeat the mailer configuration every time you need to use the Mailer object. What if you needed to change the transport from sendmail to smtp everywhere in the application? You'd need to hunt down every place you create a Mailer service and change it.

## Creating/Configuring Services in the Container¶

A better answer is to let the service container create the Mailer object for you. In order for this to work, you must teach the container how to create the Mailer service. This is done via configuration, which can be specified in YAML, XML or PHP:

```
#YAML
# app/config/config.yml
services:
  my_mailer:
      class:        Acme\HelloBundle\Mailer
      arguments:    [sendmail]

#XML
<!-- app/config/config.xml -->
<services>
    <service id="my_mailer" class="Acme\HelloBundle\Mailer">
        <argument>sendmail</argument>
    </service>
</services>

#PHP
// app/config/config.php
use Symfony\Component\DependencyInjection\Definition;

$container->setDefinition('my_mailer', new Definition(
    'Acme\HelloBundle\Mailer',
    array('sendmail')
));

```
>>When Symfony2 initializes, it builds the service container using the application configuration (app/config/config.yml by default). The exact file that's loaded is dictated by the AppKernel::registerContainerConfiguration() method, which loads an environment-specific configuration file (e.g. config_dev.yml for the dev environment or config_prod.yml for prod).

An instance of the ```Acme\HelloBundle\Mailer``` object is now available via the service container. The container is available in any traditional Symfony2 controller where you can access the services of the container via the get() shortcut method:

```
class HelloController extends Controller
{
    // ...

    public function sendEmailAction()
    {
        // ...
        $mailer = $this->get('my_mailer');
        $mailer->send('ryan@foobar.net', ...);
    }
}

```

When you ask for the my_mailer service from the container, the container constructs the object and returns it. This is another major advantage of using the service container. Namely, a service is never constructed until it's needed. If you define a service and never use it on a request, the service is never created. This saves memory and increases the speed of your application. This also means that there's very little or no performance hit for defining lots of services. Services that are never used are never constructed.

As an added bonus, the Mailer service is only created once and the same instance is returned each time you ask for the service. This is almost always the behavior you'll need (it's more flexible and powerful), but you'll learn later how you can configure a service that has multiple instances in the "How to work with Scopes" cookbook article.


> Ref:
  1. https://symfony.com/doc/2.1/book/service_container.html
  2. https://symfony.com/doc/2.1/components/dependency_injection/introduction.html
