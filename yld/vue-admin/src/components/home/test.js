const { test } = require("shelljs");


var status = [
  { id: '1', name: '11' },
  { id: '2', name: '22' },
  { id: '3', name: '33' },
];

// function test1(id) {
//   var name
//   status.forEach((s) => {
//     console.log(s);
//     console.log('id: ', id);
//     if (s.id == id) {
//       console.log(s.name);
//       name = s.name;
//       return name
//     }
//   });
//   // return name
// }
function test1(id){
  return status.find(item => item.id == id)?.name;
}

console.log('name: ', test1(2))

var nums = [1, 2, 3, 4, 5];
function test2() {
  var name
  for (i in nums) {
    if ((i = 3)) {
      name = i;
    }
  }
  return name;
}

console.log('test2: ', test2())


// function bt2() {
//   console.log(test2());
// }

// function doHomework(subject, callback) {
//   callback();
//   console.log(`Starting my ${subject} homework.`);
//   // callback();
// }
// function alertFinished() {
//   console.log('Finished my homework');
// }
// doHomework('math', alertFinished);