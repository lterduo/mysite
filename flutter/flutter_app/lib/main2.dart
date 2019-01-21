import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'My app',
        home: Scaffold(
            appBar: AppBar(
              title: Text('我是appBar',
                  style: TextStyle(color: Colors.red, fontSize: 20)),
            ),
            body: Container(height: 300, child: MyList1())));
  }
}

class MyList extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: <Widget>[
        Image.network(
            'http://jspang.com/static/upload/20181111/G-wj-ZQuocWlYOHM6MT2Hbh5.jpg'),
        Text('嘻嘻嘻嘻嘻嘻嘻嘻寻寻寻寻寻寻寻寻寻寻寻寻寻寻寻寻'),
        Image.network(
            'http://jspang.com/static/upload/20181111/G-wj-ZQuocWlYOHM6MT2Hbh5.jpg'),
        Container(
          child: new Text(
            'Hello JSPang',
            style: TextStyle(fontSize: 40.0),
          ),
          alignment: Alignment.center,
          height: 100,
          width: 200,
          color: Colors.red,
        ),
        Image.network(
            'http://jspang.com/static/upload/20181111/G-wj-ZQuocWlYOHM6MT2Hbh5.jpg'),
      ],
    );
  }
}

class MyList1 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ListView(
      scrollDirection: Axis.horizontal,
      children: <Widget>[
        new Container(
          width: 180.0,
          color: Colors.lightBlue,
        ),
        new Container(
          width: 180.0,
          color: Colors.amber,
        ),
        new Container(
          width: 180.0,
          color: Colors.deepOrange,
        ),
        new Container(
          width: 180.0,
          color: Colors.deepPurpleAccent,
        ),
      ],
    );
  }
}
