import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:path_provider/path_provider.dart';
import 'package:dio/dio.dart';

class Main extends StatefulWidget {
  _MainState createState() => _MainState();
}

class _MainState extends State<Main> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Flutter China Club'),
        ),
        body: Counter());
  }
}

//http dio
class HttpTest extends StatefulWidget {
  _HttpTestState createState() => _HttpTestState();
}

class _HttpTestState extends State<HttpTest> {
  final Dio dio = Dio();
  String msg = '';
  void getHttp() async {
    try {
      Response res = await dio.get('http://192.168.1.116:8000/vue_home');
      print(res);
      msg = res.headers.toString();
      // return res.data;
    } catch (e) {
      return print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        child: ListView(
      children: <Widget>[
        FloatingActionButton(
          child: Text('载入'),
          onPressed: () {
            getHttp();
          },
        ),
        Text(msg),
      ],
    ));
  }
}

class Counter extends StatefulWidget {
  _CounterState createState() => _CounterState();
}

class _CounterState extends State<Counter> {
  int _counter = 0;
  String _msg = '返回信息： ';
  int _counterInc() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Image.asset(
            './assets/images/1.jpg',
            width: 100,
          ),
          Text(
            '$_counter',
          ),
          FloatingActionButton(
            onPressed: () {
              _counterInc();
            },
            child: Text('点我'),
          ),
          RaisedButton(
              child: Text('新页面'),
              onPressed: () async {
                _msg = _msg +
                    await Navigator.push(context,
                        MaterialPageRoute(builder: (contet) {
                      return NewRouter();
                    }));
              }),
          Text('返回信息：   $_msg'),
          RandomWords(),
        ],
      ),
    );
  }
}

class NewRouter extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('new page'),
        ),
        body: Center(
          child: RaisedButton(
            child: Text('返回'),
            onPressed: () {
              Navigator.pop(context, '我回来了！');
            },
          ),
        ));
  }
}

class RandomWords extends StatelessWidget {
  final rw = WordPair.random();
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(10),
      child: Text(rw.toString()),
    );
  }
}

class TapBoxA extends StatefulWidget {
  _TapBoxAState createState() => _TapBoxAState();
}

//自己管理状态
class _TapBoxAState extends State<TapBoxA> {
  bool _active = false;
  void _handleTap() {
    setState(() {
      _active = !_active;
    });
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: _handleTap,
      child: Container(
        child: Center(
          child: Text(
            _active ? 'active' : 'inactive',
            style: TextStyle(color: Colors.white, fontSize: 32),
          ),
        ),
        width: 200,
        height: 200,
        decoration: BoxDecoration(
          color: _active ? Colors.lightGreen : Colors.grey,
        ),
      ),
    );
  }
}

//父类管理状态
class ParentWidget extends StatefulWidget {
  _ParentWidgetState createState() => _ParentWidgetState();
}

class _ParentWidgetState extends State<ParentWidget> {
  bool _active = false;
  void handleBoxChanged(bool newValue) {
    setState(() {
      _active = newValue;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: TapBoxB(
        active: _active,
        onChanged: handleBoxChanged,
      ),
    );
  }
}

class TapBoxB extends StatelessWidget {
  TapBoxB({Key key, bool active, ValueChanged<bool> onChanged})
      : _active = active,
        _onChanged = onChanged;
  final bool _active;
  final ValueChanged<bool> _onChanged;

  void _handleTap() {
    _onChanged(!_active);
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: _handleTap,
      child: Container(
        child: Center(
          child: Text(
            _active ? 'Active' : 'Inactive',
            style: TextStyle(fontSize: 32, color: Colors.white),
          ),
        ),
        width: 200,
        height: 200,
        decoration: BoxDecoration(
          color: _active ? Colors.red : Colors.blue,
        ),
      ),
    );
  }
}
