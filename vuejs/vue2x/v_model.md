# Basics of v-model

Of course you know v-model, the attribute which makes most of your input elements working. But did you know that you can use v-model as an interface for own components, too?

## For a better understanding let's have a look at some basics.

```
<input type="text" v-model="value">
v-model is nothing more than syntactical sugar for the following.

<input type="text" :value="value" @input="e => value = e.target.value">
```

- First we have the ```:value``` binding. It supplies the value of the input field. 
- Second there is the ```@input``` event. As soon as there is an input event fired, we update the model's data property value with the current value of the input element. 
- You also can use the abbreviation: ```@input="value = $event.target.value".```

## Wrapping an input field in a custom component

```
# Custom component called

<template>
  <CreateCustomer v-model="name"></CreateCustomer>
</template>
<script>
import CreateCustomer from './CreateCustomer'   

export default {
  components: { CreateCustomer },
  data() {
    return {
      name: 'John Doe',
    }
  },
}
</script>


# CreateCustomer.vue component which is nothing more than a wrapped input element.

<template>
  <div>
    <label>Name</label>
    <input type="text" :value="value" @input="$emit('input', $event.target.value)">
  </div>
</template>

<script>
export default {
  props: ['value'],
}
</script>

```
We bind the value that we get from the parent component to the text input and for @input we emit an input event with the field's current value to the parent. The next snippet shows the usage of the component.

## Using an object with v-model

- As soon as we add more input elements and want to use an object as value for v-model, things get a bit more complicated.

- Basically every data update of the component has to $emit a completely new instance of the object which then replaces the object instance stored in the parent's data. Otherwise you will get pretty strange and hard to debug behavior (e.g. watchers are not working properly) because objects are passed by reference in JavaScipt.

- At first glance this sounds very complicated but actually it isn't. You have to create a (deep) clone of the object, change values only on the clone and $emit that object.

Let's extend our CreateCustomer component with a second input, a select for the contact type.

```
# Custom component called 
<CreateCustomer v-model="{ name: 'John Doe', type: 'Person' }"></CreateCustomer>

# Custom component details 
<template>
  <div>
    <div>
      <label>Name</label>
      <input type="text" :value="value.name" @input="update('name', $event.target.value)">
    </div>
    <div>
      <label>Type</label>
      <select :value="value.type" @input="update('type', $event.target.value)">
        <option value="Person">Person</option>
        <option value="Company">Company</option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  props: ['value'],
  methods: {
    update(key, value) {
      this.$emit('input', { ...this.value, [key]: value })
    },
  },
}
</script>
```

Now that we have two fields we use an object as argument for v-model for the first time.

- For the :value bindings just use the object's properties. 
- For the @input I created a method which emits the input event with a shallow clone of the object and sets the new value for the given key.
- Remember you can use object destructuring for shallow cloning of objects since ES6.

## Using v-model with null

Maybe there is the case where we default the v-model value with null in our parent component because we don't know if our CreateCustomer form is actually used. If we pass null we get an error because we can't access object properties on null. In addition the consumer shouldn't know that the component only works if at least an empty object is passed to v-model.

Second, we need a default value for type. Otherwise the select shows an invalid empty option at the top.

So let's refactor our component again and add a computed property local which returns the value if there is one, otherwise an object with appropriate defaults.

```
<template>
  <div>
    <div>
      <label>Name</label>
      <input type="text" :value="local.name" @input="update('name', $event.target.value)">
    </div>
    <div>
      <label>Type</label>
      <select :value="local.type" @input="update('type', $event.target.value)">
        <option value="Person">Person</option>
        <option value="Company">Company</option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  props: ['value'],
  computed: {
    local() {
      return this.value ? this.value : { type: 'Person' }
    },
  },
  methods: {
    update(key, value) {
      this.$emit('input', { ...this.local, [key]: value })
    },
  },
}
</script>
```

Be aware that we only use this.value in our computed property local. Everywhere else we use this.local instead of this.value. So if we're getting a null value, we're working with our defaults and thus prevent weird errors.

## Using a nested object with v-model

Let's take it a step further. Suppose we have a data model like the following for our CreateCustomer component.

```
{
  name: 'John Doe',
  type: 'Person',
  address: {
    street: 'Example Street 42',
    zip: '12345',
    city: 'Example City'
  }
}
```
We added a nested object address. Basically there are two options to extend our component:

