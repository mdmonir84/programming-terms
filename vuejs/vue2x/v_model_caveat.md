# v-model caveat for object in components

v-model is nothing more than syntactical sugar for the following.

```
<input type="text" v-model="value">

equals to 

<input type="text" :value="value" @input="e => value = e.target.value">
```

- But if my value a is an object ```v-model="a"``` passes a reference to a to the child, and any changes the child makes to it affect the parent immediately (JavaScript object reference). 
- This defeats the intended abstraction and makes ```this.$emit( 'input', ... )``` redundant window dressing.

So the solution it seems is for the child to make a deep clone of the value prop into a local_val data attribute whenever it changes. Unfortunately this has to be done when component is mounted too, which adds boilerplate. (edit: just found out you can clone this.value right in the data function, so that is a bit cleaner.)

Now when we emit the input event, we attach our cloned local_val object which then becomes the value of value, which then triggers the watch on value and causes our local_val to be replaced by a deep clone of itself. So far that's inefficient but not inherently problematic.

The real problem is now we can't use a watch expression on local_val to know if it's been changed (like say in a sub-component) to trigger this.$emit because you get an infinite loop!

In my case I really wanted to use watch on local_val because it's so much less work than attaching listeners to each of my sub-components (what's the point of v-model if I also have to attach listeners everywhere?) So to prevent infinite loops I have to deep-compare this.value and this.local_val before emitting an input. More boilerplate, more inefficiencies.

So in the end my input custom components each have the following boilerplate:

```
module.exports = {
	props: ['value'],
	data: function() {
		return {
			local_val: clone( this.value );
		}
	},
	watch: {
		value: {
			handler: function() {
				this.local_val = clone( this.value );
			},
			deep: true
		},
		local_val: {
			handler: function() {
				if( !deepEqual(this.local_val, this.value, {strict:true}) ) {
					this.$emit( 'input', this.local_val );
				}
			},
			deep: true
		}
	},
```
