import 'package:flutter/material.dart';

class Test extends StatefulWidget {
  @override
  _TestState createState() => _TestState();
}

class _TestState extends State<Test> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Test'),
      ),
      body: MessageForm(),
    );
  }
}

//echo客户端
class MessageForm extends StatefulWidget {
  _MessageFormState createState() => _MessageFormState();
}

class _MessageFormState extends State<MessageForm> {
  final editController = TextEditingController();
  // 对象被从 widget 树里永久移除的时候调用 dispose 方法（可以理解为对象要销毁了）
  // 这里我们需要主动再调用 editController.dispose() 以释放资源
  @override
  void dispose() {
    super.dispose();
    editController.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Container(
          child:TextField(
          decoration: InputDecoration(
            hintText: 'Input message',
            contentPadding: EdgeInsets.all(0.0),
          ),
          style: TextStyle(fontSize: 22.0, color: Colors.black),
          controller: editController,
          // 自动获取焦点。这样在页面打开时就会自动弹出输入法
          autofocus: true,
        ),
        ),
        InkWell(
          onTap: () => debugPrint('send: ${editController.text}'),
          onDoubleTap: () => debugPrint('double tapped'),
          onLongPress: () => debugPrint('long pressed'),
          child: Container(
            padding: EdgeInsets.symmetric(vertical: 10.0, horizontal: 16.0),
            decoration: BoxDecoration(
                color: Colors.black12,
                borderRadius: BorderRadius.circular(5.0)),
            child: Text('Send'),
          ),
        ),
        ListView.builder(),
      ],
    );
  }
}

//跳转
class FirstScreen extends StatefulWidget {
  _FirstScreenState createState() => _FirstScreenState();
}

class _FirstScreenState extends State<FirstScreen> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: RaisedButton(
          child: Text('First screen'),
          onPressed: () async {
            var msg = await Navigator.push(context,
                MaterialPageRoute(builder: (context) => SecondScreen()));
            print(msg);
          }),
    );
  }
}

class SecondScreen extends StatefulWidget {
  _SecondScreenState createState() => _SecondScreenState();
}

class _SecondScreenState extends State<SecondScreen> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: RaisedButton(
          child: Text('Second screen'),
          onPressed: () async {
            var msg = await Navigator.push(context,
                MaterialPageRoute(builder: (context) => ThirdScreen()));
            print(msg);
          }),
    );
  }
}

class ThirdScreen extends StatefulWidget {
  _ThirdScreenState createState() => _ThirdScreenState();
}

class _ThirdScreenState extends State<ThirdScreen> {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: RaisedButton(
          child: Text('Third screen'),
          onPressed: () {
            Navigator.pop(context,'333');
          }),
    );
  }
}

//页面布局例子
class First extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
        child: Image.asset('./assets/images/1.jpg',
            width: 600, height: 240, fit: BoxFit.cover));
  }
}

class Second extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(32),
      child: Row(
        children: <Widget>[
          //第一个，column
          Expanded(
              child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Text(
                'hahahha',
                style: TextStyle(color: Colors.blue, fontSize: 18),
              ),
              Text('heiheihei'),
            ],
          )),
          //第二个，星
          Icon(
            Icons.star,
            color: Colors.yellow,
          ),
          //
          Container(
            margin: EdgeInsets.fromLTRB(20, 0, 0, 0),
            child: Text('41'),
          ),
        ],
      ),
    );
  }
}
