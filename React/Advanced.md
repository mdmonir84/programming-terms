
* component.render vs ReactDOM.render
React creates a virtual DOM before adding (mounting) it into the actual browser DOM, before it is displayed. 
One of the two methods does the first action only, and the other does both.

component.render only creates the virtual DOM. It does not add it to the actual browser DOM.

ReactDOM.render does both. It creates (or updates) the virtual DOM, and then additionally adds it to the actual browser DOM.
