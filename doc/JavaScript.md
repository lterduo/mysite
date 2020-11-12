# Array 对象

* https://www.runoob.com/jsref/jsref-obj-array.html

## forEach()返回值问题

* 使用forEach，你查询到以后的return，只是结束对status的遍历，forEach本身是不具备返回值的。所以你只能在forEach内部找到这个值，再交由name，然后再返回

## find()方法

* find() 方法返回通过测试（函数内判断）的数组的第一个元素的值。

~~~javascript
var status = [
  { id: '1', name: '11' },
  { id: '2', name: '22' },
  { id: '3', name: '33' },
];

function test1(id){
  const item = this.status.find(item => item.id == id)
  return item ? item.id : null
}

console.log('name: ', test1(2))
~~~

## map()

* map() 方法返回一个新数组，数组中的元素为原始数组元素调用函数处理后的值。