- Create a custom component CustomerAddress and use the patterns shown above. Then there would be one responsible component per level of nesting in the data model (which is a good recommendation anyway).
- Embed it into our component.
- We take the second, more complex approach so I can give you deeper insight into using nested objects with v-model.

To keep things simple, I removed some fields and only add a new input for address.street.

```
<template>
  <div>
    <div>
      <label>Name</label>
      <input type="text" :value="local.name" @input="update('name', $event.target.value)">
    </div>
    <!-- ... -->
    <div>
      <label>Street</label>
      <input type="text" :value="local.address.street" @input="update('address.street', $event.target.value)">
    </div>
    <!-- inputs for zip and city work the same way -->
  </div>
</template>

<script>
import { cloneDeep, tap, set } from 'lodash'

export default {
  props: ['value'],
  computed: {
    local() {
      return this.value ? this.value : { type: 'Person', address: {} }
    },
  },
  methods: {
    update(key, value) {
      this.$emit('input', tap(cloneDeep(this.local), v => set(v, key, value)))
    },
  },
}
</script>
```

We're dealing with a nested object, so we bind local.address.street as our input's value. Remember to add address: {} to the local computed property to prevent null pointers.

Since there is no native JavaScript function for deep cloning an object I've imported some functions from Lodash.

cloneDeep(value): Creates a deep clone of the value.
tap(value, callback): Returns value after passing it to callback. Used to create a functional expressive one-liner function ;-)
set(object, path, value): Sets a nested value on an object, specified by a path in dot notation, e.g. set({}, 'address.street', 'Example Street 42') yields { address: { street: 'Example Street 42' } }.
The update method accepts a property path as key, creates a deep clone of our local computed value and sets the new value at the right property path. Setting nested values becomes as simple as @input="update('address.street', $event.target.value)".

## Working with nested arrays
Let's consider we want to store a list of contact items for every customer with the option to add and delete them.

```
{
  name: 'John Doe',
  type: 'Person',
  address: {
    street: 'Example Street 42',
    zip: '12345',
    city: 'Example City'
  },
  contacts: [
    { type: 'Email', value: 'john@example.com' },
    { type: 'Phone' value: '+1234567890' }
  ]
}
```
So we extend our component for a last time.

```
<template>
  <div>
    <!-- ... -->
    <div>
      <div>
        <label>Type</label>
        <select v-model="newContactType">
          <option value="Phone">Phone</option>
          <option value="Email">Email</option>
        </select>
      </div>
      <div>
        <label>Value</label>
        <input type="text" v-model="newContactValue">
      </div>
      <button type="button" @click="addContact">Add</button>
    </div>
    <div v-for="(contact, i) in local.contacts">
      {{ contact.type }} {{ contact.value }}
      <button type="button" @click="removeContact(i)">Remove</button>
    </div>
  </div>
</template>

<script>
import { cloneDeep, tap, set } from 'lodash'

export default {
  props: ['value'],
  data() {
    return {
      newContactType: 'Email',
      newContactValue: null,
    }
  },
  computed: {
    local() {
      return this.value ? this.value : { type: 'Person', address: {}, contacts: [] }
    },
  },
  methods: {
    // ...
    addContact() {
      this.$emit('input', tap(cloneDeep(this.customer), v => v.contacts.push({ 
        type: this.newContactType,
        value: this.newContactValue,
      })))
    },
    removeContact(i) {
      this.$emit('input', tap(cloneDeep(this.customer), v => v.contacts.splice(i, 1)))
    },
  },
}
</script>
```

For the logic needed to add a new contact item, v-model is used directly because it's only about local state in our component that shouldn't be propagated to the parent. Remember to add contacts: [] to the local computed property to use an empty array as default. Only if the add or delete button is clicked, a new input event is emitted with a deep clone of the object including the array's changes.

## $emit initial state from the created hook
Of course you can use the update method in the created hook, too. Use it to set component's defaults at its instantiation and propagate them to the parent instantly. Be aware that you should only use one update or $emit and set the initial state at once to prevent unexpected executions of watchers and timing issues.

```
<script>
export default {
  created() {
    this.$emit('input', tap(cloneDeep(this.local), v => {
      v.type = 'Company'
      v.address.city = 'Example City'
      v.contacts.push({ type: 'Email' })
    }))
  },
}
</script>
```

> Ref https://simonkollross.de/posts/vuejs-using-v-model-with-objects-for-custom-components

