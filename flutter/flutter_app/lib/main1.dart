import 'package:flutter/material.dart';

void main() => runApp(MyAppContainer());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext content) {
    return MaterialApp(
        title: 'Text Widget',
        home: Scaffold(
            body: Center(
              child: Text(
            'Hei,maxLines属性设置最多显示的行数，比如我们现在只显示1行，类似一个新闻列表的题目。代码如下：overflow属性是用来设置文本溢出时，如何处理,它有下面几个常用的值供我们选择。',
            // textAlign: TextAlign.center,
            textAlign: TextAlign.left,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(
                fontSize: 20,
                // color: Color.fromARGB(255, 255, 100, 200),
                color: Colors.blue,
                decoration: TextDecoration.underline,
                decorationStyle: TextDecorationStyle.double,
                decorationColor: Color.fromARGB(255, 200, 200, 200)),
          ),
        )));
  }
}

class MyAppContainer extends StatelessWidget {
  @override
  Widget build(BuildContext content) {
    return MaterialApp(
      title: 'Text Widget',
      home: Scaffold(
        body: Center(
          child: Container(
            child: Text('I\'m container......',
                style: TextStyle(
                  fontSize: 40,
                )),
            alignment: Alignment.topLeft,
            height: 400,
            width: 500,
            // color: Colors.red, //用decoration 会冲突
            // padding: const EdgeInsets.all(10),
            padding: const EdgeInsets.fromLTRB(20, 20, 10, 100),
            margin: const EdgeInsets.all(10),
            decoration: BoxDecoration(
                gradient: const LinearGradient(
                    colors: [Colors.black, Colors.blue, Colors.yellow]),
                border: Border.all(width: 20, color: Colors.purple)),
          ),
        ),
      ),
    );
  }
}
