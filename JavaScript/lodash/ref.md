# lodash function development


## groupBy

```
function groupBy(array, callback) {
  return array.reduce(function(store, item) {
    var key = callback(item);
    var value = store[key] || [];
    store[key] = value.concat([item]);
    return store;
  }, {})
}

```

## chunk
Creates an array of elements split into groups the length of size. If array can't be split evenly, the final chunk will be the remaining elements

```
const chunk = (arr, chunkSize = 1, cache = []) => {
  const tmp = [...arr]
  if (chunkSize <= 0) return cache
  while (tmp.length) cache.push(tmp.splice(0, chunkSize))
  return cache
}
```


## Uniq
Creates a duplicate-free version of an array, in which only the first occurrence of each element is kept. The order of result values is determined by the order they occur in the array.

```
[...new Set([2, 1, 2])]
// => [2, 1]
```

## Flatten
Flattens array a single level deep.

```
[1, [2, [3, [4]], 5]].reduce((a, b) => a.concat(b), [])
// => [1, 2, [3, [4]], 5]
```
## FlattenDeep
Recursively flattens array.

```
const flattenDeep = arr =>
  Array.isArray(arr)
    ? arr.reduce((a, b) => [...flattenDeep(a), ...flattenDeep(b)], [])
    : [arr]

flattenDeep([1, [[2], [3, [4]], 5]])
// => [1, 2, 3, 4, 5]
```

- https://youmightnotneed.com/lodash/
